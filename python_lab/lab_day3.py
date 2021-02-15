import math
from collections import Counter


# Question 1
# file = open("mockingjay.txt", "r")
# final_string = file.read().replace('\n', ' ')
# string_arr = final_string.split()
# counter = Counter(string_arr)
# most_common = counter.most_common(20)
# print(most_common)

# Question 2
# x1 = float(input('enter x for the first point:\n'))
# y1 = float(input('enter y for the first point:\n'))
# x2 = float(input('enter x for the second point:\n'))
# y2 = float(input('enter y for the second point:\n'))
# distance = (y2-y1)/(x2-x1)
# print(f'the distance between two point is = {distance}')

# Question 3
# class Vehicle:
#     pass

# Question 4
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage


# Question 5
# def revers_string(sentence):
#     words = sentence.split(' ')
#     reverse_sentence = ' '.join(reversed(words))
#     return reverse_sentence
#
#
# sentence = input('please enter your sentence:\n')
# print('revers sentence is :', revers_string(sentence))

# Question 6
class String:
    def __init__(self, sentence):
        self.sentence = sentence

    def displayString(self):
        sentence = self.sentence.split(' ')
        reverse_sentence = ' '.join(reversed(sentence))
        print("string : ", self.sentence, "\n reverse string: ", reverse_sentence)


# sentence = input('please enter your sentence:\n')
# obj = String(sentence)
# obj.displayString()


# Question 7
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def displayarea(self):
        area = math.pi * math.pow(self.radius, 2)
        print("circle radius : ", self.radius, "\n circle area: ", area)

    def displayperimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("circle radius : ", self.radius, "\n circle perimeter: ", perimeter)


radius = float(input('enter radius of circle:\n'))
obj = Circle(radius)
obj.displayarea()
obj.displayperimeter()
