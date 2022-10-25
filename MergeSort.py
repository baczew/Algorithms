import math

list = [6, 35, 63, 6, 89, 0, 16, -987, 4666, 253, -6, -78]

def sort(lis):

    n = len(lis)
    result = []
    i = 0
    j = 0

    if n>1:

        a = lis[:math.floor(n/2)]
        b = lis[math.floor(n/2):]

        a = sort(a)
        b = sort(b)

        print("Before merge: a & b:", a, b)

        for h in range(0, n):

            if i==len(a):
                result.append(b[j])
                j+=1
                continue

            elif j==len(b):
                result.append(a[i])
                i+=1
                continue

            if a[i]>b[j]:
                result.append(b[j])
                j+=1

            else:
                result.append(a[i])
                i+=1

        return result

    elif n==1:

        return lis



print("Sorted:", sort(list))



