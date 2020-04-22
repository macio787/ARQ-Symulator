from Receiver import Receiver
from Sender import Sender
from Transmitter import Transmitter
from Analyzer import Analyzer
from Generator import Generator

# global functions
def printInterference():
    if receiver.interference:
        print("Nie wystapilo zaklocenie")
    else:
        print("Wystapilo zaklocenie")
    return


# ---RUN---
# init
generator = Generator()
sender = Sender()
transmitter = Transmitter(0.5)
receiver = Receiver()
analyzer = Analyzer()
print("----------------------")

# generate
sender.data_raw = generator.generate(8)

# choice
mode = "PAR"
packet_length = 2
# code
print("data raw: \t\t", sender.data_raw)
sender.data_send = sender.code(mode, packet_length)
print("\t->coding mode: ", mode)
print("data send:\t\t", sender.data_send)

# send
transmitter.simulateNoise(sender.data_send)
print("sending... simulating noise...")

# receive
receiver.data_raw = sender.data_raw
receiver.data_received = transmitter.data_noised

# encode
receiver.encode(mode, packet_length)
print("\t->encoding mode: ", mode)

# print info
print("data received:\t", receiver.data_received)
printInterference()

# analyse

analyzer.setRaw(sender.data_raw)
analyzer.setReceived(receiver.data_received)
analyzer.analize("PAR", packet_length)
# TODO:: The bit error ratio (also BER) is the number of bit
#  errors divided by the total number of transferred bits during
#  a studied time interval.
#  expressed as a percentage.
#              -> TODO:: class Analyzer



