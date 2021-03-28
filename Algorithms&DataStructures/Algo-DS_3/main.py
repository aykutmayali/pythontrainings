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

#find the difference between max and min elements in array

def differ(s1):
    maks = s1[0]
    min = s1[0]
    for i in s1:
        if i > maks:
            maks = i
        elif i <min:
            min = i

    return maks - min

if __name__ == '__main__':
    print(differ([1,3,6,9,8]))