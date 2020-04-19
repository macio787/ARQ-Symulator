import komm, random, numpy


def Generator(n):
    w = []
    for n in range(n):
        w.append(random.randint(0,1))
    return w

s = Generator(8)
print(s)

def CoderParityBit(signal, n):
    sum = 0
    i = 0
    counter = 1
    stop = len(signal) + round(len(signal)/n)
    while i < stop:
        sum = sum + signal[i]
        if (counter)%n==0:
            i = i + 1
            signal.insert(i, sum%2)
            sum=0
        counter = counter + 1
        i = i + 1
    return signal


print(CoderParityBit(s, 4))

