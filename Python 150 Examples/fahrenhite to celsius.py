print("Enter 'x' for exit")
fah = input("Enter the temperature in fahrenheit:")
if fah =='x':
    exit();
else:
    fahrenheit = float(fah)
    celsius = (fahrenheit-32)/1.8
    print("The value is:",celsius)
