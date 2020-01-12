import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("### opened ###")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws?token=64346f05509d5bcc4a0c7672626fd2ee1334593a",
    # ws = websocket.WebSocketApp("ws://akv-technopark.herokuapp.com:44810/3ca5b05abc2c463",
    # ws = websocket.WebSocketApp("ws://localhost:8081/0b1d940686904e2",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
