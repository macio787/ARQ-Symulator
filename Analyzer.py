

class Analyzer:
    def __init__(self):
        print("Analyzer initiated")
        return
    # TODO::

    data_raw = []
    data_received = []

    def setRaw(self, data):
        self.data_raw = data

    def setReceived(self, data):
        self.data_received = data

    def analize(self, mode, packet_length=0):
        if packet_length == 0: packet_length = len(self.data_raw)
        print("analize starting...")
        if mode == 'PAR': redundant_bits = 1
        if mode == 'CRC': return # TODO::
        i_received=-1
        bad=0
        for i_raw in range(len(self.data_raw)):
            if i_raw % packet_length ==0: i_received = i_received + 1
            if self.data_raw[i_raw] != self.data_received[i_received]: bad = bad + 1
            i_received = i_received + 1
        ber = bad / len(self.data_raw)
        total_redundancy = redundant_bits * len(self.data_raw) / packet_length
        print("Ber: ", ber, "\nTotal redundancy: ", total_redundancy)
# end class Analyzer