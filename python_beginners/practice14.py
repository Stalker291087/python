score = int(input("Type the student grade: "))

if score >= 90:
    print("The student had a " + str(score) + " which is an A.")
if score >= 80 and score < 90:
    print("The student had a " + str(score) + " which is an B.")
if score >= 70 and score < 80:
    print("The student had a " + str(score) + " which is an C.")
if score >= 60 and score < 70:
    print("The student had a " + str(score) + " which is an D.")
if score <= 59:
    print("The student had a " + str(score) + " which is an D.")
