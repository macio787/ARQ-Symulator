

class Receiver:
    class Encoder:
        def __init__(self):
            print("decoder initiated")
            return

        def encode_PAR(self, _receiver, n=0):
            if n == 0:
                n = len(_receiver.data_received) - 1
            sum = 0
            i = 0
            counter = 1
            stop = len(_receiver.data_received)
            while i < stop:
                sum = sum + _receiver.data_received[i]
                if (counter) % n == 0:
                    i = i + 1
                    if sum % 2 != _receiver.data_received[i]:
                        _receiver.interference = False
                        return
                    sum = 0
                counter = counter + 1
                i = i + 1
            _receiver.interference = True
            return

        def encode_CRC(self, _receiver):
            for idx in range(1, len(_receiver.data_received)):
                if _receiver.data_received[idx] != _receiver.data_raw[idx]:
                    _receiver.interference = False
            _receiver.interference = True
            return

    # end class Decoder

    data_received = []
    data_raw = []
    encoder = Encoder()
    interference = False

    def encode(self, mode, packet_length=0):
        if packet_length==0: packet_length = len(self.data_raw)
        if mode == "PAR":
            return self.encoder.encode_PAR(self, packet_length)
        elif mode == "CRC":
            return self.encoder.encode_CRC(self, packet_length)
        return


# end class Receiver