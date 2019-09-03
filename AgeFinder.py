
age = eval(input('Enter Age : '))

if age == 5:
    print("Go To Kindergaten")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go To Grade {}".format(grade))

elif age < 5:
    print("Too Young For School")
    
else:
    print("Go To Collage")
