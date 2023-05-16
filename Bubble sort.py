## 01....
def BS(element):
    V = len(element)

    for i in range (V-1):
        flag = 0

        for j in range (V-1):

            if element[j] > element [j+1]:
                #swaping 
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                flag = 1 

        if flag ==0:
         break
    return element

Element = [22,6,9,33,3,7,1,5]

result = BS(Element)

print(result)


## 02.....

def bubblesort(element):
    s = len(element)

    for i in range(s-1):
        flag = 0

        for j in range(s-1):

            if element[j] > element[j+1]:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                flag = 1

        if flag == 0:
            break
    return element

ele = [12,45,7,2,8,3,5,17,47,1]

result = bubblesort(ele)

print(result)


#3
def Bubblesort(element):
    o = len(element)

    for i in range(o-1):
        flag = 0

        for j in range(o-1):
            if element[j] > element[j+1]:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp 
                flag = 1 

        if flag == 0 :
            break

    return element

ele = [22,45,78,98,1,24,56,100,2,0]

result = Bubblesort(ele)

print(result)

def bs(e):
    h  = len(e)

    for i in range(h-1):
        flag = 0

        for j in range(h-1):

            if e[j] > e[j+1]:
                t = e[j]
                e[j]= e[j+1]
                e[j+1] =t
                flag = 1

        if flag ==0:
         break
    return e 

e = [22,45,67,90,1,3,57,2,69]
r = bs(e)
print(r)


def bs (element):
    x = len(element)

    for i in range(x-1):
        flag = 0

        for j in range(x-1):
            if element[j] >element[j+1]:
                tem =element[j]
                element[j] = element[j+1]
                element[j+1] = tem
                flag = 1

        if flag ==0:
            break

    return element

EL=[23,45,76,78,1,8,7,4,37]

result = bs(EL)
print(result)

def bS(element):
    g = len(element)

    for i in range(g-1):
        flag = 0

        for j in range(g-1):
            if element[j] >element[j+1]:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                flag =1

        if flag ==0:
         break
    return element

ELE= [22,65,67,1,5,23,0,3]

result = bS(ELE)
print(result)
    