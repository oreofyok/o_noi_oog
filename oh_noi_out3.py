import random
import time

human3 = False
human4 = False
game2 = False

print("This game will find who is final lose")
while True:
    human = input("1.solo or 2.multi players 3.only players 4.only com: ")
    if human == "1" or human == "2" or human == "3" or human == "4":
        break
    else:
        print("only 1,2,3,or 4")
    
if human == "1":
    select_amount_of_com = int(input("how many com do you want to play: "))
elif human == "2" or human == "3":
    if human == "3":
        human3 = True
    while True:
        select_amount_of_player = int(input("how many players you want to play: "))
        if select_amount_of_player <= 1:
            print("more than 1")
        else:
            break



        
    #select_amount_of_com = int(input("how many com do you want to play: "))

choices = ["f","b"]

def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key,default_value) 
    

def com_input(x):
    com = {}
    for i in range(1,x+1):
        com[f"com{[i]}"] = random.choice(choices)
    
    print()
    time.sleep(.5)
    while True:
        auto_com_name = input("input com name auto on or off: ")
        if auto_com_name == "on" or auto_com_name == "off":
            break
        else:
            print("input only on or off")
    if auto_com_name == "off":
        print("define com name")
        print("spcae bar to use com[num] name")
    auto_com_count = 0
    for i in list(com):
        old = i
        if auto_com_name == "on":
            new = i
        elif auto_com_name == "off":
            new = input(f"define your {i} name: ")
        if len(new) == 0:
            new = i
        change_dict_key(com, old, new)
        
        if auto_com_name == "on":
            if auto_com_count < 10:
                print(old ,"=",new) ; auto_com_count += 1 ; time.sleep(.1)
            elif auto_com_count >= 10 and auto_com_count < 100:
                print(old ,"=",new) ; auto_com_count += 1 ; time.sleep(.01)
            elif auto_com_count >= 100:
                print(old ,"=",new)
    
    return com
    
def player_input(x):
    global select_amount_of_com
    players = {}
    for i in range(1,x+1):
        players[f"player{[i]}"] = "s"
    
    while True:
        auto_players_name = input("input players name auto on or off: ")
        if auto_players_name == "on" or auto_players_name == "off":
            break
        else:
            print("input only on or off")
    if auto_players_name == "off":
        print("define your name")
        print("space bar to ues player[num] name")
    auto_players_count = 0
    for i in list(players):
        old = i
        if auto_players_name == "on":
            new = i
        elif auto_players_name == "off":
            new = input(f"define your {i} name: ")
        if len(new) == 0:
            new = i
        change_dict_key(players,old,new)
        if auto_players_name == "on":
            if auto_players_count < 10:
                print(old,"=",new) ; auto_players_count += 1 ; time.sleep(.1)
            elif auto_players_count >= 10 and auto_players_count < 100:
                print(old,"=",new) ; auto_players_count += 1 ; time.sleep(.01)
            elif auto_players_count >= 100:
                print(old,"=",new)
    
    if human3 != True:
        while True:
            select_amount_of_com = int(input("how many com do you want to play: "))
            if select_amount_of_com > 2:
                break
            else:
                print("must more than 2")
    return players
    #com_input(select_amount_of_com)
    
playing = True
stop = False

