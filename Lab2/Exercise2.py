def get_activity(temp):
    if temp >= 80:
        return 1
    elif temp >= 60 and temp < 80:
        return 2
    elif temp >= 40 and temp < 60:
        return 3
    elif temp < 40:
        return 4

temperature = input('Enter the temperature: ')
activity = get_activity(temperature)
if activity == 1:
    print('Swimming')
elif activity == 2:
    print('Soccer')
elif activity == 3:
    print('Volleyball')
else:
    print('Skying')
