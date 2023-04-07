def bubbleSort(list, last):
    current = 0
    compare = 0
    sorted = False
    while(current <= last and sorted == False):
        walker = last
        sorted = True
        while(walker > current):
            compare += 1
            if list[walker] < list[walker - 1]:
                sorted = False
                (list[walker], list[walker - 1]) = (list[walker-1], list[walker])
            walker -= 1
        current += 1
        print(list)
    print(compare)
bubbleSort([23,78,45,8,32,56],5)