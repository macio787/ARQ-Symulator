import random, komm, numpy
import Generator, Sender, Transmitter, Receiver, Analyzer


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
sender.data_raw = generator.generate(4)

# choice
mode = "CRC"
# code
print("data raw: \t\t", sender.data_raw)
sender.data_send = sender.code(mode)
print("\t->encoding mode: ", mode)
print("data send:\t\t", sender.data_send)

# send
transmitter.simulateNoise(sender.data_send)
print("sending... simulating noise...")

# receive
receiver.data_raw = sender.data_raw
receiver.data_received = transmitter.data_noised

# encode
receiver.encode(mode)

# print info
print("data received:\t", receiver.data_received)
printInterference()

# analyse
# TODO:: The bit error ratio (also BER) is the number of bit
#  errors divided by the total number of transferred bits during
#  a studied time interval.
#  expressed as a percentage.
#              -> TODO:: class Analyzer



