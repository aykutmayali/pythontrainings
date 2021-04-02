# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def isAnagram(s1,s2):
    if(len(s1) != len(s2)):
        return False
    s1_dict={}
    s2_dict={}

    for char in s1:
        if char not in s1_dict.keys():
            s1_dict[char] =1
        else:
            s1_dict[char] +=1

    for char in s2:
        if char not in s2_dict.keys():
            s2_dict[char] =1
        else:
            s2_dict[char] +=1

    return s1_dict == s2_dict

def fizzBuzz(n):
    for i in range(1,n):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(isAnagram("aleyna", "naleya"))
    print(isAnagram("aleyna", "rubin"))

    n = int(input("n sayısını giriniz"))
    fizzBuzz(int(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
