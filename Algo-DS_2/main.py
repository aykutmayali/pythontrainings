# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# string tersleme (reverse string)
def tersle(s1):
    return s1[::-1]

def reverseString(s1):
    reverse = ""
    for char in s1:
        reverse = char + reverse
    return reverse

def tersle2(s1):
    for idx in range(len(s1)-1,-1,-1):
        print(s1[idx], end="")


if __name__ == '__main__':
    print(tersle("voila"))
    print(reverseString("ronaldo"))
    tersle2("nicola")