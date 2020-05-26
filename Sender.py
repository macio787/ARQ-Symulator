import crc16, numpy


class Sender:
    class Coder:
        def __init__(self):
            print("coder initiated")
            return

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

        def code_CRC(self, _sender, n):
            if n > 16:
                n = 16
            # separate packets and generate key for each
            tmp_arr = []
            for i in range(0, len(_sender.data_raw)):
                tmp_arr.append(_sender.data_raw[i])
                if i % n == (n - 1):
                    _sender.key_crc.append(crc16.crc16xmodem(
                        self.arrayToBytes(tmp_arr)))
                    tmp_arr.clear()

            _sender.data_send = _sender.data_raw
            return _sender.data_send

        def arrayToBytes(self, data):
            tmp = ''
            for i in range(len(data)):
                tmp += str(data[i])
            tmp = bytes(tmp, 'utf-8')
            return tmp

    # end class Coder

    data_raw = []
    data_send = []
    key_crc = []
    coder = Coder()

    def code(self, mode, packet_length=0):
        if packet_length == 0:
            packet_length = len(self.data_raw)
        if mode == "PAR":
            return self.coder.code_PAR(self.data_raw, packet_length)
        elif mode == "CRC":
            return self.coder.code_CRC(self, packet_length)
        return


# end class Sender
