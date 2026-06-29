score_input = input("Enter a score (0-100): ")
score = int(score_input)
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("needs improvement")
        