import requests
import cv2

def main():
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

main()