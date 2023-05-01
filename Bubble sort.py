#1
def bubble_sort(element):
    size=len(element) # need to know element size 

    # for k in range(2): 
    # for k in range(size-1):
    for k in range(size-1): 
            swapped = False          # save time
            for i in range(size-1-k): #size means index value and decrricing it n-1
                if element[i] > element[i+1]: # compare 
                    # swapini it..
                    tem = element[i]
                    element[i] =element[i+1]
                    element[i+1] = tem
                    swapped =True
            if not swapped :
                break


if __name__ == '__main__':
    element = [5,9,2,1,67,34,88,34]
    element = ['roy','bikrom','sporsho','pollobi']

bubble_sort(element)
print(element)

#2 

print()

def b_s(e):
    s=len(e)
    for i in range(s-1):
        swap=False
        for a in range(s-1-i):
            if e[a] > e[a+1]:
                t = e[a]
                e[a] = e[a+1]
                e[a+1] = t
                swap=True
        if not swap:
            break

if __name__ == '__main__':

    e=[6,4,1,65,8,9,3,5,23,2]
    b_s(e)
    print(e)

#3
print()

def b_s(e):
    s=len(e)

    for a in range(s-1):
        swap=False
        for i in range(s-1):
            if e[i] > e[i+1]:
                t = e[i]
                e[i] = e[i+1]
                e[i+1] =t
                swap=True
        if not swap:
            break


if __name__ == '__main__':
    e=[9,4,6,8,0,3,34,3,97,1,3,566,34,65,23,87,9,4,1,5]
    e=['e','t','i','a','j','z','x','b']
    b_s(e)
    print(e)