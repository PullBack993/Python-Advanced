def flights(*args):
    result = [data for data in args]
    flgts = {}
    while True:
        if result[0] == 'Finish':
            return flgts
        if result[0] in flgts:
            destination = result.pop(0)
            flgts[destination] += int(result.pop(0))
        else:
            destination = result.pop(0)
            passengers = result.pop(0)
            flgts[destination] = passengers


# print(flights('Vienna', 256, 'Vienna',
#               26, 'Morocco', 98, 'Paris', 115,
#               'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))