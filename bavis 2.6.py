
import random
import time

# bavis game

# the variables
bavis_time = 0
bavis_counter = 0
g_bavis_counter = 0
multiplier = 1
lives = 3
hardcore = 0
luck = 10000
prestige = 0
rebirth = 0

# this tells the user about the help command
print('!! P.S !!\nType in bavis.help to get the help page.')

# the bavis simulator itself. this asks the user "Bavis?", in which case they have to reply: "bavis"
# if they fail to do so, it says "LOL GET TROLLED", and then the program raises a BaseException to "crash".

# this for loop makes this run ALOT of times, as you can see.

for i in range(999999999999999999999999999):
# this asks for an input
    bavis = input('Bavis?\n')
# then if the user replies with "bavis", one "bavis" gets added to the bavis_counter variable.
    if bavis == 'bavis':
        bavis_counter += 1*multiplier + (1*prestige) + (100*rebirth)
        bavis_time += 1
        if hardcore == 1:
            lives = 1

# this is the save feature, which saves the game everytime "bavis" is run
        # this is the save feature, which saves the game everytime "bavis" is run
        filesave = open("Logs.txt", "w")
        filesave.write(
        str(bavis_counter) + "\n" +
        str(g_bavis_counter) + "\n"  +
        str(multiplier) + "\n" +
        str(lives) + "\n" +
        str(hardcore) + "\n" +
        str(luck) + "\n" +
        str(prestige) + "\n" +
        str(rebirth) + "\n" +
        str(bavis_time)
        )
        filesave.close()

# this is the randomizer for the golden bavis.
        g_bavis_decide = random.randint(1,luck)
        if g_bavis_decide == 1:
            print('============================\nNO WAY!\nYOU JUST GOT A GOLDEN BAVIS!\n============================')
            g_bavis_counter += 1 + (1*prestige) + (10*rebirth)
# then this wraps texts, to show how much "bavis" the user has.
        print('==============================\nBavises = ' + str(bavis_counter)+'\nGolden Bavises = ' + str(g_bavis_counter)+'\nTimes you have said Bavis = ' + str(bavis_time) + '\n==============================')
# a cheat, which allows the user to give themselves an infinite amount of "bavises"
    elif bavis == 'bavis.give':
        bavis_want = input('How much bavis do you want? (Number)\n')
        bavis_counter += int(bavis_want)
        # then this wraps texts, to show how much "bavis" the user has.
        print('==============================\nBavises = ' + str(bavis_counter)+'\nGolden Bavises = ' + str(g_bavis_counter)+'\n==============================')
# another cheat, which gives the user however many lives they want
    elif bavis == 'lives.give':
        lives_want = input('How many lives do you want? (Number)\n')
        lives += int(lives_want)
        # then this wraps texts, to show how many lives the user has.
        print('==============================\nLives = ' + str(lives)+'\n==============================')
# yet another cheat, which gives the user however many golden bavis' they want.
    elif bavis == 'gbavis.give':
        gbavis_want = input('How many Golden Bavis\' do you want? (Number)\n')
        g_bavis_counter += int(gbavis_want)
        # then this wraps texts, to show how many bavis the user has.
        print('==============================\nBavises = ' + str(bavis_counter)+'\nGolden Bavises = ' + str(g_bavis_counter)+'\n==============================')
# however, unlike the ones above, this is a MODE. this is hardcore mode, where you only have 1 life, and you cannot increase that.
# if the hardcore variable is 0, the game is normal, however if the hardcore variable is 1, the game is hardcore.
    elif bavis == 'hardcore.enable':
        print('HARDCORE MODE ENABLED.')
        print('WATCH OUT.')
        hardcore = 1
        lives = 1
