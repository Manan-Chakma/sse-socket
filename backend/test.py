from time import sleep
import sseclient

msgs = sseclient.SSEClient('http://localhost:5000/listen')

for msg in msgs:
    print(msg)