from picamera import PiCamera

camera = PiCamera()
time.sleep(2) // seconds

# Capture image whenever ultrasonic sensor gives a warning about
# an obstacle
camera.capture("/path")
print("Image captured")
