import serial
import time

# Configure the serial connection
stm32_port = '/dev/ttyACM1'  # Replace with your STM32 port
baud_rate = 9600  # Match the baud rate in your STM32 firmware

try:
    # Open serial connection
    ser = serial.Serial(stm32_port, baud_rate, timeout=1)

    while True:
        command = input("Enter 1 to turn ON LED, 0 to turn OFF LED: ").strip()
        if command in ['0', '1']:
            ser.write(command.encode())  # Send the command
            print(f"Command '{command}' sent to STM32.")
        else:
            print("Invalid command. Enter '1' or '0'.")
except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    if 'ser' in locals():
        ser.close()
