# ============================================================
#   DATA TYPES EXERCISES
#   Solavise Tech Women in Data – Cohort 2
#   Author: Nancy Yeboah
#   Background: Biological Sciences → Data Analysis
# ============================================================

print("=" * 55)
print("   SECTION 1: DATA TYPES EXERCISES")
print("=" * 55)


# ------------------------------------------------------------
# EXERCISE 1: Personal Bio Generator
# ------------------------------------------------------------
print("\n📌 Exercise 1: Personal Bio Generator")
print("-" * 40)

name = "Nancy Yeboah"
age = 24
height = 5.6               # in feet
favorite_tech_field = "Data Analysis"
is_student = True

print(f"Hi! My name is {name}.")
print(f"I am {age} years old and {height} feet tall.")
print(f"My favourite tech field is {favorite_tech_field}.")
print(f"Currently a student: {is_student}")
print(f"\nFull intro: My name is {name}, I am {age} years old, "
      f"{height}ft tall, and I am passionate about {favorite_tech_field}. "
      f"Student status: {is_student}.")


# ------------------------------------------------------------
# EXERCISE 2: Type Checker
# ------------------------------------------------------------
print("\n📌 Exercise 2: Type Checker")
print("-" * 40)

sample_name = "Nancy"                    # String
sample_age = 24                          # Integer
sample_height = 5.6                      # Float
sample_is_student = True                 # Boolean
sample_scores = [85, 90, 78, 92, 88]    # List

print(f"'{sample_name}'       → Type: {type(sample_name)}")
print(f"{sample_age}              → Type: {type(sample_age)}")
print(f"{sample_height}            → Type: {type(sample_height)}")
print(f"{sample_is_student}          → Type: {type(sample_is_student)}")
print(f"{sample_scores} → Type: {type(sample_scores)}")


# ------------------------------------------------------------
# EXERCISE 3: Data Conversion
# ------------------------------------------------------------
print("\n📌 Exercise 3: Data Conversion")
print("-" * 40)

# Integer to String
student_id = 20240015
student_id_str = str(student_id)
print(f"Integer {student_id} → String: '{student_id_str}' | Type: {type(student_id_str)}")

# Float to Integer (drops the decimal — no rounding!)
gpa = 3.87
gpa_int = int(gpa)
print(f"Float {gpa} → Integer: {gpa_int} | Type: {type(gpa_int)}")

# String number to Integer
str_score = "95"
int_score = int(str_score)
print(f"String '{str_score}' → Integer: {int_score} | Type: {type(int_score)}")


# ------------------------------------------------------------
# EXERCISE 4: User Information
# ------------------------------------------------------------
print("\n📌 Exercise 4: User Information")
print("-" * 40)

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_country = input("Enter your country: ")

print(f"\n👋 Hello {user_name}! You are {user_age} years old and you're from {user_country}.")
print(f"Welcome to the world of data, {user_name}! 🚀")


# ------------------------------------------------------------
# EXERCISE 5: Temperature Converter (Celsius → Fahrenheit)
# ------------------------------------------------------------
print("\n📌 Exercise 5: Temperature Converter")
print("-" * 40)

# Formula: F = (C × 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"\n🌡️  {celsius}°C = {fahrenheit:.2f}°F")

# Bonus: real-world context
if celsius < 0:
    print("❄️  Freezing cold! Wrap up warm.")
elif celsius < 20:
    print("🧥 Cool weather. A light jacket would help.")
elif celsius < 30:
    print("☀️  Comfortable and warm.")
else:
    print("🔥 Very hot! Stay hydrated.")

print("\n✅ Section 1 Complete!\n")
