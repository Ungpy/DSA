# def bubbleSort(list, last):
#     current = 0
#     compare = 0
#     sorted = False
#     while(current <= last and sorted == False):
#         walker = last
#         sorted = True
#         while(walker > current):
#             compare += 1
#             if list[walker] < list[walker - 1]:
#                 sorted = False
#                 (list[walker], list[walker - 1]) = (list[walker-1], list[walker])
#             walker -= 1
#         current += 1
#         print(list)
#     print(compare)
# bubbleSort([23,78,45,8,32,56],5)

def bubbleSort(list, last):
    originalList = list.copy() #<-------เพิ่มตรงนี้
    list = cardToNum(list) #<-------เพิ่มตรงนี้
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
                (originalList[walker], originalList[walker - 1]) = (originalList[walker-1], originalList[walker]) #<-------เพิ่มตรงนี้
            walker -= 1
        current += 1
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

bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)