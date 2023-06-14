def random_name():
    import random
    import string

    num_instances = int(input("How many EC2 instances do you want names for? "))
    department_name = input("Input the name of your department ")
    letters = string.ascii_letters
    numbers = string.digits
    allow_departments = ["Marketing", "Accounting", "FinOps", "marketing", "accounting", "finops"]


    if department_name in allow_departments:
        for i in range(0, num_instances):
            print(department_name.capitalize() + '-' + ''.join(random.choice(letters+numbers) for i in range(10)))
    else:
        print("You are not allowed to use this name generator")