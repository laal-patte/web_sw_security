#This program shows an example of selection sort

#Selection sort iterates all the elements and if the smallest element in the list is found then that number
#is swapped with the first

def selectionSort(List):
    for i in range(len(List)-1):
        minimum = i
        for j in range( i + 1, len(list)-1):
            if(List[j] < List[minimum]):
                minimum = i
        if(minimum != i):
            List[j], List[minimum] = List[minimum], List[j]
    return List

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9, 3, 2, 5, 2, 8]
    print('Sorted List:',selectionSort(List))
