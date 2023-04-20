# def selectionSort(list, last):
#     """Sort the list"""
#     current = 0
#     compare = 0
#     while(current < last):
#         smallest = current
#         walker = current + 1
#         while(walker <= last):
#             compare += 1
#             if(list[walker] < list[smallest]):
#                 smallest = walker
#             walker += 1
#         list[current], list[smallest] = list[smallest], list[current]
#         current += 1
#         print(list)
#     print(compare)
# selectionSort([23,78,45,8,32,56],5)
# selectionSort([2,1,3,4,5,6],5)
# selectionSort([503,87,512,61,908,170,897,275,653,426,154,765,703],12)


def selectionSort(list, last):
    """Sort the list"""
    originalList = list.copy() #<-------เพิ่มตรงนี้
    list = cardToNum(list) #<-------เพิ่มตรงนี้
    current = 0
    compare = 0
    while(current < last):
        smallest = current
        walker = current + 1
        while(walker <= last):
            compare += 1
            if(list[walker] < list[smallest]):
                smallest = walker
            walker += 1
        list[current], list[smallest] = list[smallest], list[current]
        originalList[current], originalList[smallest] = originalList[smallest], originalList[current] #<-------เพิ่มตรงนี้
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

selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)