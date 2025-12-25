sonlar = [range(100)]

start = int(input("start: "))
stop = int(input("stop: "))

if start < len(sonlar) - 1 and stop < len(stop)-1 and -start < len(sonlar) and -stop < len(stop):
    print(sonlar[start:stop])
    