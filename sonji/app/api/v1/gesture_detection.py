from fastapi import APIRouter, WebSocket, Depends
from app.core.logging import setup_logger
from app.services.gesture_detection import GestureDetectionService

logger = setup_logger(__name__)
def get_gesture_detection_service():
  return GestureDetectionService()


router = APIRouter(prefix="/gesture-detection")
logger.info("Gesture detection router initialized")

@router.get("/health")
async def check_health():
  """Checking the health of the gesture detection service on the api"""
  logger.info("Health check requested successfully")
  return {"status": "ok"} 

@router.post("/start")
async def start_gesture_detection(service: GestureDetectionService = Depends(get_gesture_detection_service)):
  """Starting the gesture detection process on the api"""
  service.detect_gesture(data=None)
  logger.info("Gesture detection process started")
  return {"status": "started"} 

@router.websocket("/process")
async def process_gesture(websocket: WebSocket):
  await websocket.accept()
  try:
    while True:
      data = await websocket.receive_bytes()
  except Exception as e:
    logger.error(f"WebSocket connection closed: {e}")