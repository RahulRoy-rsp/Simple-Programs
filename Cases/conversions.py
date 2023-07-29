case = int(input('''
Please enter a number for which you want the conversion:
1: Mass
2: Speed
3: Temperature
--> '''))

if case == 1:
    massInfo = int(input('''
        Please enter a number for which you want the Mass conversion:
        1: Kilograms(kg) to Gram(g)
        2: Gram(g) to Kilograms(kg) 
        3: Tonne to Kilograms(kg)
        4: Kilograms(kg) to Tonne
        --> '''))
    
    if massInfo == 1:
        kg = float(input("Enter a mass in kg: "))
        print(f"{kg} kg = {kg *1000} g")
        
    elif massInfo == 2:
        g = float(input("Enter a mass in g: "))
        print(f"{g} g = {g/1000} kg")
    elif massInfo == 3:
        t = float(input("Enter a mass in T: "))
        print(f"{t} T = {t * 1000} kg")    
    elif massInfo == 4:
        kg = float(input("Enter a mass in kg: "))
        print(f"{kg} kg = {kg/1000} T")
    else:
        print("Invalid input")
        
elif case == 2:
    speedInfo = int(input('''
        Please enter a number for which you want the Speed conversion:
        1: Kilometers per hour(kmph) to Miles per hour(mph)
        2: Kilometers per hour(kmph) to Meters per hour(mps) 
        3: Miles per hour(mph) to Kilometers per hour(kmph)
        --> '''))
        
    if speedInfo == 1:
        kmph = float(input("Enter speed in kmph: "))
        print(f"{kmph} kmph = {kmph/1.609} mph")
    elif speedInfo == 2:
        kmph = float(input("Enter speed in kmph: "))
        print(f"{kmph} kmph = {kmph/3.6} mps")
    elif speedInfo == 3:
        mph = float(input("Enter speed in mph: "))
        print(f"{mph} mph = {mph * 1.609} kmph")    
    else:
        print("Invalid input")


elif case == 3:
    tempInfo = int(input('''
        Please enter a number for which you want the Speed conversion:
        1: Degree Celcius to Farenheit
        2: Degree Celcius to Kelvin 
        3: Farenheit to Degree Celcius
        --> '''))
        
    if tempInfo == 1:
        cel = float(input("Enter Temperature: "))
        print(f"{cel} Degree Celcius = {(cel*9/5) + 32} Farenheit")
    elif tempInfo == 2:
        cel = float(input("Enter Temperature: "))
        print(f"{cel} Degree Celcius = {cel + 273.15} Kelvin")
    elif tempInfo == 3:
        far = float(input("Enter Temperature: "))
        print(f"{far} Farenheit = {(far-32)* 5/9} Degree Celcius")    
    else:
        print("Invalid input")

else:
    print("Invalid Input")
