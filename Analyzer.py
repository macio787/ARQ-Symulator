from Sender import Sender
from Receiver import Receiver
import time


class Analyzer:
    def __init__(self, _sender, _receiver):
        print("Analyzer initiated")
        self.sender = _sender
        self.receiver = _receiver
        return

    sender = Sender
    receiver = Receiver
    ber = float

    def analize(self, mode, packet_length=0):
        start = int(round(time.time() * 1000000000.0))
        if packet_length == 0:
            packet_length = len(self.sender.data_raw)

        corrupted = 0
        redundant_bits = int
        if mode == "CRC":
            redundant_bits = 16
            if packet_length > 16:
                packet_length = 16
            # check only corrupted keys
            for i in range(len(self.receiver.key_crc_received)):
                if self.receiver.key_crc_received != self.receiver.key_crc_correct:
                    start_idx = i * packet_length
                    for j in range(packet_length):
                        curr_idx = start_idx + j
                        if self.receiver.data_received[curr_idx] != self.sender.data_raw[curr_idx]:
                            corrupted += 1

        elif mode == "PAR":
            redundant_bits = 1
            i_received = -1
            for i_raw in range(len(self.sender.data_raw)):
                if i_raw % packet_length == 0:
                    i_received = i_received + 1
                if self.sender.data_raw[i_raw] != self.receiver.data_received[i_received]:
                    corrupted += 1
                i_received += 1

        self.ber = corrupted / len(self.sender.data_raw)
        total_redundancy = redundant_bits * len(self.sender.data_raw) / packet_length
        end = int(round(time.time() * 1000000000.0))

        print("Ber: ", self.ber, "\nTotal redundancy: ", total_redundancy)
        print("analizing time: ", (end-start)/1000000.0 ," ms")
# end class Analyzer
