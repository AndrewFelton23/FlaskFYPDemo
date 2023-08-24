from flask import Flask, render_template, request, jsonify, Response
import cv2

app = Flask(__name__)

def generate_frames():
    camera = cv2.VideoCapture(0)  # Use 0 for default camera or specify the video file path

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route to receive commands from the web interface
@app.route('/update_led_color', methods=['POST'])
def update_led_color():
    # Get the color information from the request's JSON payload
    data = request.get_json()
    started = data.get('start')
    print("Start sequence: "+ str(started))

    # Perform any required actions with the LED color
    # For example, you can store it in a database or trigger a physical LED to change color

    # You can also send a response back to the frontend if needed
    # For this example, we'll simply send a success response
    return jsonify({'message': 'LED color updated successfully'})

@app.route('/manual_mode', methods=['POST'])
def manual_mode():
    # Get the color information from the request's JSON payload
    Manualdata = request.get_json()
    mode = Manualdata.get('manualMode')
    print("Manual mode: " + str(mode))

    # Perform any required actions with the LED color
    # For example, you can store it in a database or trigger a physical LED to change color

    # You can also send a response back to the frontend if needed
    # For this example, we'll simply send a success response
    return jsonify({'message': 'LED color updated successfully'})

@app.route('/get_coordinates')
def get_coordinates():
    return jsonify({'joint1': 'Joint 1 position',
                    'joint2': 'Joint 2 position',
                    'joint3': 'Joint 3 position',
                    'joint4': 'Joint 4 position',
                    'gripper': 'Gripper Open or Closed'
                    })


if __name__ == '__main__':
    app.run(debug=True)
