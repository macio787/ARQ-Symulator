import komm

class Transmitter:
    def __init__(self, prob):
        self.setCrossProb(prob)
        print("Transmitter initiated")
        return

    data_noised = []
    cross_prob = 0.5

    def setCrossProb(self, prob):
        if prob > 1 or prob < 0:
            raise ValueError("Probability have to be less than 1 and greater than 0")
        self.cross_prob = prob
        print("\nCrossover probability set to: ", prob, "\n")
        return

    def simulateNoise(self, data_sent):
        bsc = komm.BinarySymmetricChannel(self.cross_prob)
        data_nsd = bsc(data_sent)
        self.data_noised = data_nsd
        return


# end class Transmitter
