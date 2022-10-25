
def main():

    l = [145, 4, 6, 7, 95, 474, 5.6, 5.5, 7.5]

    position = BinarySearch(l, 5.5)

    if position >= 0:
        print(f"Value found at position {position + 1} of a sorted input array.")
    else:
        print("Value not found in the input array.")

def BinarySearch(input_list, searched_value):

    input_list = sort_list(input_list)

    if input_list:
        n = (len(input_list) - 1)//2 
    else:
        return float("-Inf")

    if input_list[n] == searched_value:
        cut = n
        
    elif input_list[n] > searched_value:
        cut = BinarySearch(input_list[:n], searched_value)
        
    else:
        cut = BinarySearch(input_list[(n+1):], searched_value)
        cut+=n+1
    
    return cut
    


def sort_list(input_list):

    n = len(input_list)
    result = []
    i = 0
    j = 0

    if n>1:

        a = input_list[:n//2]
        b = input_list[n//2:]

        a = sort_list(a)
        b = sort_list(b)

        for _ in range(0, n):

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

        return input_list


if __name__ == "__main__":
    main()

