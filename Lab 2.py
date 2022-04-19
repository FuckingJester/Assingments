# Task 1
# function map()
# .split() to make a gap
"""a, b, c, d, e = map(int,input("Введіть ціле число:\n").split())
# find maximum value using max()
M = max(a, b, c, d, e)
print(M)
# Task 2
# int use to convert string in integer
age_a = int(input("Введіть вік Антона:\n"))
age_b = int(input("Введіть вік Бориса:\n"))
age_v = int(input("Введіть вік Віктора:\n"))
# create the list to save all inputs
all_age = [age_a, age_b, age_v]
# write all possible conditions
if age_a > age_b and age_a > age_v:
    print("Антон найстарший")
elif age_a == age_b and age_a > age_v:
    print("Антон и Борис старше Віктора ")
elif age_a == age_v and age_a > age_b:
    print("Антон и Віктор старше Бориса ")
elif age_v == age_b and age_a > age_a:
    print("Віктор и Борис старше Антона ")
elif age_b > age_a and age_b > age_v:
    print("Борис найстарший ")
elif age_v > age_b and age_v > age_a:
    print("Віктор найстарший")
elif age_a == age_b == age_v:
    print("Всі хлопці одного віку")
# Task 3
# the same actions like in 1 task
a, b, c, = map(int,input("Введіть три числа :\n").split())
# all possible conditions as well as in 2 Task
if a == b == c:
    print("Всі числа однакові")
elif a == b or a == c or c == b:
    print("Два числа однакові")
elif a != b != c:
    print("Немає однакових чисел")
# Task 4
kind_of_year = int(input("Введіть номер місяця\n"))
if kind_of_year == 12 and 1 and 2:
    print("Зима")
elif kind_of_year == 3 and 4 and 5:
    print("Весна")
elif kind_of_year == 6 and 7 and 8:
    print("Літо")
elif kind_of_year == 9 and 10 and 11:
    print("Осінь")
else:
    print("Невірний номер місяця")"""