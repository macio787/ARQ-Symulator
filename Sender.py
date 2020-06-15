import crc16, numpy


class Sender:

    def code_PAR(self, data, n):
        data_snd = data.copy()
        sum = 0
        i = 0
        counter = 1
        stop = len(data_snd)
        while i < stop:
            sum = sum + data_snd[i]
            if (counter) % n == 0:
                data_snd.append(sum % 2)
                sum = 0
            counter += 1
            i = i + 1
        return data_snd

    def code_CRC(self, data, n):
        if n > 16:
            n = 16
        data_snd = data.copy()
        i = 0
        counter = 1
        stop = len(data_snd)
        arr = []
        while i < stop:
            arr.append(data_snd[i])
            if counter % n == 0:
                val = crc16.crc16xmodem(self.arrayToBytes(arr))
                data_snd = numpy.concatenate([data_snd, [val]])
                arr.clear()
            counter += 1
            i += 1
        return data_snd

    def arrayToBytes(self, data):
        tmp = ''
        for i in range(len(data)):
            tmp += str(data[i])
        tmp = bytes(tmp, 'utf-8')
        return tmp

    data_raw = []
    data_send = []
    key_crc = []

    def code(self, mode, packet_length=0):
        if packet_length == 0:
            packet_length = len(self.data_raw)
        if mode == "PAR":
            return self.code_PAR(self.data_raw, packet_length)
        elif mode == "CRC":
            return self.code_CRC(self.data_raw, packet_length)
        return


# end class Sender
