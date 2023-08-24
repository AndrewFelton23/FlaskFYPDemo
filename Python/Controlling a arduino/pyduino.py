import serial
import time

arduino = "/dev/tty.usbmodem141301"

# Replace 'COM3' with the appropriate serial port of your Arduino (e.g., '/dev/ttyACM0' on Linux)
ser = serial.Serial(arduino, 9600, timeout=1)

def turn_led_on():
    ser.write(b'1')
    print("LED turned ON")

def turn_led_off():
    ser.write(b'0')
    print("LED turned OFF")

if __name__ == "__main__":
    while True:
        choice = input("Enter 1 to turn on the LED, 0 to turn off the LED, or q to quit: ")
        if choice == '1':
            turn_led_on()
        elif choice == '0':
            turn_led_off()
        elif choice == 'q':
            break
        else:
            print("Invalid input. Try again.")
        time.sleep(0.1)

ser.close() # Close the serial connection when done
