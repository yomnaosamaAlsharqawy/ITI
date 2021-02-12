import math

question = int(input('Enter number of question from 1 to 10 that you want it’s answer:\n'))
if question == 1:
    # Question 1:
    f_name = input('Enter your first name:\n')
    l_name = input('Enter your last name:\n')
    msg = f"Welcome {l_name} {f_name}"
    print(msg)
elif question == 2:
    # Question 2:
    num1 = input('Enter a number:\n')
    num2 = int(num1 * 2)
    num3 = int(num1 * 3)
    result = int(num1) + num2 + num3
    print(f'result of equation {num1} + {num2} + {num3} = {result}')
elif question == 3:
    # Question 3:
    doc_str = """
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example """
    print(doc_str)
elif question == 4:
    # Question 4:
    r = 6
    volume = (4 / 3) * math.pi * math.pow(r, 3)
    print(f'the volume of a sphere with radius 6 is {volume}')
elif question == 5:
    # Question 5:
    base = int(input('please enter base of the triangle:\n'))
    height = int(input('please enter height of the triangle:\n'))
    area = (base * height) / 2
    print(f'area of the triangle is: {area}')
elif question == 6:
    z = 1
    for i in range(9):
        if i < 5:
            for j in range(i + 1):
                print('*', end=" ")
        else:
            for j in range(i - z):
                print('*', end=" ")
            z = z + 2
        print('\n')

elif question == 7:
    option = int(
        input('enter 1 to reverse letter in one word or enter 2 to reverse sentence to be start from end to start:\n'))
    if option == 1:
        word = input('enter word: \n')
        reverse_word = ""
        length = len(word)
        for i in range(length - 1, -1, -1):
            reverse_word += word[i]
        print(reverse_word)
    else:
        string = input('enter a sentence:\n')
        words = string.split()
        words = list(reversed(words))
        print(" ".join(words))

elif question == 8:
    for i in range(0, 7):
        if i == 3 or i == 6:
            continue
        else:
            print(i, end=" ")

elif question == 9:
    arr = []
    count = int(input('how many term you want?\n'))
    for i in range(0, count):
        if i == 0 or i == 1:
            arr.append(i)
        else:
            arr.append(arr[i - 1] + arr[i - 2])
    print(f'Fibonacci series: {arr}')

else:
    string = input('enter your string:\n')
    numbers = sum(c.isdigit() for c in string)
    letters = sum(c.isalpha() for c in string)
    print(f'string have {numbers} of digits and {letters} of letters')


