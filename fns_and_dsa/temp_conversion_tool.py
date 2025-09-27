FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5
while True:
    def convert_to_celsius(fahrenheit):    
        temperature_in_celsious = (temperature -32) * FAHRENHEIT_TO_CELSIUS_FACTOR        
        print("temperature_in_celsius:" + str(temperature_in_celsious)+"F")
        return temperature_in_celsious
    
    def convert_to_fahrenheit(celsius):
            temperature_in_fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32       
            print("temperature_in_fahrenheit:" + str(temperature_in_fahrenheit)+"F")
            return temperature_in_fahrenheit
    

    temperature =int(input("Enter the temperature to convert: "))
    CorF = str(input('Is this temperature in Celsius or Fahrenheit? (C/F): '))
    if CorF == "F":
        convert_to_celsius(CorF)
        break
        
    elif CorF == "C":
        convert_to_fahrenheit(CorF)
        break
    else:
        print("You did not enter neither C nor F")