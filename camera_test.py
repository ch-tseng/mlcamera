# camera_test.py

import picamera
import inception_predict

# Create camera interface
camera = picamera.PiCamera()
while True:
    # Take the jpg image from camera
    print "Capturing"
    filename = '/home/pi/cap.jpg'
    # Show quick preview of what's being captured
    camera.start_preview()
    camera.capture(filename)
    camera.stop_preview()
    
    # Run inception prediction on image
    print "Predicting"
    topn = inception_predict.predict_from_local_file(filename, N=5)
    
    # Print the top N most likely objects in image (default set to 5, change this in the function call above)
    print topn
