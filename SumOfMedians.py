
def main():
    
    data = [0, 1.5, -0.1, 1, 100, 500]
    print(sum_of_medians_in_a_list(data))


def insert_into_heap(heap: list, add: float) -> list:
    '''Function built to add an element to an existing ordered list (heap), so that the new element follows the order. 
    It allows us not to sort the list every time we are requested to find the median value.'''

    new_heap = []

    if not heap:
        return [add]

    for i, val in enumerate(heap):

        if val > add:
            new_heap += [add] + heap[i:]
            break
        else:
            new_heap.append(val)

    else:
        new_heap.append(add)

    return new_heap



def sum_of_medians_in_a_list(input: list) -> float:
    '''Function built to calculate sum of medians of all the consective lists created by providing one additional 
    element of the input list at a time. First list is a slice of input(0, 1), next one input(0, 2), next input(0, 3) and so on.'''

    median_array = []
    result = []

    for val in (input):

        median_array = insert_into_heap(median_array, val)
        print(f"Array: {median_array}")

        median_array_length = len(median_array)

        median_index = median_array_length//2

        if median_array_length%2 == 0:
   
            median_index_slice = slice(median_index - 1, median_index + 1)

        else:

            median_index_slice = slice(median_index, median_index + 1)

        list_to_calculate_median = median_array[median_index_slice]
        sum_to_median = sum(list_to_calculate_median)
        len_to_median = len(list_to_calculate_median)
        
        median = sum_to_median/len_to_median
        
        result.append(median)
        print(f"Median of {median:0.2f} added")

    return sum(result)


if __name__ == "__main__":
    main()