# this is a help command. it is used to help people through commands.
    elif bavis == 'bavis.help':
        print('================================= Help ==========================================')
        print('bavis - The default command. Use this to increase your bavis_counter variable.')
        print('bavis.shop - Use to open the shop.')
        print('bavis.give - Use to give yourself a certain amount of bavis.')
        print('lives.give - Use to give yourself a certain amount of lives.')
        print('gbavis.give - Use to give yourself a certain amount of golden bavis.')
        print('luck.give - Use to give yourself a certain amount of luck.')
        print('multi.give - Use to give yourself a certain amount of multipliers.')
        print('prestige.give - Use to give yourself a certain amount of prestiges.')
        print('rebirth.give - Use to give yourself a certain amount of rebirths.')
        print('hardcore.enable - Use to enable hardcore mode. (CANNOT BE DISABLED)')
        print('bavis.help - Use to print this.')
        print('bavis.get - Used to get the values of items.')
        print('bavis.load - Used to load the game in the logs file.')
        print('bavis.prestige - Used to prestige')
        print('bavis.rebirth - Used to rebirth.')
        print('==================================================================================')
# these commands are "get" commands. these commands allow you to get the value of something.
    elif bavis == 'bavis.get':
        print('1> Multipliers')
        print('2> Lives')
        print('3> Luck')
        print('4> Golden bavis')
        print('5> Prestiges')
        print('6> Rebirths')
        getitem = input('What item would you like to get the value of?\n')
        # this is the actual code for the get command.
        if getitem == '1':
            print('===========================\n'+str(multiplier)+' Multipliers.\n===========================')
        elif getitem == '2':
            print('===========================\n'+str(lives)+' Lives.\n===========================')
        elif getitem == '3':
            print('===========================\n'+str(10000-luck)+' Luck.\n===========================')
        elif getitem == '4':
            print('===========================\n'+str(g_bavis_counter)+' Golden Bavis.\n===========================')
        elif getitem == '5':
            print('===========================\n'+str(prestige)+' Prestiges.\n===========================')
        elif getitem == '6':
            print('===========================\n'+str(rebirth)+' Rebirths.\n===========================')

    # this is for giving the user luck

    elif bavis == 'luck.give':
        luck_want = input('How much Luck do you want? (Number)\n')
        luck -= int(luck_want)

    # and this is for giving the user multipliers.

    elif bavis == 'multi.give':
        multi_want = input('How many multipliers do you want? (Number)\n')
        multiplier += int(multi_want)

    # this is the load command, to load a previous save.

    elif bavis == 'bavis.load':
        fileload = open("Logs.txt", "r")
        line = fileload.readlines()
        bavis_counter = int(line[0].strip("\n"))
        g_bavis_counter = int(line[1].strip("\n"))
        multiplier = int(line[2].strip("\n"))
        lives = int(line[3].strip("\n"))
        hardcore = int(line[4].strip("\n"))
        luck = int(line[5].strip("\n"))
        prestige = int(line[6].strip("\n"))
        rebirth = int(line[7].strip("\n"))
        bavis_time = int(line[8].strip("\n"))

    elif bavis == 'bavis.prestige':
        areyousureprestige = input('Prestiging costs 100 Golden bavis\'.\nAre you sure you would like to continue?\n')
        if areyousureprestige == 'yes' and g_bavis_counter >= 100:
            prestige += 1
            g_bavis_counter = 0
            bavis_counter = 0
            lives = 3
            if hardcore == 1:
                lives = 1
            luck = 10000
        elif areyousureprestige == 'no':
            print('ok sure')

    elif bavis == 'bavis.rebirth':
        areyousurerebirth = input('Rebirthing costs 200 Prestiges.\nAre you sure you would like to continue?\n')
        if areyousurerebirth == 'yes' and prestige >= 200:
            rebirth += 1
            prestige = 0
            g_bavis_counter = 0
            bavis_counter = 0
            lives = 3
            if hardcore == 1:
                lives = 1
            luck = 10000
        elif areyousurerebirth == 'no':
            print('ok sad')

    elif bavis == 'prestige.give':
        prestige_want = input('How many prestiges do you want? (Number)\n')
        prestige += int(prestige_want)

    elif bavis == 'rebirth.give':
        rebirth_want = input('How many rebirths do you want? (Number)\n')
        rebirth += int(rebirth_want)
        

