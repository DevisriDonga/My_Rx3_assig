""" Given an array of Red Green Blue balls.You have to sort it. 
Constraint : Time complexity O(n) 
Constraint : Space complexity O(1) 
Example: 
Input: [R, G, B, G, G, R, B, B, G] 
Output : [B,B,B,G,G,G,G,R, R] """

def sort_balls(arr):
    l , m, h = 0, 0, len(arr)-1
    while m <= h:
        if arr[m] == "B":
            arr[l],arr[m] = arr[m], arr[l]
            l +=1 
            m += 1 
        elif arr[m] == "G":
            m += 1 
        else :
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1 
    return arr
Input= ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
output= sort_balls(Input)
print(output)