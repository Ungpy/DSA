class DataNode:
    def __init__(self, input_name):
        self.name = input_name
        self.next = None


class SinglyLinkList:
    def __init__(self):
        self.count = 0
        self.head = None


    def traverse(self):
        if self.head == None:
            #empty list
            print("This is an empty list")
        else:
            pos = self.head
            while pos != None:
                print("->", pos.name, end="")
                pos = pos.next
            print("")
        return

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
        return
    def insertLast(self, data):#มั่ว1
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pos = self.head
            while pos.next != None:
                pos = pos.next
            pos.next = pNew
        return
    def insertBefore(self, targetnode, data):
        pNew = DataNode(data)
        if self.head == None:
            print("Cannot insert, <target node> does not exist")
        elif self.head.name == targetnode:
            pNew.next = self.head
        else:
            pos = self.head
            while pos.next != None:
                if pos.next.name == targetnode:
                    pNew.next = pos.next
                    pos.next = pNew
                    return
                pos = pos.next
            print("Cannot insert, <target node> does not exist")

    def delete(self, data):
        target_name = data
        if self.head == None: #ถ้า empty list
            print("Cannot delete, <data> does not exist, BC This is an empty list")
        elif self.head.name == target_name: #ถ้าอยู่ตัวแรก
            self.head = None
        else: #ถ้า empty list
            pos = self.head
            while pos.next != None:
                if pos.next.name == target_name:
                    del_target_node = pos.next
                    if pos.next.next != None: #ถ้ามีตัวให้เชื่อม
                        pos.next = pos.next.next
                    else:
                        pos.next = None
                    del del_target_node
                    return
                else:
                    pos = pos.next
            print("Cannot delete, <data> does not exist")
        return
       
mylist = SinglyLinkList()
pNew = DataNode("John")
mylist.head = pNew
print(mylist.head.name)
pNew = DataNode("Tony")
mylist.head.next = pNew
print(mylist.head.next.name)
pNew = DataNode("Bill")
mylist.head.next.next = pNew
mylist.traverse()
mylist.insertFront("Kim")
mylist.traverse()
mylist.insertLast("Pao")
mylist.traverse()
mylist.delete("John")
mylist.traverse()
mylist.insertBefore("Pao", "Meow")
mylist.traverse()
