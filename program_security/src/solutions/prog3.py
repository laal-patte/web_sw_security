#This program is an example for sequential search

def sequentialSearch(target, List):
    '''This function returns the position of the target if found else returns -1'''
    position = 0
    global iterations
    iterations = 0
    while position < len(List):
        iterations += 1
        if target == List[position]:
            return position
        position += 1
    return -1

if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 3
    ans = sequentialSearch(target, List)
    if ans != -1:
        print('Target',target,'found at position:',ans,'in',iterations,'iterations')
    else:
        print('Target',target,'not found in the list')

    target = 9
    ans = sequentialSearch(target, List)
    if ans != -1:
        print('Target',target,'found at position:',ans,'in',iterations,'iterations')
    else:
        print('Target',target,'not found in the list')

#solution:
#line 5+ -> insert `global iterations`
#line 7 -> {len(List)+1} -> {len(List)}
#line 18&25 -> {ans == -1} -> {ans != -1}