# the shop system for buying things.
    elif bavis == 'bavis.shop':
        print('=========== Shop ============')
        print()
        print('=== Multipliers ===')

        print('1> +1x multiplier')
        print('  50 Bavis points')

        print('2> +2x multiplier')
        print('  100 Bavis points')

        print('3> +4x multiplier')
        print('  200 Bavis points')

        print('4> +8x multiplier')
        print('  400 Bavis points')
        print()
        print('=== Lives ===')

        print('5> +1 Lives')
        print('  1000 Bavis points')

        print('6> +2 Lives')
        print('  2000 Bavis points')

        print('7> +3 Lives')
        print('  3000 Bavis points')

        print('8> +4 Lives')
        print('  4000 Bavis points')
        print()
        print('=== Golden purchases ===')

        print('9> 1,000,000 Bavis points')
        print('  1 Golden Bavis')

        print('10> Trophy')
        print('  1,000,000,000 Golden Bavis')
        print()
        print('=== User inputted purchases ===')

        print('11> User inputted Multipliers')
        print('  11max> Buy the max amount that you can')
        print('12> User inputted Lives')
        print('  12max> Buy the max amount that you can')
        print('13> User inputted Luck effect')
        print('  13max> Buy the max amount that you can')
        print()
        print('=== Effects ===')

        print('14> Luck')
        print('  1,000,000 Bavis points')

        shopbuy = input('\nEnter what you would like to buy.\n')
# this is the shop results, when you buy something.
        # this is when you buy one multiplier.
        if shopbuy == '1' and bavis_counter >= 50:
            bavis_counter -= 50
            multiplier += 1
            print('Multiplier succesfully increased by 1.\n===========================')
            # however, this is when you buy 2
        elif shopbuy == '2' and bavis_counter >= 100:
            bavis_counter -= 100
            multiplier += 2
            print('Multiplier succesfully increased by 2.\n===========================')
            # this is when you buy 4
        elif shopbuy == '3' and bavis_counter >= 200:
            bavis_counter -= 200
            multiplier += 4
            print('Multiplier succesfully increased by 4.\n===========================')
            # and when you buy 8.
            # 8 is the max since i dont think anyone has such a low life to play this game for 7 hours lmao
        elif shopbuy == '4' and bavis_counter >= 400:
            bavis_counter -= 400
            multiplier += 8
            print('Multiplier succesfully increased by 8.\n===========================')
            
            # then this is to buy lives, which are very useful for later on in the game. ========================================

        elif shopbuy == '5' and bavis_counter >= 1000:
            bavis_counter -= 1000
            lives += 1
            print('Lives succesfully increased by 1.\n===========================')
            if hardcore == 1:
                lives = 1
                print('Wait... This is hardcore mode!\nI\'m removing your extra lives.')
        elif shopbuy == '6' and bavis_counter >= 2000:
            bavis_counter -= 2000
            lives += 2
            print('Lives succesfully increased by 2.\n===========================')
            if hardcore == 1:
                lives = 1
                print('Wait... This is hardcore mode!\nI\'m removing your extra lives.')
        elif shopbuy == '7' and bavis_counter >= 3000:
            bavis_counter -= 3000
            lives += 3
            print('Lives succesfully increased by 3.\n===========================')
            if hardcore == 1:
                lives = 1
                print('Wait... This is hardcore mode!\nI\'m removing your extra lives.')
        elif shopbuy == '8' and bavis_counter >= 4000:
            bavis_counter -= 4000
            lives += 4
            print('Lives succesfully increased by 4.\n===========================')
            if hardcore == 1:
                lives = 1
                print('Wait... This is hardcore mode!\nI\'m removing your extra lives.')

            # then these are the golden purchases, for the rarest of items.
            # golden bavis are a one in one thousand chance to drop, after typing "bavis"

        elif shopbuy == '9' and g_bavis_counter >= 1:
            g_bavis_counter -= 1
            bavis_counter += 1000000
            print('Succesfully bought 1,000,000 Bavis.\n===========================')

            # this is if you buy the trophy, which is the finale of the game.
            # this is a cutscene
        elif shopbuy == '10' and g_bavis_counter >= 1000000000:
            g_bavis_counter -= 1000000000
            print('Well done, you beat the game. You got the trophy. You may leave now.')
            time.sleep(3)
            print('...')
            time.sleep(4)
            print('Okay, why are you still here? What do you want?')
            time.sleep(3)
            print('I GAVE YOU A TROPHY! JUST LEAVE ALREADY!')
            time.sleep(5)
            print('Fine, If you wont leave...')
            time.sleep(3)
            print('...')
            time.sleep(4)
            print('I\'ll do it myself.')
            time.sleep(3)
            print('Goodbye.')
            time.sleep(5)
            file = open("Logs.txt", "w")
            file.write("") 
            file.close()
            raise BaseException

        # this is the user inputted section, where the user can choose how much they want to buy.
        # they first choose how many they would like to buy, then it runs a calculation for the amount each multiplier costs.
        # afterwards, if the player has enough money, it will give them however many multipliers they bought.

        elif shopbuy == '11':
            user_input_11 = input('How many Multipliers would you like?\n')
            moneyrequiredm = int(user_input_11)*50
            if shopbuy == '11' and moneyrequiredm <= bavis_counter:
                bavis_counter -= moneyrequiredm
                multiplier += int(user_input_11)
                print('Succesfully bought '+str(user_input_11)+' multipliers!')

        # this is for buying the maximum amount that you can buy.
        # it uses floor division to calculate how many you can buy, and then gives you the multipliers.
        # if you cannot buy any, it will not give you any, and say that you need to "go get more bavis".
        # however if you can buy some, it will decrease your balance by how many you bought times by how much the item costs.
        # idk if that made sense, but the code is down below

        elif shopbuy == '11max':
            maxamountm = bavis_counter // 50
            if maxamountm <= 0:
                print('Go get more bavis.')
            elif maxamountm > 0:
                bavis_counter -= maxamountm*50
                multiplier += maxamountm
                print('Succesfully bought '+str(maxamountm)+' Multipliers.')

        elif shopbuy == '12max':
            maxamountl = bavis_counter // 1000
            if maxamountl <= 0:
                print('Go get more bavis.')
            elif maxamountl > 0:
                bavis_counter -= maxamountl*1000
                lives += maxamountl
                print('Succesfully bought '+str(maxamountl)+' Lives.')

        elif shopbuy == '13max':
            maxamounte = bavis_counter // 1000000
            if maxamounte <= 0:
                print('Go get more bavis.')
            elif maxamounte > 0:
                bavis_counter -= maxamounte*1000000
                luck -= maxamounte
                if luck <= 0:
                    luck = 1
                    print('Succesfully bought '+str(maxamounte)+' Luck effects.')

