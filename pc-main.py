import serial
import time
import serial.tools.list_ports

# Define the expected VID and PID for the Raspberry Pi Pico
EXPECTED_VID = '2E8A'
EXPECTED_PID = '0005'

def handshake(ser):
    for _ in range(3):  # Retry up to 3 times
        ser.write(b"syn\n")  # Send SYN
        time.sleep(0.2)  # Increased delay to ensure the message is sent
        response = ser.readline().decode('utf-8').strip()  # Wait for SYN-ACK
        if not response:
            print("Empty response, retrying...")
            time.sleep(0.1)
            continue
        if "syn-ack" in response:
            ser.write(b"ack\n")  # Send ACK
            return True  # Handshake successful
        time.sleep(0.2)  # Delay before retrying
    return False  # Handshake failed

def find_pico_port():
    # List all available COM ports
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Check if the port has the expected VID and PID
        if (EXPECTED_VID in port.hwid) and (EXPECTED_PID in port.hwid):
            return port.device
    return None

def main():
    connected_port = None
    while True:
        # Try to find the Pico port
        pico_port = find_pico_port()
        if pico_port:
            if pico_port != connected_port:
                print(f"Connected to {pico_port}")
                connected_port = pico_port
            try:
                # Open the serial port
                with serial.Serial(pico_port, 115200, timeout=1) as ser:
                    if not handshake(ser):
                        print("Handshake failed")
                        continue
                    print(f"Handshake successful on {pico_port}")
                    while True:
                        if ser.in_waiting > 0:
                            # Read and print the incoming data
                            data = ser.readline().decode('utf-8').strip()
                            print(data)
                        time.sleep(0.2)
            except serial.SerialException as E:
                print(f"{E}: most likely device disconnect")
                connected_port = None
                time.sleep(1)  # Wait before retrying
        else:
            if connected_port is not None:
                print("Pico not found. Checking again...")
                connected_port = None
            time.sleep(3)  # Wait before trying again

if __name__ == "__main__":
    main()