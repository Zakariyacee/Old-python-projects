from random import choice

# create a list of animes, restaurants, movies, shows etc
def auto_anime():

# animes 
    s = ['Naruto', 'Bleach', 'Hellsing Ultimate']
    f = ['Monster', 'Summertime rendering']
    d = ['Honey & clover', 'Mushishi']

# input what mood you're in

    mood = input("What mood are you in: chill, action or mindboggling: " )

    if mood == "chill":
        print(choice(d))
    elif mood == 'action':
        print(choice(s))
    else:
        print(choice(f))

auto_anime()

# print a random anime for the list of animes
