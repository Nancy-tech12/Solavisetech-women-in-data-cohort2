# ============================================================
#   DATA STRUCTURES EXERCISES
#   Solavise Tech Women in Data – Cohort 2
#   Author: Nancy Yeboah
#   Background: Biological Sciences → Data Analysis
# ============================================================

print("=" * 55)
print("   SECTION 4: DATA STRUCTURES EXERCISES")
print("=" * 55)


# ------------------------------------------------------------
# EXERCISE 1: Favourite Tools List
# ------------------------------------------------------------
print("\n📌 Exercise 1: Favourite Data Tools List")
print("-" * 40)

tools = ["Python", "Excel", "SQL", "Tableau"]
print(f"  Initial tools list: {tools}")

# Add items
tools.append("Power BI")
tools.append("GitHub")
print(f"  After adding tools: {tools}")

# Remove an item
tools.remove("Excel")
print(f"  After removing Excel: {tools}")

print(f"  Total tools in list: {len(tools)}")


# ------------------------------------------------------------
# EXERCISE 2: Student Scores
# ------------------------------------------------------------
print("\n📌 Exercise 2: Student Scores Analysis")
print("-" * 40)

scores = [78, 92, 65, 88, 74, 95, 83, 70, 91, 60]

highest = max(scores)
lowest  = min(scores)
average = sum(scores) / len(scores)

print(f"  Scores:   {scores}")
print(f"  Highest:  {highest} 🏆")
print(f"  Lowest:   {lowest}  📉")
print(f"  Average:  {average:.1f} 📊")

# Bonus: count how many passed (score >= 50)
passed = [s for s in scores if s >= 50]
print(f"  Passed:   {len(passed)}/{len(scores)} students")


# ------------------------------------------------------------
# EXERCISE 3: Shopping List Manager
# ------------------------------------------------------------
print("\n📌 Exercise 3: Shopping List Manager")
print("-" * 40)

shopping_list = ["Rice", "Tomatoes", "Onions", "Chicken"]
print(f"  🛒 Current list: {shopping_list}")

# Add items
shopping_list.append("Cooking Oil")
shopping_list.append("Pepper")
print(f"  After adding:   {shopping_list}")

# Remove item
shopping_list.remove("Onions")
print(f"  After removing Onions: {shopping_list}")

# Check if item exists
item_to_check = "Rice"
if item_to_check in shopping_list:
    print(f"  ✅ '{item_to_check}' is in your shopping list.")
else:
    print(f"  ❌ '{item_to_check}' is NOT in your shopping list.")

print(f"  Total items to buy: {len(shopping_list)}")


# ------------------------------------------------------------
# EXERCISE 4: Country Capitals (Tuples)
# ------------------------------------------------------------
print("\n📌 Exercise 4: Country Capitals using Tuples")
print("-" * 40)

# Tuples are immutable — perfect for fixed data like capitals
country_capitals = (
    ("Ghana", "Accra"),
    ("Nigeria", "Abuja"),
    ("Kenya", "Nairobi"),
    ("South Africa", "Pretoria"),
    ("Egypt", "Cairo"),
    ("Rwanda", "Kigali"),
)

print("  🌍 African Country Capitals:")
for country, capital in country_capitals:
    print(f"     {country:<15} →  {capital}")

# Access a specific tuple
print(f"\n  First entry: {country_capitals[0][0]} — {country_capitals[0][1]}")
print(f"  Tuples cannot be changed (immutable) — great for fixed reference data!")


# ------------------------------------------------------------
# EXERCISE 5: Unique Visitors (Sets)
# ------------------------------------------------------------
print("\n📌 Exercise 5: Unique Visitors using Sets")
print("-" * 40)

# Raw visitor log — contains duplicates
visitor_log = ["Nancy", "Ama", "Kofi", "Nancy", "Efua", "Kofi", "Abena", "Ama", "Nancy"]
print(f"  Raw visitor log ({len(visitor_log)} entries): {visitor_log}")

# Convert to set — automatically removes duplicates
unique_visitors = set(visitor_log)
print(f"  Unique visitors ({len(unique_visitors)} people): {unique_visitors}")
print(f"  Duplicates removed: {len(visitor_log) - len(unique_visitors)}")


# ------------------------------------------------------------
# EXERCISE 6: Common Skills (Set Intersection)
# ------------------------------------------------------------
print("\n📌 Exercise 6: Common Skills Between Two Cohorts")
print("-" * 40)

cohort_1_skills = {"Python", "Excel", "SQL", "Tableau", "Statistics"}
cohort_2_skills = {"Python", "SQL", "Power BI", "GitHub", "Statistics"}

print(f"  Cohort 1 skills: {cohort_1_skills}")
print(f"  Cohort 2 skills: {cohort_2_skills}")

common_skills   = cohort_1_skills & cohort_2_skills   # intersection
all_skills      = cohort_1_skills | cohort_2_skills   # union
unique_to_c1    = cohort_1_skills - cohort_2_skills   # difference

print(f"\n  🤝 Skills in BOTH cohorts:       {common_skills}")
print(f"  📚 All skills combined:          {all_skills}")
print(f"  🔵 Unique to Cohort 1:           {unique_to_c1}")


# ------------------------------------------------------------
# EXERCISE 7: Student Record (Dictionary)
# ------------------------------------------------------------
print("\n📌 Exercise 7: Student Record using Dictionary")
print("-" * 40)

student_record = {
    "name":          "Nancy Yeboah",
    "age":           24,
    "program":       "Women in Data – Cohort 2",
    "background":    "Biological Sciences",
    "skills":        ["Python", "Git", "GitHub", "Excel"],
    "gpa":           3.7,
    "is_active":     True
}

print("  📋 Student Record:")
for key, value in student_record.items():
    print(f"     {key:<15}: {value}")

# Update a field
student_record["skills"].append("SQL")
print(f"\n  After adding SQL → Skills: {student_record['skills']}")


# ------------------------------------------------------------
# EXERCISE 8: Mini Contact Book
# ------------------------------------------------------------
print("\n📌 Exercise 8: Mini Contact Book")
print("-" * 40)

contact_book = {
    "Nancy Yeboah":   "+233-XX-XXX-0001",
    "Ama Mensah":     "+233-XX-XXX-0002",
    "Efua Asante":    "+233-XX-XXX-0003",
    "Abena Boateng":  "+233-XX-XXX-0004",
    "Kofi Owusu":     "+233-XX-XXX-0005",
}

print("  📱 Contact Book:")
for name, number in contact_book.items():
    print(f"     {name:<18} : {number}")

# Search for a contact
search_name = input("\n  Search for a contact (enter name): ")

if search_name in contact_book:
    print(f"  ✅ Found! {search_name}: {contact_book[search_name]}")
else:
    print(f"  ❌ '{search_name}' not found in contact book.")

# Add new contact
contact_book["Akosua Darko"] = "+233-XX-XXX-0006"
print(f"\n  ✅ New contact added. Total contacts: {len(contact_book)}")

print("\n✅ Section 4 Complete!")
print("\n" + "=" * 55)
print("   🎉 ALL SECTIONS COMPLETE — GREAT WORK, NANCY!")
print("=" * 55)
