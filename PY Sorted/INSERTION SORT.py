# def insertionSort(list, last):
#     cardToNum(list)
#     current = 1
#     compare = 0
#     while (current <= last):
#         hold = list[current]
#         walker = current - 1
#         compare += 1 #นับล่วงหน้า
#         while (walker >= 0 and hold < list[walker]):
#             list[walker+1] = list[walker]
#             walker -= 1
#             compare += 1
#         list[walker+1] = hold
#         current += 1
#         if walker < 0:
#             compare -= 1
#         print(list)
#     print(compare)

#insertionSort([23,78,45,8,32,56],5)


def insertionSort(list, last):
    originalList = list.copy() #<-------เพิ่มตรงนี้
    list = cardToNum(list) #<-------เพิ่มตรงนี้
    current = 1
    compare = 0
    while (current <= last):
        hold = list[current]
        hold2 = originalList[current] #<-------เพิ่มตรงนี้
        walker = current - 1
        compare += 1
        while (walker >= 0 and hold < list[walker]):
            list[walker+1] = list[walker]
            originalList[walker+1] = originalList[walker] #<-------เพิ่มตรงนี้
            walker -= 1
            compare += 1
        list[walker+1] = hold
        originalList[walker+1] = hold2 #<-------เพิ่มตรงนี้
        current += 1
        if walker < 0:
            compare -= 1
        print(originalList)
        # print(list)
        # print("----------------------------")
    print(compare)

def cardToNum(list):
    special = ["J", "Q", "K", "A"]
    sign = ["♣", "♦", "♥", "♠"]
    for i in range(len(list)):
        list[i] = list[i].replace(list[i][-1], str(sign.index(list[i][-1])))
        if(list[i][0] in special):
            list[i] = (str(11 + int(special.index(list[i][0]))) + list[i][1:])
        list[i] = int(list[i])
    print(list)
    return list

insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
