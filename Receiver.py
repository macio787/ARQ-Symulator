import crc16
import numpy


class Receiver:
    def encode_PAR(self, n):
        sum = 0
        i = 0
        counter = 1
        stop = len(self.data_received)
        while i < stop:
            sum += self.data_received[i]
            if counter % n == 0:
                val = sum % 2
                self.data_received = numpy.concatenate([self.data_received, [val]])
                sum = 0
            counter += 1
            i += 1
        return

    def encode_CRC(self, n):
        if n > 16:
            n = 16
        i = 0
        counter = 1
        stop = len(self.data_received)
        arr = []
        while i < stop:
            arr.append(self.data_received[i])
            if counter % n == 0:
                val = crc16.crc16xmodem(self.arrayToBytes(arr))
                self.data_received = numpy.concatenate([self.data_received, [val]])
                arr.clear()
            counter += 1
            i += 1
        return

    def arrayToBytes(self, data):
        tmp = ''
        for i in range(len(data)):
            tmp += str(data[i])
        tmp = bytes(tmp, 'utf-8')
        return tmp

    data_received = []
    data_raw = []
    key_crc_correct = []
    key_crc_received = []

    def encode(self, mode, packet_length=0):
        if packet_length == 0:
            packet_length = len(self.data_raw)
        if mode == "PAR":
            self.encode_PAR(packet_length)
        elif mode == "CRC":
            self.encode_CRC(packet_length)
        return


# end class Receiver