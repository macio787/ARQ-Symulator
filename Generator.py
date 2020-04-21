import random


class Generator:
    def __init__(self):
        print("generator initiated")
        return

    def generate(self, n):
        data = []
        for n in range(n):
            data.append(random.randint(0, 1))
        return data


# end class Generator
