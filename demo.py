def calculate_bmi(weight, height):
 
  if height  <= 0:
    return "Error: Height cannot be zero or negative."
  bmi = weight / (height * height)
  return bmi

def Bmi(bmi):
 
  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal weight"
  elif bmi <= 29.9:
    return "Overweight"
  else:
    return "Obese"

def main():
  
  while True:
    try:
      weight = float(input("Enter your weight in kilograms (kg): "))
      height = float(input("Enter your height in meters (m): "))
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")

  bmi = Bmi(weight, height)

  if isinstance(bmi, str):  # Check for error message
    print(bmi)
  else:
    print("Your BMI is:", round(bmi, 2))
    interpretation = Bmi(bmi)
    print("BMI Interpretation:", interpretation)

if __name__ == "__main__":
  main()
