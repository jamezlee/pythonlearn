#learning about list
import random
names_string = input()
names = names_string.split(', ')

states_of_America = ["Delaware", "Texas", "LA"]

num_item = len(names)
random_choice = random.randint(0, num_item-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay)