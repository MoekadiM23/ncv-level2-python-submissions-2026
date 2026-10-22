mark = int(input("Enter a whole-number mark (0-100): "))
    
    # 1. Reject invalid values outside 0-100
    if mark < 0 or mark > 100:
        print("Invalid mark: Value must be between 0 and 100.")
    
    # 2. Classify valid marks (using an if-elif-else chain with descending thresholds)
    elif mark >= 80:
        classification = "Distinction"
        print(f"Classification: {classification}")
    elif mark >= 65:
        classification = "Merit"
        print(f"Classification: {classification}")
    elif mark >= 50:
        classification = "Competent"
        print(f"Classification: {classification}")
    else:
        classification = "Not Yet Competent"
        print(f"Classification: {classification}")

    # Extension: Second decision to check if the learner reached 'Competent' or above (mark >= 50)
    if 0 <= mark <= 100:
        is_competent_or_above = mark >= 50  # Uses boolean expression directly (avoiding == True)
        if is_competent_or_above:
            print("Competent Status: Yes (Reached Competent or above)")
        else:
            print("Competent Status: No (Did not reach Competent)")

except ValueError:
    print("Invalid input: Please enter a valid whole number.")