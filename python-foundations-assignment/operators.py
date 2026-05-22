# ============================================================
#   BASIC OPERATIONS & MATHEMATICAL OPERATORS
#   Solavise Tech Women in Data – Cohort 2
#   Author: Nancy Yeboah
#   Background: Biological Sciences → Data Analysis
# ============================================================

import math

print("=" * 55)
print("   SECTION 2: OPERATORS & MATHEMATICAL EXERCISES")
print("=" * 55)


# ------------------------------------------------------------
# EXERCISE 1: Simple Calculator
# ------------------------------------------------------------
print("\n📌 Exercise 1: Simple Calculator")
print("-" * 40)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2
division       = num1 / num2 if num2 != 0 else "undefined (can't divide by zero)"

print(f"\n  {num1} + {num2} = {addition}")
print(f"  {num1} - {num2} = {subtraction}")
print(f"  {num1} × {num2} = {multiplication}")
print(f"  {num1} ÷ {num2} = {division}")


# ------------------------------------------------------------
# EXERCISE 2: Area of Shapes
# ------------------------------------------------------------
print("\n📌 Exercise 2: Area of Shapes")
print("-" * 40)

# Circle — Formula: π × r²
radius = 7
circle_area = math.pi * radius ** 2
print(f"🔵 Circle (radius={radius}):              Area = {circle_area:.2f} sq units")

# Rectangle — Formula: length × width
length, width = 12, 5
rectangle_area = length * width
print(f"🟦 Rectangle ({length} × {width}):              Area = {rectangle_area} sq units")

# Triangle — Formula: ½ × base × height
base, height = 10, 8
triangle_area = 0.5 * base * height
print(f"🔺 Triangle (base={base}, height={height}):   Area = {triangle_area} sq units")


# ------------------------------------------------------------
# EXERCISE 3: Even or Odd
# ------------------------------------------------------------
print("\n📌 Exercise 3: Even or Odd Checker")
print("-" * 40)

number = int(input("Enter a number to check: "))

if number % 2 == 0:
    print(f"  {number} is EVEN ✅")
else:
    print(f"  {number} is ODD ✅")

# Bonus: show the modulus result
print(f"  ({number} % 2 = {number % 2}  — modulus operator at work!)")


# ------------------------------------------------------------
# EXERCISE 4: Student Grade Percentage
# ------------------------------------------------------------
print("\n📌 Exercise 4: Student Grade Percentage")
print("-" * 40)

student = "Nancy Yeboah"
marks_obtained = 87
total_marks = 100

percentage = (marks_obtained / total_marks) * 100

print(f"  Student:         {student}")
print(f"  Marks Obtained:  {marks_obtained} / {total_marks}")
print(f"  Percentage:      {percentage:.1f}%")

if percentage >= 80:
    print("  Remark:          🏆 Distinction!")
elif percentage >= 70:
    print("  Remark:          ⭐ Merit")
elif percentage >= 50:
    print("  Remark:          ✅ Pass")
else:
    print("  Remark:          📚 Needs Improvement")


# ------------------------------------------------------------
# EXERCISE 5: BMI Calculator
# ------------------------------------------------------------
print("\n📌 Exercise 5: BMI Calculator")
print("-" * 40)

# BMI Formula: weight (kg) / height (m)²
weight_kg = float(input("Enter weight in kg: "))
height_m  = float(input("Enter height in metres (e.g. 1.65): "))

bmi = weight_kg / (height_m ** 2)

print(f"\n  Weight: {weight_kg} kg")
print(f"  Height: {height_m} m")
print(f"  BMI:    {bmi:.2f}")

if bmi < 18.5:
    print("  Category: 🔵 Underweight")
elif bmi < 25:
    print("  Category: 🟢 Normal weight")
elif bmi < 30:
    print("  Category: 🟡 Overweight")
else:
    print("  Category: 🔴 Obese")

print("  (BMI is a general guide — always consult a healthcare professional)")


# ------------------------------------------------------------
# EXERCISE 6: Power & Modulus
# ------------------------------------------------------------
print("\n📌 Exercise 6: Power & Modulus Operators")
print("-" * 40)

base_num = 3
exp      = 4
mod_val  = 10

power_result  = base_num ** exp
modulus_result = mod_val % 3

print(f"  Power:   {base_num} ** {exp} = {power_result}  (3 multiplied by itself 4 times)")
print(f"  Modulus: {mod_val} %  3  = {modulus_result}   (remainder after dividing {mod_val} by 3)")

# Real-world use case
print("\n  💡 Real-world use: Modulus tells us if a number is divisible.")
for i in range(1, 11):
    tag = "✅ divisible by 3" if i % 3 == 0 else ""
    print(f"     {i} % 3 = {i % 3}  {tag}")

print("\n✅ Section 2 Complete!\n")
