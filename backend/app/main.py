from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
	"http://localhost:3000",
	"localhost:3000"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	count = 0
	while True:
		try:
			# Получаем данные
			data = await websocket.receive_json()
			count += 1
			# Здесь можем что то с этими данными сделать, обработать их
			data['count'] = count
			# и далее отправляем их клиенту
			await websocket.send_json(data)
		except Exception as e:
			print('error:', e)
			break

