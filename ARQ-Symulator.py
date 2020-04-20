import random, komm, numpy


class Generator:
    def __init__(self):
        print("generator initiated")
        return

    def generate(self, n):
        data = []
        for n in range(n):
            data.append(random.randint(0, 1))
        return data
# end class Generator


class Sender:

    class Coder:
        def __init__(self):
            print("coder initiated")
            return

        def code_PAR(self, data):
            n = len(data)
            sum = 0
            i = 0
            counter = 1
            stop = len(data) + len(data) / n
            while i < stop:
                sum = sum + data[i]
                if (counter) % n == 0:
                    i = i + 1
                    data.insert(i, sum % 2)
                    sum = 0
                counter = counter + 1
                i = i + 1
            return data

        def code_CRC(self, data):
            n = len(data)
            # TODO::czy to sie w ogole jakos koduje...
            return
    # end class Coder

    data = []
    coder = Coder()

    def code(self, mode):
        if mode == "PAR":
            self.coder.code_PAR(self.data)
            print("coding mode: PARITY BIT")
        elif mode == "CRC":
            self.coder.code_CRC(self.data)
            print("coding mode: CRC")
        return

    def send(self, _transmitter):
        _transmitter.simulateNoise(self.data)
        return
# end class Sender


class Transmitter:
    def __init__(self):
        print("Transmitter initiated")
        return

    data_noised = []

    def simulateNoise(self, data_sent):
        data_nsd = data_sent.copy()
        # TODO::NOISE
        data_nsd[2] = 0
        # TODO::NOISE
        self.data_noised = data_nsd
        return
# end class Transmission


class Receiver:

    class Encoder:
        def __init__(self):
            print("decoder initiated")
            return

        def encode_CRC(self, data_rcvd, data_snt):
            for idx in range(1, len(data_rcvd)):
                if data_rcvd[idx] != data_snt[idx]:
                    return False
            return True
    # end class Decoder

    data_received = []
    data_sent = []
    encoder = Encoder()

    def encode(self, mode):
        good = False
        if mode == "PAR":
            # TODO::
            print("encoding mode: PARITY BIT")
        elif mode == "CRC":
            # TODO::
            print("encoding mode: CRC")
            good = self.encoder.encode_CRC(self.data_received, self.data_sent)
        return good

    def updateDataReceived(self, dr):
        self.data_received = dr
        return

    def updateDataSent(self, ds):
        self.data_sent = ds
        return
# end class Receiver


# run
generator = Generator()
sender = Sender()
transmitter = Transmitter()
receiver = Receiver()
print("----------------------")

sender.data = generator.generate(4)

sender.send(transmitter)

receiver.updateDataSent(sender.data)
receiver.updateDataReceived(transmitter.data_noised)

if receiver.encode("CRC"):
    print("Nie wystapilo zaklocenie")
else:
    print("Wystapilo zaklocenie")

print("\ndata sent: \t\t", receiver.data_sent)
print("data received:\t", receiver.data_received)

# print(data)
# print(code_parity_bit(data, 4))
