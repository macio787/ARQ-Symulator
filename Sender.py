

class Sender:
    class Coder:
        def __init__(self):
            print("coder initiated")
            return

        def code_PAR(self, data):
            data_snd = data.copy()
            n = len(data_snd)
            sum = 0
            i = 0
            counter = 1
            stop = len(data_snd) + len(data_snd) / n
            while i < stop:
                sum = sum + data_snd[i]
                if (counter) % n == 0:
                    i = i + 1
                    data_snd.insert(i, sum % 2)
                    sum = 0
                counter = counter + 1
                i = i + 1
            return data_snd

        def code_CRC(self, data):
            # TODO::sprawdzic czy ma jakos byc zakodowane
            # n = len(data)
            data_snd = data.copy()
            return data_snd

    # end class Coder

    data_raw = []
    data_send = []
    coder = Coder()

    def code(self, mode):
        if mode == "PAR":
            print("\t->coding mode: PARITY BIT")
            return self.coder.code_PAR(self.data_raw)
        elif mode == "CRC":
            print("\t->coding mode: CRC")
            return self.coder.code_CRC(self.data_raw)
        return


# end class Sender
