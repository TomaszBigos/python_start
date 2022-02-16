# Fahrenheit to Celsius
inp = input('The temperature in the Fahrenheit scale: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print("Temperature in the Celsius scale")
    print(cel)
except:
    print('Please provide a number')
