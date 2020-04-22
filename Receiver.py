import crc16


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

        def encode_CRC(self, _receiver, n):
            if n > 16:
                n = 16
            # separate packets and generate key for each
            tmp_arr = []
            for i in range(0, len(_receiver.data_received)):
                tmp_arr.append(_receiver.data_received[i])
                if i % n == (n - 1):
                    _receiver.key_crc_received.append(crc16.crc16xmodem(
                        self.arrayToBytes(tmp_arr)))
                    tmp_arr.clear()
            return

        def arrayToBytes(self, data):
            tmp = ''
            for i in range(len(data)):
                tmp += str(data[i])
            tmp = bytes(tmp, 'utf-8')
            return tmp
    # end class Decoder

    data_received = []
    data_raw = []
    key_crc_correct = []
    key_crc_received = []
    interference = False
    encoder = Encoder()

    def encode(self, mode, packet_length=0):
        if packet_length == 0:
            packet_length = len(self.data_raw)
        if mode == "PAR":
            return self.encoder.encode_PAR(self, packet_length)
        elif mode == "CRC":
            return self.encoder.encode_CRC(self, packet_length)
        return


# end class Receiver