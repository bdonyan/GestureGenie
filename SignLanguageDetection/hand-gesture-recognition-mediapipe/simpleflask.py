# from flask import Flask, make_response, render_template, request
#
# app = Flask(__name__)
#
# frame = None  # global variable to keep single JPG
#
#
# @app.route('/upload', methods=['PUT'])
# def upload():
#     global frame
#
#     # keep jpg data in global variable
#     frame = request.data
#
#     return "OK"
#
#
# @app.route('/video')
# def video():
#     if frame:
#         return make_response(frame)
#     else:
#         return ""
#
#
# @app.route('/')
# def index():
#     return 'image:<br><img src="/video">'
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, Response, render_template_string, request
import time

app = Flask(__name__)

frame = None  # global variable to keep single JPG,


# at start you could assign bytes from empty JPG

@app.route('/upload', methods=['PUT'])
def upload():
    global frame

    # keep jpg data in global variable
    frame = request.data

    return "OK"


def gen():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'\r\n' + frame + b'\r\n')
        time.sleep(0.04)  # my Firefox needs some time to display image / Chrome displays image without it
        # 0.04s = 40ms = 25 frames per second


@app.route('/video')
def video():
    if frame:
        # if you use `boundary=other_name` then you have to yield `b--other_name\r\n`
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return ""


@app.route('/')
def index():
    return 'image:<br><img src="/video">'
    # return render_template_string('image:<br><img src="{{ url_for("video") }}">')


if __name__ == "__main__":
    app.run(debug=True)  # , use_reloader=False)