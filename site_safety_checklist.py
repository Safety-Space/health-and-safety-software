# Simple Site Safety Checklist Tool
# Run this script in a terminal (Python 3)

checklist = [
    "PPE worn (hard hats, boots, hi-vis)",
    "First aid kit available",
    "Fire extinguisher checked",
    "Hazard signs visible",
    "Incident logbook updated",
]

print("Site Safety Checklist")
print("====================")

for i, item in enumerate(checklist, start=1):
    answer = input(f"{i}. {item}? (y/n): ")
    status = "✅" if answer.lower() == "y" else "⚠️"
    print(f"{item}: {status}")

print("\nChecklist complete. Stay safe!")
print("For a full safety management system: https://safetyspace.co")
