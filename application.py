from flask import Flask, render_template  # Importing the Flask framework and the render_template function from it
from flask_socketio import SocketIO  # Importing the SocketIO extension for Flask
import serial  # Importing the serial module for serial communication
import time  # Importing the time module for time-related functions
import threading  # Importing the threading module for multi-threading support
import os  # Importing the os module for operating system-related functions

# Getting the directory name of the current file
project_root = os.path.dirname(__file__)
# Creating a path to the template directory within the project root
template_path = os.path.join(project_root, 'app/templates')

# Creating a Flask application instance
app = Flask(__name__)
# Creating a SocketIO instance, passing the Flask app instance to it
socketio = SocketIO(app)

# Function to extract latitude and longitude information from GPS data
def GPS_Info(NMEA_buff):
    nmea_latitude = NMEA_buff[1]
    nmea_longitude = NMEA_buff[3]

    lat = float(nmea_latitude)
    longi = float(nmea_longitude)

    lat_in_degrees = convert_to_degrees(lat)
    long_in_degrees = convert_to_degrees(longi)

    return lat_in_degrees, long_in_degrees

# Function to convert raw GPS data to degrees format
def convert_to_degrees(raw_value):
    decimal_value = raw_value / 100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value)) / 0.6
    position = degrees + mm_mmmm
    position = "%.4f" % position
    return position

# Function to continuously send GPS location updates
def send_location():
    global lat_in_degrees, long_in_degrees
    while True:
         received_data = str(ser.readline())  # Read data from the serial port
         GPGGA_data_available = received_data.find(gpgga_info)  # Check if GPS data is available

         if GPGGA_data_available > 0:  # If GPS data is available
             # Extract GPS data from the received string
             GPGGA_buffer = received_data.split("$GPGGA,", 1)[1]
             NMEA_buff = GPGGA_buffer.split(',')
             # Convert GPS data to latitude and longitude in degrees format
             lat_in_degrees, long_in_degrees = GPS_Info(NMEA_buff)

             # Emit the latest location to all connected clients
             socketio.emit('update_location', {'lat': lat_in_degrees, 'long': long_in_degrees})

             # Wait for a short interval (e.g., 1 second)
             time.sleep(1)

# Flask route to render the index template
@app.route('/')
def index():
    return render_template('index_socketio.html')  # Render the HTML template

if __name__ == '__main__':
    gpgga_info = "$GPGGA,"  # Define the GPGGA information string
    # ser = serial.Serial("/dev/ttyUSB0")  # Open the serial port connection (commented out for testing)
    GPGGA_buffer = 0  # Initialize GPS data buffer
    NMEA_buff = 0  # Initialize NMEA buffer
    lat_in_degrees = 0  # Initialize latitude in degrees
    long_in_degrees = 0  # Initialize longitude in degrees

    # Start the SocketIO server in a separate thread
    socket_thread = threading.Thread(target=socketio.run, kwargs={'app': app, 'host': '0.0.0.0', 'port': 5000, 'debug': False})
    socket_thread.daemon = True
    socket_thread.start()

    # Start sending location updates in a separate thread
    send_location_thread = threading.Thread(target=send_location)
    send_location_thread.daemon = True
    send_location_thread.start()
    
    # Run the Flask application
    app.run()
