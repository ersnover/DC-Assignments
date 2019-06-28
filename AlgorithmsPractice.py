
names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
intArray = [5,8,10,65,8,33,25,96]
strArray = ["to","the","window","to","the","wall","til","the","sweat","drips","down","my"]
missArray = [0,6,2,3,4,5,7,1,9]

#removes duplicate strings from an array
def RemoveDups(array):
    temp = []
    temp.append(array[0])
    for item in array:
        for i in temp:
            if i == item:
                break
        else:
            temp.append(item)
    return temp

#finds largest integer in array
def FindLargeInt(array):
    large = array[0]
    for i in array:
        if i > large:
            large = i
    return large

#finds largest string in array
def FindLargeStr(array):
    large = array[0]
    for i in array:
        if len(i) > len(large):
            large = i        
    return large

#finds smallest integer in array
def FindSmallInt(array):
    small = array[0]
    for i in array:
        if i < small:
            small = i
    return small

#finds smallest string in array
def FindSmallStr(array):
    small = array[0]
    for i in array:
        if len(i) < len(small):
            small = i            
    return small

#finds missing integer in list from 0-9
def FindMissInt(array):
    for i in range(10):
        for num in array:
            if i == num: 
                break
        else:
            print(f"{i} is missing.")
            return i
    else:
        print("They're all here!")

#Duplicates a given array
def ArrayDup(array):
    for i in range(len(array)):
        array.append(array[i])
    return array

            

print(RemoveDups(names))
print(FindLargeInt(intArray))
print(FindLargeStr(strArray))
print(FindSmallInt(intArray))
print(FindSmallStr(strArray))
FindMissInt(missArray)
print(ArrayDup(intArray))