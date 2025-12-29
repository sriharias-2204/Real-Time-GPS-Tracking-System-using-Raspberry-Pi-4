import serial
import pynmea2

def read_gps_data(serial_port):
    try:
        # Open the serial port connection with the specified settings
        with serial.Serial(serial_port, 9600, timeout=1) as ser:
            # Loop indefinitely to continuously read GPS data
            while True:
                # Read a line of data from the serial port and decode it as UTF-8
                sentence = ser.readline().decode('utf-8')
                # Check if the sentence starts with '$GP' (indicating it's a GPS sentence)
                if sentence.startswith('$GP'):
                    # Parse the NMEA sentence using pynmea2
                    msg = pynmea2.parse(sentence)
                    # Check if the parsed message is of type GGA (Global Positioning System Fix Data)
                    if isinstance(msg, pynmea2.types.talker.GGA):
                        # Print the parsed GPS data
                        print("Latitude: {}".format(msg.latitude))
                        print("Longitude: {}".format(msg.longitude))
                        print("Altitude: {} meters".format(msg.altitude))
                        print("Fix Quality: {}".format(msg.gps_qual))
                        print("Number of Satellites: {}".format(msg.num_sats))
                        print("Horizontal Dilution of Precision (HDOP): {}".format(msg.horizontal_dil))
                        print("===================================")

    # Catch and handle serial communication errors
    except serial.SerialException as e:
        print("Error reading from the GPS module: {}".format(e))
    # Catch and handle any unexpected errors
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

if __name__ == "__main__":
    # Specify the serial port where your GPS module is connected (e.g., '/dev/ttyUSB0')
    serial_port = '/dev/ttyUSB0'  # Update this with your specific serial port

    # Call the function to read GPS data from the specified serial port
    read_gps_data(serial_port)
