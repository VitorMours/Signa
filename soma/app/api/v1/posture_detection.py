from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.core.logging import setup_logger
from app.services.posture_detection import PostureDetectionService
import asyncio


def get_posture_detection_service():
  return PostureDetectionService()

router = APIRouter(prefix="/posture-detection")
logger = setup_logger(__name__)
logger.info("Posture detection router initialized")


@router.get("/health")
async def check_health():
  logger.info("Health check requested successfully")
  return {"status": "ok"}


@router.post("/start")
async def start_posture_detection(service: PostureDetectionService = Depends(get_posture_detection_service),):
  logger.info("Posture detection process initialized via HTTP")
  return {"status": "ready"}


@router.websocket("/process")
async def process_gesture(websocket: WebSocket, service: PostureDetectionService = Depends(get_posture_detection_service),):
  headers = dict(websocket.headers)
  client_origin = headers.get("origin")
  logger.info(f"Tentativa de conexão WebSocket vinda de: {client_origin}")
  
  await websocket.accept()
  logger.info("Cliente WebSocket conectado para detecção de postura.")

  try:
    while True:
      data = await websocket.receive_bytes()

      posture_result = service.detect_posture(data=data)
      await websocket.send_json({"posture": posture_result})
      await asyncio.sleep(0.01)

  except WebSocketDisconnect:
    logger.info("Conexão WebSocket fechada graciosamente pelo cliente.")
  except Exception as e:
    logger.error(f"Erro na conexão WebSocket: {e}")
