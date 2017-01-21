import os

"""
" Edit below this line to fit your needs
"""
default_linear_x=0.2
default_linear_y=0.2
#default_linear_z=0
default_angular_z=0.5
#default_angular_x=0
#default_angular_y=0
# Interface to LISTEN ("0.0.0.0" for all interfaces)
IFACE = "192.168.191.2"

# Network port to LISTEN
PORT = 5000

# I2C bus to use : 0 for older Raspberry Pi model B 256MB, 1 for others
I2CBUS = 1

# I2C address of the slave Arduino
ADDRESS = 0x04

# Get path of config file
CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))
# Streaming start script
STREAM_START = [CONFIG_PATH + "/bin/stream.sh", "start"]
# Streaming stop script
STREAM_STOP = [CONFIG_PATH + "/bin/stream.sh", "stop"]
person_START = [CONFIG_PATH + "/bin/person.sh", "start"]
person_STOP = [CONFIG_PATH + "/bin/person.sh", "stop"]
temp_START = [CONFIG_PATH + "/bin/temp.sh", "start"]
temp_STOP = [CONFIG_PATH + "/bin/temp.sh", "stop"]
medicine_START = [CONFIG_PATH + "/bin/medicine.sh", "start"]
medicine_STOP = [CONFIG_PATH + "/bin/medicine.sh", "stop"]


