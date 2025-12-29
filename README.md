# Real-Time-GPS-Tracking-System-using-Raspberry-Pi-4

-> Real-Time GPS Tracking System using Raspberry Pi 4
This project implements a real-time GPS tracking system using Raspberry Pi 4 and an L80 GPS module, where live location data (latitude, longitude, altitude, satellites, fix quality, HDOP) is read from the GPS receiver and displayed dynamically on Google Maps via a Flask + WebSocket based web interface.
The system continuously reads NMEA GPS data, processes it in Python, and updates the user's location on an interactive web map in real-time.

-> Key Features
Live GPS data acquisition (Latitude, Longitude, Altitude, HDOP, Fix quality)
Serial communication between Raspberry Pi and GPS module
NMEA sentence parsing using pynmea2
Real-time web visualization using:
Flask
Flask-SocketIO
Google Maps API
Automatic map refresh without page reload

-> Hardware Used
Raspberry Pi 4
L80 GPS Module with baseboard
USB to RS232 converter
Power cables

-> Software & Libraries
Install the required libraries:
pip install pyserial
pip install pynmea2
pip install Flask
pip install flask-socketio

-> Project Structure
GPS-Tracking-System/

│
├── gps_reader.py          # Reads GPS data from serial port

├── socket_server.py       # Flask + SocketIO server

├── templates/

│   └── index_socket.html  # Google Maps UI

├── report.pdf             # Detailed project report

└── README.md


-> How to Run
Step 1 – Connect Hardware
Connect the GPS module to Raspberry Pi using USB-to-RS232.

Step 2 – Check Serial Port
ls /dev/ttyUSB*

Update the port in Python code (e.g., /dev/ttyUSB0).

Step 3 – Run the server
python socket_server.py

Step 4 – Open Browser
Open:
http://127.0.0.1:5000

Your real-time GPS location will be shown on Google Maps.

-> Applications
Vehicle tracking
Fleet management
Navigation systems
IoT-based location services
Asset tracking

-> Author
Srihari A S
Electronics & Communication Engineering