def play2(players,com):
    global game2
    if human == "1":
        if len(com) == 1: # player and com
            rps = True
            while rps == True:
                while True:
                    me = input("r p s: ")
                    if me == "r" or me == "p" or me == "s":
                        break
                    else:
                        print("input only r p or s")
                for i in com:
                    c_think = random.choice(["r","p","s"])
                    print(i,"choose",c_think)
                if (me == "r" and c_think == "s") or (me == "p" and c_think == "r") or (me == "s" and c_think == "p"):
                    print("you win") ; print(i,"is the final lose");rps = False
                elif (me == "r" and c_think == "p") or (me == "p" and c_think == "s") or (me == "s" and c_think == "r"):
                    print(i,": win") ; print("you are the final lose"); rps = False
                elif me == c_think:
                    print("draw play again.")
            #quit()
            
        elif len(com) == 2: # no player
            cc = {}; rps = True
            while rps == True:
                cc1 = [];cc2 = []
                for i in com:
                    cc[i] = random.choice(["r","p","s"])
                    cc1.append(i) ; cc2.append(cc[i])
                print(cc) 
                if (cc2[0] == "r" and cc2[1] == "s") or (cc2[0] == "p" and cc2[1] == "r") or (cc2[0] == "s" and cc2[1] == "p"):
                    print(cc1[0],": win") ; print(cc1[1],"is the final lose");rps = False
                elif (cc2[0] == "r" and cc2[1] == "p") or (cc2[0] == "p" and cc2[1] == "s") or (cc2[0] == "s" and cc2[1] == "r"):  
                    print(cc1[1],": win") ; print(cc1[0],"is the final lose");rps = False
                elif cc2[0] == cc2[1]:
                    print('draw try again.')
    elif human == "2":
        if playing == True and len(players) == 2: # 2 players left
            hh = {} ; rps = True
            while rps == True:
                pp1 = [] ; pp2 = []
                for i in players:
                    while True:
                        hh[i] = input(f"{i} select r,p,or s: ")
                        if hh[i] == "r" or hh[i] == "p" or hh[i] == "s":
                            break
                        else:
                            print("input only r p or s")
                    pp1.append(i) ; pp2.append(hh[i])
                if (pp2[0] == "r" and pp2[1] == "s") or (pp2[0] == "p" and pp2[1] == "r") or (pp2[0] == "s" and pp2[1] == "p"):
                        print(pp1[0],": win") ; print(pp1[1],"is the final lose"); rps = False
                elif (pp2[0] == "r" and pp2[1] == "p") or (pp2[0] == "p" and pp2[1] == "s") or (pp2[0] == "s" and pp2[1] == "r"):  
                    print(pp1[1],": win") ; print(pp1[0],"is the final lose"); rps = False
                elif pp2[0] == pp2[1]:
                    print('draw try again.')
        elif len(com) == 1: # 1 player and 1 com left
            rps = True
            while rps == True:
                for p in players:
                    while True:
                        me = input(f"{p} choose r,p,or s:")
                        if me == "r" or me == "p" or me == "s":
                            break
                        else:
                            print("input only r p or s")
                for i in com:
                    c_think = random.choice(["r","p","s"])
                    print(i,"choose",c_think)
                if (me == "r" and c_think == "s") or (me == "p" and c_think == "r") or (me == "s" and c_think == "p"):
                    print(p,"win") ; print(i,"is the final lose");rps = False
                elif (me == "r" and c_think == "p") or (me == "p" and c_think == "s") or (me == "s" and c_think == "r"):
                    print(i,": win") ; print(p,"is the final lose"); rps = False
                elif me == c_think:
                    print("draw play again.")
        elif len(com) == 2: # 2 com left
            cc = {}; rps = True
            while rps == True:
                cc1 = [];cc2 = []
                for i in com:
                    cc[i] = random.choice(["r","p","s"])
                    cc1.append(i) ; cc2.append(cc[i])
                print(cc) 
                if (cc2[0] == "r" and cc2[1] == "s") or (cc2[0] == "p" and cc2[1] == "r") or (cc2[0] == "s" and cc2[1] == "p"):
                    print(cc1[0],": win") ; print(cc1[1],"is the final lose"); rps = False
                elif (cc2[0] == "r" and cc2[1] == "p") or (cc2[0] == "p" and cc2[1] == "s") or (cc2[0] == "s" and cc2[1] == "r"):  
                    print(cc1[1],": win") ; print(cc1[0],"is the final lose");rps = False
                elif cc2[0] == cc2[1]:
                    print('draw try again.')
                    
    game2 = True

