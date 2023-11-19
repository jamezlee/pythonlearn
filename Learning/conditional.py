print("welcome to rollercoaster")
height =  int(input("what is your height "))
bill = 0
if height > 120:
    print("you can ride the rollercoater")
    age = int(input("What is your age"))
    if age < 12:
        bill = 5
        print(f"yout child are {bill}")
    elif age <=18:
        bill = 7
        print(f"yout Youth are {bill}")
    elif age >=45 and age <= 55:
        print("free")
    
else:
    print("sorry, you have to grow taller")