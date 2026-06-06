from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.core.logging import setup_logger
from app.services.gesture_detection import GestureDetectionService
import asyncio


def get_gesture_detection_service():
  return GestureDetectionService()

router = APIRouter(prefix="/gesture-detection")
logger = setup_logger(__name__)
logger.info("Gesture detection router initialized")


@router.get("/health")
async def check_health():
  logger.info("Health check requested successfully")
  return {"status": "ok"}


@router.post("/start")
async def start_gesture_detection(service: GestureDetectionService = Depends(get_gesture_detection_service),):
  # Se for apenas para dar um "trigger" inicial, está ok.
  # Mas o ideal é que o streaming de dados aconteça no WebSocket abaixo.
  logger.info("Gesture detection process initialized via HTTP")
  return {"status": "ready"}


@router.websocket("/process")
async def process_gesture(websocket: WebSocket, service: GestureDetectionService = Depends(get_gesture_detection_service),):
  headers = dict(websocket.headers)
  client_origin = headers.get("origin")
  logger.info(f"Tentativa de conexão WebSocket vinda de: {client_origin}")
  
  await websocket.accept()
  logger.info("Cliente WebSocket conectado para detecção de gestos.")

  try:
    while True:
      data = await websocket.receive_bytes()

      gesture_result = service.detect_gesture(data=data)
      await websocket.send_json({"gesture": gesture_result})
      await asyncio.sleep(0.01)

  except WebSocketDisconnect:
    logger.info("Conexão WebSocket fechada graciosamente pelo cliente.")
  except Exception as e:
    logger.error(f"Erro na conexão WebSocket: {e}")
