class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap
    def hashFunction(self, mykey):
        return mykey % self.n

    def rehashFunction(self, hashkey):
        return (hashkey + 1) % self.n
        
    def insertData(self, student_obj):
        index = self.hashFunction(student_obj.getId())
        first_look_index = index
        while True:
            if self.hashtable[index] == None:
                self.hashtable[index] = student_obj
                print("Insert", student_obj.getId() ,"at index", index)
                break
            else:
                index = self.rehashFunction(index)
            
            if index == first_look_index:
                break
            
    def searchData(self, key):
        index = self.hashFunction(key)
        first_look_index = index
        while True:
            if self.hashtable[index] != None:
                if self.hashtable[index].getId() == key:
                    print("Found", key ,"at index", index)
                    return self.hashtable[index]
                else:
                    index = self.rehashFunction(index)
            else:
                print(key,"does not exist.")
                return None
            
            if index == first_look_index:
                print(key,"does not exist.")
                return None
            
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGpa(self):
        return self.gpa
    
    def printDetail(self):
        print("ID:", self.id, "\nName:", self.name, "\nGPA:", self.gpa)

#meow = ProbHash(20)
#print(list(meow.hashtable))

s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)
myHash = ProbHash(20)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)

std = myHash.searchData(65070077)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070032)