# sender.py
from digi.xbee.devices import XBeeDevice

# Adjust COM port and baud rate to match your XCTU settings
PORT = "COM3"   # e.g., COM3 on Windows or /dev/ttyUSB0 on Linux
BAUD_RATE = 9600

# Destination 64-bit or 16-bit address of the other XBee
DEST_ADDR_16 = b'\x00\x02'   # if MY of the receiver is 0x0002

def main():
    device = XBeeDevice(PORT, BAUD_RATE)
    try:
        device.open()
        print("Device opened. Sending message...")

        # Look up the remote device
        remote_device = device.get_network().discover_device("00 02")
        # If discover_device doesn't work, you can manually create:
        if remote_device is None:
            from digi.xbee.devices import RemoteXBeeDevice, XBee16BitAddress
            remote_device = RemoteXBeeDevice(device, XBee16BitAddress.from_bytes(DEST_ADDR_16))

        message = "Hello from Router 1!"
        device.send_data(remote_device, message)
        print(f"Sent: {message}")

    finally:
        if device.is_open():
            device.close()
            print("Device closed.")

if __name__ == "__main__":
    main()
