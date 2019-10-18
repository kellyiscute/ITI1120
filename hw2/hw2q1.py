def bmi(p, t):
    ## complete your work here ##
    r = p/t**2
    ## return something for now
    return r

def print_bmi_level(r):
    ## complete your work here ##
    if r < 18.5:
        print('underweight')
    elif r >= 18.5 and r < 25:
        print('normal weight')
    elif r >= 25 and r < 30:
        print('overweight')
    elif r >= 30:
        print('obese')
    return

p = float(input("Enter your weight in kilograms "))
t = float(input("Enter your height in meters "))

r = bmi(p,t)
print("Your BMI is", r)
print_bmi_level(r)
