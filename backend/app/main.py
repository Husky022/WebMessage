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
			data = await websocket.receive()
			data_dict = json.loads(data['text'])
			count += 1
			print(count)
			# Здесь можем что то с этими данными сделать, обработать их
			data_dict['count'] = count
			data_str = json.dumps(data_dict)
			# и далее отправляем их клиенту
			await websocket.send_text(data_str)
		except Exception as e:
			print('error:', e)
			break

