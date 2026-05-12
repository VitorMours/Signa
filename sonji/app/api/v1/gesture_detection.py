from fastapi import APIRouter, WebSocket

router = APIRouter(prefix="/gesture-detection")

@router.get("/health")
async def check_health():
  """Checking the health of the gesture detection service on the api"""
  return {"status": "ok"} 

@router.post("/detect")
async def detect_gesture():
  pass 

@router.websocket("/process")
async def process_gesture(websocket: WebSocket):
  await websocket.accept()
  try:
    while True:
      data = await websocket.receive_text()
      # Process the received data and perform gesture detection
      # For example, you can call a function to analyze the data and return results
      result = "Processed gesture data: " + data
      await websocket.send_text(result)
  except Exception as e:
    print(f"WebSocket connection closed: {e}")