# receiver.py
from digi.xbee.devices import XBeeDevice

PORT = "COM4"   # receiver XBee's COM port
BAUD_RATE = 9600

def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    def data_receive_callback(xbee_message):
        data = xbee_message.data.decode('utf-8')
        sender = xbee_message.remote_device.get_16bit_addr()
        print(f"Received data from {sender}: {data}")

    try:
        device.open()
        device.add_data_received_callback(data_receive_callback)
        print("Receiver is ready. Waiting for messages...")
        input("Press Enter to exit...\n")
    finally:
        if device.is_open():
            device.close()
            print("Receiver closed.")

if __name__ == "__main__":
    main()
