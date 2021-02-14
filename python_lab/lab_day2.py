from random import randint

question = int(input('Enter number of question from 1 to 5 that you want it’s answer:\n'))
if question == 1:
    list1 = [1, 2.6, 3.3, 4.1, 5.8]
    list2 = []
    for i in list1:
        list2.append(int(i))
    print(list2)
elif question == 2:
    string1 = input('enter your first string:\n')
    string2 = input('enter your second string:\n')
    a_front = ''
    a_back = ''
    b_front = ''
    b_back = ''
    half_string1 = int(len(string1) / 2)
    for i in range(0, half_string1):
        a_front += string1[i]
    for i in range(half_string1, len(string1)):
        a_back += string1[i]

    half_string2 = int(len(string2) / 2)
    for i in range(0, half_string2):
        b_front += string2[i]
    for i in range(half_string2, len(string2)):
        b_back += string2[i]
    print(f'final string is: {(a_front + b_front) + " " + (a_back + b_back)}')

elif question == 3:
    def list_check(list):
        flag = 0
        for i in range(len(list)):
            for j in range(len(list)):
                if i != j:
                    if list[i] == list[j]:
                        flag = 1
        if not flag:
            print(f'List: {list} contains all unique elements')
        else:
            print(f'List: {list} contains does not contains all unique elements')


    list = [1, 3, 3, 5, 2, 9]
    # list = []
    # for i in range(0, 10):
    #     list.append(randint(0, 10))
    list_check(list)

elif question == 4:
    def BubbleSort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'sorted array is: {arr}')

    # list = []
    # for i in range(0, 10):
    #     list.append(randint(0,50))
    list = [64, 34, 25, 12, 22, 11, 1, 90]

    BubbleSort(list)

else:
    count = 0
    arr = []
    while True:
        if count < 5:
            user_num = int(input('enter number from 0 to 100 \n'))
            number = randint(0, 100)
            if user_num in arr:
                print('you already used this number before please try another one')
            elif user_num > 100:
                print('please enter number less than or equal 100')
            elif user_num > number:
                arr.append(user_num)
                count += 1
                print('your number is greater than the random number')
            elif user_num < number:
                arr.append(user_num)
                count += 1
                print('your number is less than the random number')
            elif user_num == number:
                arr.append(user_num)
                count += 1
                print('congratulations')
        else:
            option = input('your tries is finished enter yes to play again or no to finish playing\n')
            if option == 'yes':
                count = 0
                arr = []
            else:
                break
