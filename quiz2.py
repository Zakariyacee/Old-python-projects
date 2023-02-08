
def quiz():
    score = 0

    print("Q1: What is the largest country by landmass? ")
    print("A. China")
    print("B. Russia")
    print("C. Usa")

    answer = input()

    if answer.lower() == "c":
        print("Correct! ")
        score = score + 1
    else:
        print("Incorrect! ")

    print(score)

    answer = input(("Q2. What is the colour of the sky?\nA. Blue \nB. green \nC. yellow\n ")
    if answer.lower() == "a":
        print("Correct")
        score += 1
    else: print("Incorrect! ")

quiz()
