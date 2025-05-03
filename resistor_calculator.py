# 4 & 5 band resistor calculator
bands = int(input("How many bands? (4 or 5): "))

#list of colours and their values for first 3 or 2 bands:
firstBands = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

nextBands = {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 10000,
    "green": 100000,
    "blue": 1000000,
    "violet": 10000000,
    "grey": 100000000,
    "white": 1000000000,
    "gold": 0.1,
    "silver": 0.01
}

toleranceBand = {
    "brown": 1,
    "red": 2,
    "green": 0.5,
    "blue": 0.25,
    "violet": 0.10,
    "grey": 0.05,
    "gold": 5,
    "silver": 10
}

if bands == 5:
    print("Calculating for 5 band resistors.")

    #find value of each band
    color1 = input("What colour is the first band? ")
    color2 = input("What colour is the second band? ")
    color3 = input("What colour is the third band? ")
    color4 = input("What colour is the fourth band? ")
    color5 = input("What colour is the fifth band? ")

    #find first 3 bands
    step1 = firstBands[color1]*100 + firstBands[color2]*10 + firstBands[color3]
    
    #find multiplier
    multiplier = nextBands[color4]

    #multiply by multiplier
    step2 = multiplier*step1

    #convert units
    if step2 >= 1000 and step2 <= 999999:
        step3 = f"{step2/1000} KΩ"
    elif step2 >= 1000000 and step2 <= 999999999:
        step3 = f"{step2/1000000} MΩ"
    elif step2 >= 1000000000 and step2 <= 999999999999:
        step3 = f"{step2/1000000000} GΩ"
    else:
        step3 = f"{step2} Ω"

    #find tolerance
    tolerance = toleranceBand[color5]

    #print output
    print(f"Your 5 band resistor is for {step3} with a tolerance of ±{tolerance}%")

elif bands == 4:
    print("Calculating for 4 band resistors.")

    #find value of each band
    color1 = input("What colour is the first band? ")
    color2 = input("What colour is the second band? ")
    color3 = input("What colour is the third band? ")
    color4 = input("What colour is the fourth band? ")


    #find first 3 bands
    step1 = firstBands[color1]*10 + firstBands[color2]
    
    #find multiplier
    multiplier = nextBands[color3]

    #multiply by multiplier
    step2 = multiplier*step1

    #convert units
    if step2 >= 1000 and step2 <= 999999:
        step3 = f"{step2/1000} Ohms"
    elif step2 >= 1000000 and step2 <= 999999999:
        step3 = f"{step2/1000000} Ohms"
    elif step2 >= 1000000000 and step2 <= 999999999999:
        step3 = f"{step2/1000000000} Ohms"
    else:
        step3 = f"{step2} Ohms"

    #find tolerance
    tolerance = toleranceBand[color4]

    #print output
    print(f"Your 4 band resistor is for {step3} with a tolerance of {tolerance}%")

else:
    print("No such resistor.")