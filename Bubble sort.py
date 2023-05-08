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
