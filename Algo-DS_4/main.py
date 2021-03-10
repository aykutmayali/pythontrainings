

def oddTot(s1):
    sum = 0
    for element in s1:
        if element % 2 == 1:
            sum += element

    return sum

if __name__ == '__main__':
    print(oddTot([1,2,3,4,5,6,7]))
