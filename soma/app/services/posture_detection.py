from app.core.logging import setup_logger 
import time 
import numpy as np 
import mediapipe as mp 
import cv2

from mediapipe.tasks.python.vision import (
    PoseLandmarker,
    PoseLandmarkerOptions,
    RunningMode
)
from mediapipe.tasks.python.core.base_options import BaseOptions

logger = setup_logger(__name__)

class PostureDetectionService:
  
  def __init__(self) -> None:
    options = PoseLandmarkerOptions(
      base_options=BaseOptions(
          model_asset_path="app/assets/pose_landmarker_full.task"
      ),
      running_mode=RunningMode.VIDEO,
      num_poses=2 
    )
    self.landmarker = PoseLandmarker.create_from_options(options)

  def detect_posture(self, data: bytes) -> dict:
    try:
      np_arr = np.frombuffer(data, np.uint8)
      
      frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
      if frame is None:
        return {"success": False, "message": "Imagem inválida"}

      rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
      
      # Timestamp obrigatório para o RunningMode.VIDEO
      timestamp = int(time.time() * 1000)
      result = self.landmarker.detect_for_video(mp_image, timestamp)

      poses = []
      # Corrigido para extrair 'pose_landmarks' em vez de 'hand_landmarks'
      if result.pose_landmarks:
        for pose in result.pose_landmarks:
          landmarks = []
          for landmark in pose:
            landmarks.append({
              "x": float(landmark.x),
              "y": float(landmark.y),
              "z": float(landmark.z),
              "visibility": float(landmark.visibility) if hasattr(landmark, 'visibility') else 0.0
              })
          poses.append(landmarks)
          
      return {"success": True, "poses": poses}

    except Exception as e:
      logger.exception("Erro ao processar postura")
      return {"success": False, "message": str(e)}