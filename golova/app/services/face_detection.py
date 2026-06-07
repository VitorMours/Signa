from app.core.logging import setup_logger 
import time 
import numpy as np 
import mediapipe as mp 
from mediapipe.tasks import python
import cv2
from mediapipe.tasks.python.vision import (
    FaceLandmarker,
    FaceLandmarkerOptions,
    RunningMode
)
BaseOptions = mp.tasks.BaseOptions
VisionRunningMode = RunningMode
logger = setup_logger(__name__)


class HeadDetectionService:
  
  def __init__(self ) -> None:
    options = FaceLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="app/assets/face_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO,
    )
    self.landmarker = FaceLandmarker.create_from_options(options)

  face_CONNECTIONS = [
    (0,1), (1,2), (2,3), (3,4), # Polegar
    (0,5), (5,6), (6,7), (7,8), # Indicador
    (5,9), (9,10), (10,11), (11,12), # Médio
    (9,13), (13,14), (14,15), (15,16), # Anelar
    (13,17), (17,18), (18,19), (19,20), # Mindinho
    (0,17) # Palma
  ]
  
  def detect_head(self, data: bytes) -> None:
    try:
      np_arr = np.frombuffer(data, np.uint8)
      
      frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
      if frame is None:
        return {"success": False, "message": "Imagem inválida"}

      rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
      timestamp = int(time.time() * 1000)
      result = self.landmarker.detect_for_video(mp_image, timestamp)

      faces = []
      if result.face_landmarks:
        for face in result.face_landmarks:
          landmarks = []
          for landmark in face:
            landmarks.append({
              "x": float(landmark.x),
              "y": float(landmark.y),
              "z": float(landmark.z)
              })
          faces.append(landmarks)
          print(faces)
        return {"success": True,"faces": faces}

    except Exception as e:
      logger.exception("Erro ao processar gesto")
      return {"success": False, "message": str(e)}