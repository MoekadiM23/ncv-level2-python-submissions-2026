# Version 4: Add all ordered categories

mark = float(input("Enter the mark between 0 and 100: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 80:
    print("Outstanding")
elif mark >= 70:
    print("Highly competent")
elif mark >= 50:
    print("Competent")
elif mark >= 40:
    print("Not yet competent")
else:
    print("Not achieved")