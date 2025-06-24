#BMI Calculator

# Constants for conversions
INCHES_IN_FOOT = 12
CM_PER_INCH = 2.54

def get_valid_weight():
    while True:
        try:
            weight_input=input(" ⚖️ Enter your weight in Kilograms: ")
            
            weight=float(weight_input)
            # print(weight)
            if (weight<=0):
                print(" ⚠️ Weight Should be greater than Zero.")
            else:
                break
        except ValueError:
          print(" ⚠️ Weight Must be a Number.")
    return weight

def get_valid_height():
    while True:
        #Inputing feet in terms of Feet
        feet_input=input(" 📏 Enter your height in feets: ")
        if feet_input.isdigit():
            feet=int(feet_input)
            if (feet<=0 or feet>9):
                print(" ⚠️ feet Should be greater than Zero and less than 9.")
            else:
                # print(feet)
                break

        else:
            print(" ⚠️ Feet Must be a Number.")

    while True:
        #Inputing feet in terms of Feet
        inch_input=input(" 📐 Enter your height in inches: ")
        if inch_input.isdigit():
            inches=int(inch_input)
            if (inches<0 or inches>11):
                print(" ⚠️ Inches Should be in 0 to 11 range .")
            else:
                # print(inches)
                break

        else:
            print(" ⚠️ Inch Must be a Number.")
    return feet,inches

def calc_bmi(weight,feet,inches):
    #conversions of height
    total_inches=(feet*INCHES_IN_FOOT)+inches
    Inches_To_CM=total_inches*CM_PER_INCH
    CM_To_Meter=Inches_To_CM/100

    height_meter=CM_To_Meter

    #calculating BMI
    bmi=weight/((height_meter)**2)
    print(f"📊 Your BMI Score is: 🧮 {bmi:.2f}")

    return bmi, height_meter

def get_bmi_category(bmi):   
    if(bmi<18.5):
        print(" 🦴 you are Underweight.")
    elif(18.5<=bmi<25):
        print(" ✅ You are Normal 👌.")
    elif(25<=bmi<30):
        print(" ⚠️ You are overweight. Consider regular exercise and a healthy diet.")
    elif(bmi>=30):
        print("🚨 You are Obese. Consider regular exercise and a healthy diet.")

def health_tip(bmi):
    if bmi < 18.5:
        print("💡 Tip: Consider eating nutrient-rich foods and consulting a doctor.")
    elif bmi >= 25:
        print("💡 Tip: Try adding regular walks or workouts to your routine.")


def suggest_weight_range(height_meter):
    min_weight = 18.5 * (height_meter ** 2)
    max_weight = 24.9 * (height_meter ** 2)
    print(f"📏 Ideal weight range: {min_weight:.2f} kg ➡️  {max_weight:.2f} kg.")

def ask_to_continue():
    while True:
        choice = input("🔁 Do you want to calculate BMI for another person? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("👋 Thank you for using the BMI Calculator. Stay healthy!")
            return False
        else:
            print("⚠️ Please enter yes or no.")



def main():
    print("👋 Welcome to the BMI(Body Mass Index) Calculator!\n")
    while True:
        weight = get_valid_weight()
        feet, inches = get_valid_height()
        bmi, height_meter = calc_bmi(weight, feet, inches)

        get_bmi_category(bmi)
        health_tip(bmi)
        suggest_weight_range(height_meter)

        if not ask_to_continue():
            break

main()