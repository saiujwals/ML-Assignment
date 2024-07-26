def Pair(list, size, key): #function to check if pair of elements having sum as 10
    count = 0 #holds count of no. of pairs 
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (list[i] + list[j] == key): 
                count = count + 1
    return count
List = [2,7,4,1,3,6]
search_key = 10 #search element
size = len(List)
total_count =  Pair(List, size, search_key)
#total count of pairs
print("The no. of pairs with sum 10 are ", total_count)