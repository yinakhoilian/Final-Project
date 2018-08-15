import textwrap
from random import randint

print('****************************Escape to New York****************************')
opening = 'Welcome to the Concrete Jungle. You just moved to New York and need \
to find a studio to rent. You are an experienced day trader. To see how much \
money you can spend per month on rent, you are going to take your weekly \
trading gains as an estimate. Based on your budget and preferences, you are \
trying to decide which neighborhood you should live in out of the following: \
Union Square, Tribeca, Ktown, Soho and Midtown.'
for line in textwrap.wrap(opening,80):
    print(line)

print('***********************************************************************')
print('You will now roll a dice to determine your trading skill level. Good luck!')

def dice(x,y):
    dice=randint(x,y)
    return dice

input('>>>Press any key + enter to roll the dice.')
roll = dice(1,6)
print('Congrats! You have a trading level skill of: ' + str(roll) +'. Now let us see how much money that translates to.')

if roll == 1:
    print('You have $1500 to spend for rent per month which is not enough to live in NY by yourself.')
    notenoughmoney = input('Do you wish to: 1) carry on by finding a roommate or 2) do you wish to work on your trading skills and come back another time? Press on the corresponding number + enter')
    if notenoughmoney == '1':
        print('Do not feel bad about finding a roommate. It is a great way to make new friends. Proceed onwards to see which neighborhood is the best fit for you.')
    elif notenoughmoney == '2':
        input('>>>Welcome back! You have been working diligently on your skill for the past year. Press any key + enter to see your current skill level.')
        secondroll = dice(3,6)
        print('Congrats! You have a trading level skill of: ' + str(secondroll) + '. Now let us see how much money that translates to.')
        if secondroll == 3:
            print('You have $1700 to spend for rent per month.')
        elif secondroll == 4:
            print('You have $1800 to spend for rent per month.')
        elif secondroll == 5:
            print('You have $1900 to spend for rent per month.')
        else:
            print('You earn $2000 per week and have that much to spend for rent.')
    else:
        print('You have provided an invalid response. Please exit and open the file again.')
elif roll == 2:
    print('You have $1600 to spend for rent per month which is not enough to live in NY by yourself.')
    notenoughmoney = input('Do you wish to: 1) carry on by finding a roommate or 2) do you wish to work on your trading skills and come back another time? Press on the corresponding number + enter')
    if notenoughmoney == '1':
        print('Do not feel bad about finding a roommate. It is a great way to make new friends. Proceed onwards to see which neighborhood is the best fit for you.')
    elif notenoughmoney == '2':
        input('>>>Welcome back! It has been a year and you have been working diligently on your skill. Press any key + enter to see your current skill level.')
        secondroll = dice(3,6)
        print('Congrats! You have a trading level skill of: ' + str(secondroll) +'. Now let us see how much money that translates to.')
        if secondroll == 3:
            print('You have $1700 to spend for rent per month.')
        elif secondroll == 4:
            print('You have $1800 to spend for rent per month.')
        elif secondroll == 5:
            print('You have $1900 to spend for rent per month.')
        else:
            print('You have $2000 to spend for rent per month.')
    else:
        print('You have entered an invalid response. Please reopen the file and try again.')
elif roll == 3:
    print('You have $1700 to spend for rent per month.')
elif roll == 4:
    print('You have $1800 to spend for rent per month.')
elif roll == 5:
    print('You have $1900 to spend for rent per month.')
else:
    print('You have $2000 to spend for rent per month.')

print('Before you head out into the Concrete Jungle, ask yourself the following: What do you like to do most in your spare time?')
favoriteactivity = input('Choose the letter that applies the most to you + enter: a) Reading a book at The Strand b) Going to the Hudson River Park c) Karaoke in Ktown d) Shopping e) Pretending to be a tourist. Or press q + enter to exit.')

neighborhoods = {'Union Square':0,'Tribeca':0,'Koreatown':0,'Soho':0,'Midtown':0}

if favoriteactivity == 'a':
    neighborhoods['Union Square']+=10

elif favoriteactivity == 'b':
    neighborhoods['Tribeca']+=10

elif favoriteactivity == 'c':
    neighborhoods['Koreatown']+=10

elif favoriteactivity == 'd':
    neighborhoods['Soho']+=10

elif favoriteactivity == 'e':
    neighborhoods['Midtown'] +=10

elif favoriteactivity == 'q':
    print('Thank you for playing!')
    exit()
else:
    print('You have entered an invalid response. Please reopen the file and try again.')

print('Now it is time to step out and look for an apt. You bump into a group of tourists and while you would like to catch the light and cross the street, they are blocking the way. Despite your attempts to say "excuse me", it is still very difficult to pass and you are forced to step off of the sidewalk into the road to pass.')
patiencewithtourists = input('Does this incident annoy you? Press y or n + enter for yes or no. Or press q + enter to exit.')

if patiencewithtourists == 'y':
    neighborhoods['Midtown']+=-10

elif patiencewithtourists == 'n':
    print('Good for you, you are a better person than the game creator!')

elif patiencewithtourists == 'q':
    print('Thank you for playing!')
    exit()
else:
    print('You have entered an invalid response. Please reopen the file and try again.')

print('You continue to walk through the Concrete Jungle. Wait, who do you see over there in front of the bodega? Is it who I think it is? Is that Ryan Reynolds? Wow he seems taller in person.')
celebritystruck = input('Did you enjoy this celebrity sighting and would you want to see more? Press y or n + enter for yes or no. Or press q + enter to exit.')

if celebritystruck == 'y':
    neighborhoods['Tribeca']+=10

elif celebritystruck == 'n':
    print('That is a sensible response.')

elif celebritystruck == 'q':
    print('Thank you for playing!')
    exit()
else:
    print('You have entered an invalid response. Please reopen the file and try again.')

max_value = max(neighborhoods.values())
max_keys = [k for k, v in neighborhoods.items() if v == max_value]

if max_value == 0:
    print('Based on your previous answers, you seem like you would be a good fit for any of these neighborhoods: Union Square, Tribeca, Koreatown, Soho or Midtown. Feel free to try living in any of these.')
else:
    print('Hope you are having a nice time in NY so far. Based on your previous answers, my prediction is that you will enjoy living in this neighborhood:' + str(max_keys) + '!')

print('Hope you enjoyed this game. Thank you for playing!')
exit()
