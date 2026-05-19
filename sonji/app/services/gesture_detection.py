from app.core.logging import setup_logger 
import time 
import numpy as np 
import mediapipe as mp 
from mediapipe.tasks import python
import cv2

logger = setup_logger(__name__)


class GestureDetectionService:
  HAND_CONNECTIONS = [
    (0,1), (1,2), (2,3), (3,4), # Polegar
    (0,5), (5,6), (6,7), (7,8), # Indicador
    (5,9), (9,10), (10,11), (11,12), # Médio
    (9,13), (13,14), (14,15), (15,16), # Anelar
    (13,17), (17,18), (18,19), (19,20), # Mindinho
    (0,17) # Palma
  ]
  
  @staticmethod
  def detect_gesture(data) -> None:
    try:
      logger.info("Processing gesture data")
    except Exception as e:
      logger.error(f"Houve um problema durante o processamento de gestos: {e}")