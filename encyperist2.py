#Three Sum Problem Sample Problem: Given an array of integers, find all unique triplets in the array which give the sum of zero. The solution should return the list of triplets.

def find_triplets(arr):
    triplets = [] 
    n = len(arr)

   
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append([arr[i], arr[j], arr[k]])

    return triplets


arr = [0, -1, 2, -3, 1]
result = find_triplets(arr)
if not result:
    print("No triplets found with sum zero.")
else:
    for t in result:
        print(f"{t[0]}, {t[1]}, {t[2]}")