# Python3 program to swap elements 
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp
    return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print("List: ", List)
print("List after swaping", swapPositions(List, pos1 - 1, pos2 - 1))