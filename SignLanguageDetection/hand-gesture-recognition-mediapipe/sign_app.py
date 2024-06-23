from flask import Flask
from app import run_app
import requests
import cv2


app = Flask(__name__)

in_memory_datastore = {
    "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
    "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
    "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}


@app.get('/process-image')
def list_programming_languages():
    run_app()

if __name__ == "__main__":
   app.run()


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if success:
        cv2.imshow("OUTPUT", img)

        _, imdata = cv2.imencode('.JPG', img)

    print('.', end='', flush=True)

    requests.put('http://127.0.0.1:5000/upload', data=imdata.tobytes())

    if cv2.waitKey(40) == 27:  # 40ms = 25 frames per second (1000ms/40ms)
        break

cv2.destroyAllWindows()
cap.release()