# the continuiation of the user inputted section ==========================================================

        elif shopbuy == '12':
            user_input_12 = input('How many Lives would you like?\n')
            moneyrequiredl = int(user_input_12)*1000
            if shopbuy == '12' and moneyrequiredl <= bavis_counter:
                bavis_counter -= moneyrequiredl
                lives += int(user_input_12)
                print('Succesfully bought '+str(user_input_12)+' Lives!')
                if hardcore == 1:
                    print('Actually, this is hardcore isn\'t it?')
                    print('These lives arent yours, kid.')
                    lives = 1

        elif shopbuy == '13':
            user_input_13 = input('How many luck effects would you like?\n')
            moneyrequirede = int(user_input_13)*1000000
            if shopbuy == '13' and moneyrequirede <= bavis_counter:
                bavis_counter -= moneyrequirede
                luck -= int(user_input_13)
                if luck <= 0:
                    luck = 1
                print('Succesfully bought '+str(user_input_13)+' luck effects!!')

                    # these are the effects, which give the user certain buffs permanently.

        elif shopbuy == '14' and bavis_counter >= 1000000:
            bavis_counter -= 1000000
            luck -= 1
            if luck <= 0:
                luck = 1
            print('Luck succesfully increased by 1.\n===========================')

    else:
# however, if the player doesnt type bavis, they get a message, and then the program ends.
        print('U mispelt it')
        lives -= 1
        if lives <= 0:
            print('YOU DIED LOL NOOB')
            time.sleep(1)
            raise BaseException
        elif lives > 0:
            print('You have ' + str(lives) + ' lives left.')
            time.sleep(1)
