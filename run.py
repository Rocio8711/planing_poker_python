import webbrowser
import uvicorn
import threading
import time

def open_browser():
    time.sleep(1)  # Espera 1 segundo para que el servidor arranque
    webbrowser.open("http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#python run.py