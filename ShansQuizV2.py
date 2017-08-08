#Game texts provided by Udacity's pyc file (simplified for hard question)
easytext = 'A common first thing to do in a language is display\n\'Hello __1__!\'  In __2__ this is particularly easy; all you have to do\nis type in:\n__3__ "Hello __1__!"\nOf course, that isn\'t a very useful thing to do. However, it is an\nexample of how to output to the user using the __3__ command, and\nproduces a program which does something, so it is useful in that capacity.\n\nIt may seem a bit odd to do something in a Turing complete language that\ncan be done even more easily with an __4__ file in a browser, but it\'s\na step in learning __2__ syntax, and that\'s really its purpose.\n'
easyanswer = ['world', 'Python','print','HTML']
mediumtext = "\nA __1__ is created with the def keyword.  You specify the inputs a\n__1__ takes by adding __2__ separated by commas between the parentheses.\n__1__s by default returns __3__ if you don't specify the value to retrun.\n__2__ can be standard data types such as string, integer, dictionary, tuple,\nand __4__ or can be more complicated such as objects and lambda functions."
mediumanswer = ['function', 'arguments', 'None', 'list']
hardtext= "When you create a __1__, certain __2__s are automatically\ngenerated for you if you don't make them manually. These contain multiple\nunderscores before and after the word defining them.  When you write\na __1__, you almost always include at least the __3__ __2__, defining\nvariables for when __4__s of the __1__ get made. "
hardanswer = ['class', 'method', '__init__','instance']
blanks = ["___1___", "___2___", "___3___", "___4___"]
levels = ["easy", "medium", "hard"]
#Ask a player to select level of game
def selector():
        prompt = "Please select a level - easy, medium or hard:"
        difficulty = raw_input(prompt)
        for difficulty in levels:
            if difficulty == "easy":
                print easytext
                return (easytext, easyanswer)
            elif difficulty == "medium":
                print mediumtext
                return (mediumtext, mediumanswer)
            elif difficulty == "hard":
                print hardtext
                return (hardtext, hardanswer)
            else:
                return difficulty()

#Pop up information to ask player to select number of tries they wish to have
def max_attempts():
    prompt = "How many tries would you like to have:"
    return max_attempts

#Ask the player to answer
def answer(mark):
    for i in range(1,5):
        answer = raw_input("\nProvide what you think is suitable to fill in the blanks {_" + i + "_} : ".format(mark)).lower()
        i +=1
    return answer

#Fill in the blanks game
def play():
    index = 0

    print "\t\tWelcome to Python Quiz! \nHope you have fun and learn something new. \nLet the game begin...\n"

    difficulty, attempt = selector()
    life = max_attempts
    print "\nYou have "+ str(max_attempts) + ". Good luck!"

    while index < len(blanks):
        useranswer = answer(blanks[index])
        if useranswer == attempt[index]:
            print "\nGreat! You aced this:)\n"
            difficulty = difficulty.replace(blanks[index], useranswer)
            index += 1
        else:
            print "\nBad luck, try again:(\n"
            tries -= 1
            print "You have" + str(tries) + "left!"
    print "\nYou won!\n"
    print difficulty
    raw_input("Exit")

play()
