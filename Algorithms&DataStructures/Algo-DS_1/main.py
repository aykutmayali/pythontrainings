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

array = [10.0,3,"Adam",5,36,52]

print(array[:-2]) # last 2 except
print(array[0:3]) # except 3. element
print('reverse array with -1', array[::-1]) # reverse it

# elements in array
a = [1,3,58,75,95,63]

for i in range(len(a)):
    print(a[i])
#-------------------
for i in a:
    print(i)


# linear search O(N)
array[2] = 87
print(" new array " , array)
max = array[0]
for num in array:
    if num > max:
        max = num
        print("max is ", max, " num is ", num)

#Reversing an array in-place overview

for i in range(len(array),0,-1):
    print(i)
#-------------------

def reverse(nums):
    #pointing to first item
    start_index = 0
    #pointing to last item
    end_index = len(nums)-1

    while end_index > start_index:
        nums[start_index],nums[end_index] = nums[end_index],nums[start_index]
        start_index = start_index+1
        end_index = end_index -1

if __name__== '__main__':
    n=[11,2,3,4,5]
    reverse(n)
    print(n)
