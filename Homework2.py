name = input("First name: ")
surname = input("Last name: ")
age = int(input("Age: "))
birth = int(input("Date of birth(Year): "))
info = [name,surname,age,birth]
for i in info:
    print(i)
if age < 18:
    print("You can't go out beacuse it's so dangerous!")
else:
    print("You can go out street.")