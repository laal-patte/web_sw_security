#This program shows an example of selection sort

#Selection sort iterates all the elements and if the smallest element in the list is found then that number
#is swapped with the first

def selectionSort(List):
    for i in range(len(List)-1):
        minimum = i
        for j in range( i + 1, len(List)):
            if(List[j] < List[minimum]):
                minimum = j
        if(minimum != i):
            List[i], List[minimum] = List[minimum], List[i]
    return List

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9, 3, 2, 5, 2, 8]
    print('Sorted List:',selectionSort(List))

#Solution:
    #line 9 -> len(list)-1 => len(List)-1
    #line 9 -> len(List)-1 => len(List)
    #line 11 -> i => j
    #line 13 -> j => i {both places}
