# maximum in a list
def max(list):
    max = list[0] #initialise 1st element as max
    for x in list:
        if x > max:
            max = x
    return max
# minimum in list 
def min(list):
    min = list[0] #initialise first element as min
    for x in list:
        min = x
    return min
#main
list = [5,3,8,1,0,4]
range = max(list) - min(list)
print("Range of the list is ",range)