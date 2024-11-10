import pyaudio
import websockets
import asyncio
import base64
import json


FRAMES_PER_BUFFER = 3200 # number of frames per buffer
FORMAT = pyaudio.paInt16 # 16 bit integer format
CHANNELS = 1 # 1 channel
RATE = 16000 # 16 kHz sampling rate

P = pyaudio.PyAudio() # create an interface to PortAudio, object P is a PortAudio system object

stream = P.open(format=FORMAT, 
                channels=CHANNELS,
                  rate=RATE, 
                  input=True, 
                  frames_per_buffer=FRAMES_PER_BUFFER) # open the stream

URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"


async def send_receive():
    async with websockets.connect(
        URL,
        ping_timeout = 20,
        ping_interval = 5,
        extra_headers = {"Authorization":'febfc0071dee44cbaddc0286d7724a1c'}



    ) as websocket:
        await asyncio.sleep(0.1)    
        session = await websocket.recv()
        print(session)
        print("Sending message")

        async def send_audio():
            while True:
              try:
                data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
                data = base64.b64encode(data).decode("utf-8")
                json_data = json.dumps({"audio_data": str(data)})
                await websocket.send(json_data)
              except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
              except Exception as e:
                    assert False, "Not a websocket 4008 error"
              await asyncio.sleep(0.01) 
            return True   

        async def receive_text():
            while True:
                  
              try:
                result_string = await websocket.recv()
                result = json.loads(result_string)
                prompt = result['text']
                if prompt and result['message_type'] == 'FinalTranscript':
                   
                   print("Me:", prompt)
                   print("Bot:", "this is my answer")

              except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
              except Exception as e:
                    assert False, "Not a websocket 4008 error"

        send_result,receive_result = await asyncio.gather(send_audio(), receive_text())



asyncio.run(send_receive())       