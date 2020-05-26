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
    redundancy = float

    def analize(self, mode, packet_length=0):
        if packet_length == 0:
            packet_length = len(self.sender.data_raw)

        corrupted_bits = 0
        redundant_bits = int
        if mode == "CRC":
            redundant_bits = 16
            if packet_length > 16:
                packet_length = 16
            # check only corrupted keys
            for i in range(len(self.receiver.key_crc_received)):
                if self.receiver.key_crc_received != self.receiver.key_crc_correct:
                    start_par_bits = i * packet_length
                    for j in range(packet_length):
                        curr_idx = start_par_bits + j
                        if self.receiver.data_received[curr_idx] != self.sender.data_raw[curr_idx]:
                            corrupted_bits += 1
            self.receiver.key_crc_received.clear()

        elif mode == "PAR":
            redundant_bits = 1

            corrupted_par_bits = 0
            par_counter = -1
            par_corrupt = False
            start_par_bits = len(self.sender.data_raw)

            for i in range(start_par_bits):
                if self.sender.data_send[i] != self.receiver.data_received[i]:
                    corrupted_bits += 1
                    if i % packet_length == 0:
                        print("parcounter++")
                        par_counter += 1
                        par_corrupt = False

                    if not par_corrupt:
                        curr_par_bit_idx = start_par_bits + par_counter
                        print("end is; " + str(len(self.receiver.data_received)))
                        if self.sender.data_send[curr_par_bit_idx] == self.receiver.data_received[curr_par_bit_idx]:
                            par_corrupt = True
                            corrupted_par_bits += 1

            # bit parzystosci nie pokazal bledu, a tak na prawde byl
            print("\nmismatched parity bits: " + str(corrupted_par_bits))

        self.ber = corrupted_bits / len(self.sender.data_raw)
        self.redundancy = redundant_bits * len(self.sender.data_raw) / packet_length

        print("Ber: ")
        print('{0:.7f}'.format(self.ber))
        print("\nTotal redundancy: ", self.redundancy)
# end class Analyzer