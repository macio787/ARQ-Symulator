from Receiver import Receiver
from Sender import Sender
from Transmitter import Transmitter
from Analyzer import Analyzer
from Generator import Generator

# functions

def printInterference():
    if receiver.interference:
        print("Nie wystapilo zaklocenie")
    else:
        print("Wystapilo zaklocenie")
    return


def arrToStr(data):
    tmp = ''
    for i in range(len(data)):
        tmp += str(data[i])
    return tmp

# ---RUN---
# parametres

mode = "CRC"
data_length = 4
packet_length = 2
cross_prob = 0.6

# init
generator = Generator()
sender = Sender()
transmitter = Transmitter(cross_prob)
receiver = Receiver()
analyzer = Analyzer(sender, receiver)

running = True
while running:
    print("---Menu---")
    print("1.zmien tryb: ", mode,
          "\n2.zmien dlugosc sygnalu:", data_length,
          "\n3.zmien dlugosc pakietu:", packet_length,
          "\n4.zmien prawdopodobienstwo zaklocenia:", cross_prob,
          "\n5.Uruchom symulacje",
          "\n0.Wyjdz z programu")
    choice = input()
    if choice == "0":
        running = False
    elif choice == "1":
        mode = input("podaj tryb: (CRC/PAR): ")
    elif choice == "2":
        data_length = int(input("podaj dlugosc sygnalu(int): "))
    elif choice == "3":
        packet_length = int(input("podaj dlugosc pakietu(int): "))
    elif choice == "4":
        cross_prob = float(input("podaj prawdopodobienstwo zaklocenia: (0 <= x >= 1): "))
    elif choice == "5":
        err = False
        if mode != "CRC" and mode != "PAR":
            print("Nieprawidlowy tryb: ", mode)
            err = True
        if cross_prob < 0 or cross_prob > 1:
            print("Nieprawidlowe prawdopodobienstwo zaklocenia: ", cross_prob)
            err = True
        if not err:
            print("------\n")
            # generate
            sender.data_raw = generator.generate(data_length)
            # code
            sender.data_send = sender.code(mode, packet_length)
            print("<-Data sent:\t\t", arrToStr(sender.data_send))
            # send
            transmitter.simulateNoise(sender.data_raw)
            print("Simulating noise...")

            # receive
            receiver.key_crc_correct = sender.key_crc
            receiver.data_raw = sender.data_raw
            receiver.data_received = transmitter.data_noised

            print("->Data received:\t", arrToStr(receiver.data_received))
            analyzer.analize(mode, packet_length)
            print("------\n")


