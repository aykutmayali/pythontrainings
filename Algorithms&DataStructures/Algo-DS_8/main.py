# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# find repeated charecters in word
def repeated_char(w1):
    w1_dict = {}
    repeatings = []

    for chars in w1:
        if chars not in w1_dict:
            w1_dict[chars] = 1
        else:
            w1_dict[chars] += 1

    for keys, values in w1_dict.items():
        if values > 1:
            repeatings.append(keys)

    return repeatings

def most_repeated(w1):
    w1_dict = {}
    max = 0
    result = ""

    for char in w1:
        if char not in w1_dict.keys():
            w1_dict[char] = 1
        else:
            w1_dict[char] += 1

    for key, val in w1_dict.items():
        if val> max:
            max = val
            result = key

    return  result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(repeated_char('balaban'))
    print(most_repeated('balaban'))