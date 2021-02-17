# Question 1:
# class Vehicle:
#     color = "white"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# class Bus(Vehicle):
#     pass
#
#
# class Car(Vehicle):
#     pass

# Question 2:
class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    # Question 3
    def displayinfo(self):
        print("name : ", self.name, "\n mileage: ", self.mileage, "\n Capacity:", self.capacity)


class Bus(Vehicle):
    def fare(self):
        fare = self.capacity * 100
        extra_fare = fare * 0.1
        return fare + extra_fare


# School_bus = Bus("School Volvo", 12, 50)
# # print("Total Bus fare is:", School_bus.fare())
# School_bus.displayinfo()

# Question 4:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def displayarea(self):
        area = self.length * self.width
        print("area of rectangle = ", area)


# length = float(input("enter length of rectangle =\n"))
# width = float(input("enter width of rectangle =\n"))
# rectangle = Rectangle(length, width)
# rectangle.displayarea()

# Question 5:
class String:
    def __init__(self, sentence):
        self.sentence = sentence

    def displayString(self):
        sentence = self.sentence.upper()
        print("string : ", self.sentence, "\n string uppercase: ", sentence)


# sentence = input('please enter your sentence:\n')
# obj = String(sentence)
# obj.displayString()

# Question 6:
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displaygender(self):
        pass


class Male(Person):
    def displaygender(self):
        print("name:", self.name, "\n gender:", "Male")


class Female(Person):
    def displaygender(self):
        print("name:", self.name, "\n gender:", "Female")


# person1 = Male("ahmed", 25, "Male")
# person2 = Female("aya", 20, "Female")
# person1.displaygender()
# print("\n")
# person2.displaygender()

# Question 7:
class ValidParenthese:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


print(ValidParenthese().is_valid_parenthese("(){}[]"))
print(ValidParenthese().is_valid_parenthese("()[{)}"))
print(ValidParenthese().is_valid_parenthese("({}({}{}))"))
