# input
name = input("Please input your name: ")
weight = int(input("Please input your weight in kg: "))
height = float(input("please input your height in m: "))

#calculate Ponderal Index
def bmi(weight, height):
    bmi = weight / ( height * height)
    return bmi

#calculate bmi prime
def bmi_prime(bmi):
    bmi_prime = bmi / 25
    return bmi_prime

# classification num could be wether bmi or bmi prime
def classification(bmi):
    #determine classification
    if 0 < bmi < 16 or 0 < bmi < 0.64 :
        classification = "Severe Thinness"
    elif 16 <= bmi < 17 or 0.64 <= bmi < 0.68 :
        classification = "Moderate Thinness"
    elif 17 <= bmi < 18.5 or 0.68 <= bmi < 0.74 :
        classification = "Mild Thinness"
    elif 18.5 <= bmi < 25 or 0.74 <= bmi < 1 :
        classification = "Normal"
    elif 25 <= bmi < 30 or 1 <= bmi < 1.2 :
        classification = "Overweight"
    elif 30 <= bmi < 35 or 1.2 <= bmi < 1.4:
        classification = "Obese Class I"
    elif 35 <= bmi <= 40 or 1.4 <= bmi <= 1.6 :
        classification = "Obese Class II"
    elif 40 < bmi < 50 or 1.6 < bmi < 2:
        classification = "Obese Class III"
    else :
        classification = "Your data is invalid"
    return classification

# healthy range and weight report print
def health(name, height):
    weight_low = round(18.5 * (height * height))
    weight_high = round(25 * (height * height),2)
    print("Healthy BMI range: 18.5 kg/m2 - 25 kg/m2")
    print("Healthy weight for", name , "is", weight_low ," kg - " 
          , weight_high," kg")

print(name+"'s BMI report :")
print("Your BMI number is" , round(bmi(weight,height),2) , " kg/m^2")
print("Your BMI prime number is" ,round(bmi_prime(bmi(weight,height)), 2) , " kg/m^2")
print("Base on the number, you are BMI type is " + classification(bmi(weight,height)))
print("To be healthy:")
health(name, height)
