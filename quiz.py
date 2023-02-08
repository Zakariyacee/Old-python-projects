def quizgame():

    print("Welcome to our quiz game!")
    play = input("would you to play this game? Enter 'yes' or 'no': ")
    if play.lower() == "yes":
        print("Have fun!")
    else:
        quit()


    question = input("what is the best piece of fiction to ever exist?: ")

    if question.lower() == "attack on titan":
        print("Correct!")
    elif question.lower() != "attack on titan": # maybe you can use else: instead of having to write all this.
        print("False!")

    question2 = int(input("How many hours are there in a day?: "))
    if question2 == 24:
        print("Correct!")
    else:
        print("False!")

    question3 = input("By what month should i start applying to software developer jobs?: ")
    if question3.lower() == "november":
        print("Correct!")
    else:
        print("False!")
    
quizgame()

    
