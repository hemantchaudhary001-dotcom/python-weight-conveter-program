# python weight converter

weight = float(input("enter your weight :"))
unit = input("enter your unit (kg or lb):").lower()
if unit == "kg":
    weight = weight * 2.205
    unit = "lbs."
    print(f"your weight is : {round(weight,1)} {unit}")33
elif unit =="lb":
    weight = weight / 2.205
    unit = "kg."
    print(f"your weight is : {round(weight,1)} {unit}")
else:
    print("invalid unit")
exit()


