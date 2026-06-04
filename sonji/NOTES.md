Isso daqi pode ser a forma correta de fazer com que o processamento seha feita pela api


```python
import asyncio
from concurrent.futures import ThreadPoolExecutor
import cv2
import mediapipe as mp
from fastapi import FastAPI, WebSocket

app = FastAPI()
executor = ThreadPoolExecutor(max_workers=4)  # Ajuste conforme os cores da CPU

# Inicialização do MediaPipe (pode precisar estar dentro da thread, cuidado com thread-safety)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

def process_frame(frame_bytes):
    # Converte bytes para imagem OpenCV
    # Executa o MediaPipe
    # Retorna os pontos (landmarks)
    ...
    return landmarks

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    loop = asyncio.get_running_loop()
    
    try:
        while True:
            # Recebe os bytes da imagem (pode ser base64 ou binário puro)
            data = await websocket.receive_bytes()
            
            # Envia para o ThreadPoolExecutor sem bloquear o Event Loop
            landmarks = await loop.run_in_executor(executor, process_frame, data)
            
            # Envia o resultado de volta
            await websocket.send_json(landmarks)
    except Exception as e:
        print(f"Conexão encerrada: {e}")

```