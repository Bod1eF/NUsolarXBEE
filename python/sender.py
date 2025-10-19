# sender.py
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress

PORT = "COM3"      # change to your sender’s COM port
BAUD_RATE = 9600

DEST_ADDR_64 = XBee64BitAddress.from_hex_string("13A2004157BEB1")

def main():
    device = XBeeDevice(PORT, BAUD_RATE)
    try:
        device.open()
        print("Device opened. Sending message...")

        remote_device = RemoteXBeeDevice(device, DEST_ADDR_64)

        message = "Hello from Router 1!"
        device.send_data(remote_device, message)
        print(f"Sent: {message}")

    finally:
        device.close()
        print("Device closed.")

if __name__ == "__main__":
    main()
