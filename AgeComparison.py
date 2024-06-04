message1 = 'The oldest by age is'

firstname_1 = input('please enter your firstname_1: ')
surname_1 = input('please enter your surname_1: ')
adress_1 = input('please enter your adress_1: ')
age_1 = int(input('please enter your age_1: '))

firstname_2 = input('please enter your firstname_2: ')
surname_2 = input('please enter your surname_2: ')
adress_2 = input('please enter your adress_2: ')
age_2 = int(input('please enter your age_2: '))

firstname_3 = input('please enter your firstname_3: ')
surname_3 = input('please enter your surname_3: ')
adress_3 = input('please enter your adress_3: ')
age_3 = int(input('please enter your age_3: '))

print()
print(message1)

if age_1 > age_2 and age_1 > age_3:
    print(firstname_1)
elif age_2 > age_3 and age_2 > age_1:
    print(firstname_2)
elif age_3 > age_1 and age_3 > age_2:
    print(firstname_3)

