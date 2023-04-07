def insertionSort(list, last):
    current = 1
    compare = 0
    while (current <= last):
        hold = list[current]
        walker = current - 1
        compare += 1 #นับล่วงหน้า
        while (walker >= 0 and hold < list[walker]):
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1
        list[walker+1] = hold
        current += 1
        if walker < 0:
            compare -= 1
        print(list)
    print(compare)

insertionSort([23,78,45,8,32,56],5)