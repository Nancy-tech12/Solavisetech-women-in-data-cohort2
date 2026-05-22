# ============================================================
#   CONTROL FLOW EXERCISES
#   Solavise Tech Women in Data – Cohort 2
#   Author: Nancy Yeboah
#   Background: Biological Sciences → Data Analysis
# ============================================================

import random
import time

print("=" * 55)
print("   SECTION 3: CONTROL FLOW EXERCISES")
print("=" * 55)


# ------------------------------------------------------------
# EXERCISE 1: Age Eligibility Checker
# ------------------------------------------------------------
print("\n📌 Exercise 1: Age Eligibility Checker")
print("-" * 40)

age = int(input("Enter your age: "))

if age < 0:
    print("  ❌ Invalid age entered.")
elif age < 13:
    print(f"  🧒 Age {age}: You are a CHILD.")
elif age < 18:
    print(f"  🧑 Age {age}: You are a TEENAGER.")
elif age < 65:
    print(f"  🙋 Age {age}: You are an ADULT.")
else:
    print(f"  👴 Age {age}: You are a SENIOR CITIZEN.")


# ------------------------------------------------------------
# EXERCISE 2: Password Validator
# ------------------------------------------------------------
print("\n📌 Exercise 2: Password Strength Checker")
print("-" * 40)

password = input("Enter a password to check: ")
length = len(password)

print(f"\n  Password length: {length} characters")

if length < 6:
    print("  🔴 Strength: WEAK — Too short. Use at least 6 characters.")
elif length < 10:
    print("  🟡 Strength: MODERATE — Consider using 10+ characters.")
elif length < 14:
    print("  🟢 Strength: STRONG — Good password!")
else:
    print("  🏆 Strength: VERY STRONG — Excellent password!")


# ------------------------------------------------------------
# EXERCISE 3: Grade Classification
# ------------------------------------------------------------
print("\n📌 Exercise 3: Grade Classification")
print("-" * 40)

score = float(input("Enter student score (0–100): "))

if score < 0 or score > 100:
    print("  ❌ Invalid score. Please enter a value between 0 and 100.")
elif score >= 80:
    grade = "A"
    remark = "Distinction 🏆"
elif score >= 70:
    grade = "B"
    remark = "Merit ⭐"
elif score >= 60:
    grade = "C"
    remark = "Credit 👍"
elif score >= 50:
    grade = "D"
    remark = "Pass ✅"
else:
    grade = "F"
    remark = "Fail — Keep pushing! 💪"

print(f"  Score: {score}  →  Grade: {grade}  →  {remark}")


# ------------------------------------------------------------
# EXERCISE 4: Multiplication Table
# ------------------------------------------------------------
print("\n📌 Exercise 4: Multiplication Table")
print("-" * 40)

num = int(input("Enter a number for its multiplication table: "))
print(f"\n  Multiplication Table for {num}:")
print(f"  {'─' * 25}")

for i in range(1, 11):
    result = num * i
    print(f"  {num} × {i:2d} = {result:4d}")


# ------------------------------------------------------------
# EXERCISE 5: Number Guessing Game
# ------------------------------------------------------------
print("\n📌 Exercise 5: Number Guessing Game")
print("-" * 40)

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

print(f"  🎮 I'm thinking of a number between 1 and 20.")
print(f"  You have {max_attempts} attempts. Good luck!\n")

while attempts < max_attempts:
    guess = int(input(f"  Attempt {attempts + 1}/{max_attempts} — Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("  📉 Too low! Try higher.")
    elif guess > secret_number:
        print("  📈 Too high! Try lower.")
    else:
        print(f"\n  🎉 Correct! The number was {secret_number}.")
        print(f"  You got it in {attempts} attempt(s)!")
        break
else:
    print(f"\n  😅 Game over! The number was {secret_number}. Better luck next time!")


# ------------------------------------------------------------
# EXERCISE 6: Countdown Timer
# ------------------------------------------------------------
print("\n📌 Exercise 6: Countdown Timer")
print("-" * 40)

print("  🚀 Launching countdown...\n")

for count in range(10, 0, -1):
    print(f"  {count}...")

print("  🎉 BLAST OFF!\n")


# ------------------------------------------------------------
# EXERCISE 7: ATM Withdrawal Simulation
# ------------------------------------------------------------
print("\n📌 Exercise 7: ATM Withdrawal Simulation")
print("-" * 40)

account_balance = 2500.00
print(f"  💳 Account Balance: GH₵{account_balance:.2f}")

withdrawal = float(input("  Enter withdrawal amount: GH₵"))

if withdrawal <= 0:
    print("  ❌ Invalid amount. Please enter a positive value.")
elif withdrawal > account_balance:
    print(f"  ❌ Insufficient funds. Your balance is GH₵{account_balance:.2f}.")
elif withdrawal > 1000:
    print("  ❌ Withdrawal limit exceeded. Maximum single withdrawal is GH₵1,000.")
else:
    account_balance -= withdrawal
    print(f"  ✅ GH₵{withdrawal:.2f} dispensed successfully.")
    print(f"  💳 Remaining Balance: GH₵{account_balance:.2f}")


# ------------------------------------------------------------
# EXERCISE 8: Login System
# ------------------------------------------------------------
print("\n📌 Exercise 8: Login System")
print("-" * 40)

correct_username = "nancy_data"
correct_password = "solavise2024"
max_login_attempts = 3
login_attempts = 0

print("  🔐 Welcome to the Data Portal\n")

while login_attempts < max_login_attempts:
    entered_username = input("  Username: ")
    entered_password = input("  Password: ")
    login_attempts += 1

    if entered_username == correct_username and entered_password == correct_password:
        print(f"\n  ✅ Login successful! Welcome back, {entered_username}! 🎉")
        print("  📊 Redirecting to your data dashboard...")
        break
    else:
        remaining = max_login_attempts - login_attempts
        if remaining > 0:
            print(f"  ❌ Incorrect credentials. {remaining} attempt(s) remaining.\n")
        else:
            print("  🔒 Account locked after 3 failed attempts. Contact admin.")

print("\n✅ Section 3 Complete!\n")
