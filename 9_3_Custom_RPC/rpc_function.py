import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

s.write(bytes("\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

while 1:
    s.write(bytes("/LEDControl_ORANGE/run 1\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/LEDControl_ORANGE/run 0\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

while 1:
    s.write(bytes("/LEDControl_GREEN/run 1\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/LEDControl_GREEN/run 0\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)


# s.write(bytes("/LEDControl/run 3 0\r", 'UTF-8'))
# line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
# print(line)
# line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
# print(line)
# time.sleep(1)

# s.write(bytes("/LEDControl/run 1 0\r", 'UTF-8'))
# line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
# print(line)
# line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
# print(line)

s.close()