def play(players,com):
    global playing;global stop
    
    while stop != True:
    
        if com != None:
            for i in com.keys():
                com[i] = random.choice(choices)
        
        print()
        count_f = 0 ; count_b = 0
        
        player = " "
        
        com_out = [] ; play_out = []
    
        if com != None: 
            for i in com:
                if com[i] == "f":
                    count_f += 1
                elif com[i] == "b":
                    count_b += 1
        
        
        if count_b + count_f > 2 and playing == False or count_b + count_f > 1 and playing != False:
            if human3 == False:
                print("com =",com)
        elif count_b + count_f == 1 and human == "2" and len(players) > 1:
            if human3 == False:
                print("com =",com)
        elif count_b + count_f == 1 and human == "2" and  playing == True and len(players) == 1:
            c = [] ; p = []
            for i in com:
                c.append(i)
            for i in players:
                p.append(i)
            print(f"only {p[0]} and {c[0]} left")
        else:
            if count_b + count_f == 2 and playing == False:
                c = [i for i in com]
                print("only",c[0],"and",c[1],"left")
            elif count_b + count_f == 1 and playing != False and human == "1":
                for i in com:
                    print("only you and",i,"left")
                    
        if human == "1":
            if playing == True and stop != True and len(com) > 1:
                while True:
                    player = input("You choose f or b: ").lower()
                    if player == "f" or player == "b":
                        break
                    else:
                        print("input only f or b")
                if player == "f":
                    count_f += 1
                elif player == "b":
                    count_b += 1
        elif human == "2":
            if len(players) > 1 and len(com) >= 1 or len(players) >= 1 and len(com) > 1 or len(players) > 2 and len(com) == 0:
                for p in players.keys():
                    while True:
                        players[p] = input(f"{p} select f or b: ").lower()
                        if players[p] == "f" or players[p] == "b":
                            break
                        elif players[p] == "q":
                            quitt = input("Sure to Quit? y or n: ").lower()
                            if quitt == "y":
                                print("Game Quit")
                                quit()
                            else:
                                print("OK back to the game")
                        else:
                            print("input only f or b")
                    if players[p] == "f":
                        count_f += 1
                    elif players[p] == "b":
                        count_b += 1
            elif players == None:
                playing == False
                pass
        
        if count_b + count_f > 2 and playing == False or count_b + count_f > 1 and playing != False:
            if human4 == False and players != None:
                print("players =",players)
            if human3 == False:
                print("com =",com)
        elif count_b + count_f == 1 and human == "2" and len(players) > 1:
            if human4 == False and players != None:
                print("players =",players)
            if human3 == False:
                print("com =",com)
        elif count_b + count_f == 1 and human == "2" and playing == True and len(players) == 1:
            c = [] ; p = []
            for i in com:
                c.append(i)
            for i in players:
                p.append(i)
            print(f"only {p[0]} and {c[0]} left")
        else:
            if count_b + count_f == 2 and playing == False:
                c = [i for i in com]
                print("only",c[0],"and",c[1],"left")
            elif count_b + count_f == 1 and playing != False and human == "1":
                for i in com:
                    print("only you and",i,"left")
                    
        if human == "1":
            if count_b + count_f == 1 and playing == True:   # you and com go r p s
                c = []
                for i in com:
                    print(f"you and {i} go to r p and s")
                    c.append(i)
                stop = True
                play2(None,c)
            elif count_b + count_f == 2 and playing == False:  # com and com go r p s
                c = []
                for i in com:
                    c.append(i)
                print(f"{c[0]} and {c[1]} go to r p and s")
                stop = True
                play2(None,c)
            elif count_f == count_b and count_f > 1 or count_f == 0 or count_b == 0:  # draw
                print("draw f =",count_f,"b =",count_b)
            else:
                if count_f > count_b:
                    print("b outed")
                    if player == "b":
                        print("You win ,outed.")
                        print()
                        playing = False
                    elif player == "f":
                        print("Go to next round.")
                    if com!= None:
                        for i in com:
                            if com[i] == "b":
                                com_out.append(i)
                        
                        
                elif count_f < count_b:
                    print("f outed")
                    if player == "b":
                        print("Go to next round.")
                        
                    elif player == "f":
                        print("You win,outed")
                        playing = False
                        
                    
                    if com != None:
                        for i in com:
                            if com[i] == "f":
                                com_out.append(i)
                                
                print("com out =",len(com_out),com_out)
                if com != None:
                    for i in com_out:
                        if i in com.keys():
                            del com[i]
                             
        elif human == "2":
            if count_b + count_f == 0 and len(players) == 2: # 2 players left
                p = []
                for i in players:
                    p.append(i)
                print(p[0],"and",p[1],"go to r p s")
                stop = True
                play2(p,None)
            elif count_b + count_f == 1 and playing == True and len(players) == 1: # 1 player and 1 com left
                p = [] ; c = []
                for i in players:
                    p.append(i)
                for i in com:
                    c.append(i)
                print(p[0],"and",c[0],"go to r p s") 
                stop = True
                play2(p,c)
            elif count_b + count_f == 2 and playing == False: # 2 com left
                c = []
                for i in com:
                    c.append(i)
                print(c[0],"and",c[1],"go to r p s")
                stop = True
                play2(None,c)
            elif count_b == count_f and count_f > 1 or count_f == 0 or count_b == 0: # b = f and b,f != 0 or b == 0 or f == 0
                print("draw f =",count_f,"b =",count_b)
            else:
                if count_f > count_b and playing == True: # b < f and player still play
                    print("b outed")
                    if human3 == False and com != None:
                        for i in com:
                            if com[i] == "b":
                                com_out.append(i)
                        print("com out =",len(com_out),com_out)
                        for i in com_out:
                            if i in com.keys():
                                del com[i]
                    if human4 == False and players != None:
                        for i in players:
                            if players[i] == "b":
                                play_out.append(i)
                        print("player out =",len(play_out),play_out)
                        for i in play_out:
                            if i in players.keys():
                                del players[i]
                                
                elif count_f < count_b and playing == True: # b > f and player still playing
                    print("f outed")
                    if human3 == False and com != None:
                        for i in com:
                            if com[i] == "f":
                                com_out.append(i)
                        print("com out =",len(com_out),com_out)
                        for i in com_out:
                            if i in com.keys():
                                del com[i]
                    if human4 == False and players != None:
                        for i in players:
                            if players[i] == "f":
                                play_out.append(i)
                        print("player out =",len(play_out),play_out)
                        for i in play_out:
                            if i in players.keys():
                                del players[i]
                elif count_f < count_b and playing == False: # b > f and player all out
                    print("f outed")
                    if human3 == False and com != None:
                        for i in com:
                            if com[i] == "f":
                                com_out.append(i)
                                
                        print("com out =",len(com_out),com_out)
                        for i in com_out:
                            if i in com.keys():
                                del com[i]
                elif count_f > count_b and playing == False: # b < f and player all out
                    print("b outed")
                    if human3 == False and com != None:
                        for i in com:
                            if com[i] == "b":
                                com_out.append(i)
                        print("com out =",len(com_out),com_out)
                        for i in com_out:
                            if i in com.keys():
                                del com[i]
        
        if human == "2" and len(players) == 0:
            playing = False
            if human4 != True:
                print("players all out")
        elif human3 == False and human == "2" and len(com) == 0:
            print("com all out")
            
        if game2 == False and human == "2":
            if len(players) != 0:
                still_p = [i for i in players]
                print("players left = ",len(still_p),still_p)
            if len(com) != 0:
                still_c = [i for i in com]
                print("com left = ",len(still_c),still_c)
             
        # if stop != True:
        #     play(players,com)


if human == "1":
    play(None,com_input(select_amount_of_com))
elif human == "2":
    play(player_input(select_amount_of_player),com_input(select_amount_of_com))
elif human == "3":
    human = "2"
    play(player_input(select_amount_of_player),{})
elif human == "4":
    human4 = True
    human = "2"
    while True:
        select_amount_of_com = int(input("how many com do you want to play: "))
        if select_amount_of_com > 2:
            break
        else:
            print("must more than 2")
            
    play({},com_input(select_amount_of_com))

