import re
"""This program checks if the license plate number matches the category template """

def check(num):
    match = re.fullmatch(r'([A-Za-z]){2}\s(\d){4}\s([A-Za-z]){2}', num)
    if match:
        print("regular car")
    elif not match:
        match = re.fullmatch(r'([A-Za-z]){4}\s(\d){4}', num)
        if match:
            print('motorcycle')
        elif not match:
            match = re.fullmatch(r'([A-Za-z]){2}\s(\d){3}\s(\d){3}', num)
            if match:
                print('Diplomats, consuls, international organizations')
            elif not match:
                match = re.fullmatch(r'(\d){2}\s(\d){2}\s[A-Za-z]\d', num)
                if match:
                    print('AFU')
                else:
                    print('Does not exist')


car_number = input(str("Введіть номер авто: "))
check(car_number)
