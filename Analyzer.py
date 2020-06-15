from Sender import Sender
from Receiver import Receiver
import numpy


class Analyzer:
    def __init__(self, _sender, _receiver):
        print("Analyzer initiated")
        self.sender = _sender
        self.receiver = _receiver
        return

    sender = Sender
    receiver = Receiver
    ber = float
    redundancy = float

    def analize(self, mode, packet_length=0):
        if packet_length == 0:
            packet_length = len(self.sender.data_raw)

        redundant_bits = 0

        if mode == "CRC":
            if packet_length > 16:
                packet_length = 16
            corrupted_crc_bits = 0
            # check only corrupted keys
            start_crc_bits = len(self.sender.data_raw)
            end_crc_bits = len(self.receiver.data_received)
            redundant_bits = len(self.receiver.data_received) - start_crc_bits

            # 1
            for i in range(start_crc_bits, end_crc_bits):
                if self.receiver.data_received[i] != self.sender.data_send[i]:
                    corrupted_crc_bits += 1
            self.receiver.key_crc_received.clear()
            self.ber = corrupted_crc_bits / redundant_bits

        elif mode == "PAR":

            corrupted_par_bits = 0
            start_par_bits = len(self.sender.data_raw)
            end_part_bits = len(self.receiver.data_received)
            redundant_bits = end_part_bits - start_par_bits

            # 1
            for i in range(start_par_bits, end_part_bits):
                if self.sender.data_send[i] != self.receiver.data_received[i]:
                    corrupted_par_bits += 1

            self.ber = corrupted_par_bits / redundant_bits

        self.redundancy = redundant_bits
# end class Analyzer
