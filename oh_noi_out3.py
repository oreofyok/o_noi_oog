import random

select_amount_of_com = int(input("how many com do you want to play: "))
choices = ["f","b"]

def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key,default_value)

def com_input(x):
    com = {}; com_out = []
    for i in range(1,x+1):
        com[f"com{[i]}"] = random.choice(choices)
        
    for i in com:
        old = i
        new = input(f"define your {i} name: ")
        change_dict_key(com, old, new)
       
    play(com)
    
playing = True
stop = False

def play2(com):
    
    if len(com) == 1:
        rps = True
        while rps == True:
            me = input("r p s: ")
            for i in com:
                c_think = random.choice(["r","p","s"])
                print(i,"choose",c_think)
            if (me == "r" and c_think == "s") or (me == "p" and c_think == "r") or (me == "s" and c_think == "p"):
                print("you win") ; rps = False
            elif (me == "r" and c_think == "p") or (me == "p" and c_think == "s") or (me == "s" and c_think == "r"):
                print(i,": win") ; rps = False
            elif me == c_think:
                print("draw play again.")
        #quit()
        
    elif len(com) == 2:
        cc = {}; rps = True
        while rps == True:
            cc1 = [];cc2 = []
            for i in com:
                cc[i] = random.choice(["r","p","s"])
                cc1.append(i) ; cc2.append(cc[i])
            print(cc) ; print(cc2[0],cc2[1])
            if (cc2[0] == "r" and cc2[1] == "s") or (cc2[0] == "p" and cc2[1] == "r") or (cc2[0] == "s" and cc2[1] == "p"):
                print(cc1[0],": win") ; rps = False
            elif (cc2[0] == "r" and cc2[1] == "p") or (cc2[0] == "p" and cc2[1] == "s") or (cc2[0] == "s" and cc2[1] == "r"):  
                print(cc1[1],": win") ; rps = False
            elif cc2[0] == cc2[1]:
                print('draw try again.')

def play(com):
    global playing;global stop
    
    while stop != True:
    
        if com != None:
            for i in com.keys():
                com[i] = random.choice(choices)
        
        print()
        count_f = 0 ; count_b = 0
        
        
        player = " "
        
        
        com_out = []
        play_ground = []

        
        if com != None: 
            for i in com:
                if com[i] == "f":
                    count_f += 1
                elif com[i] == "b":
                    count_b += 1
        
        if count_b + count_f > 2 and playing == False or count_b + count_f > 1 and playing != False :
            print("com =",com)
        else:
            if count_b + count_f == 2 and playing == False:
                c = []
                for i in com:
                    c.append(i)
                print("only",c[0],"and",c[1],"left")
            elif count_b + count_f == 1 and playing != False:
                for i in com:
                    print("only you and",i,"left")
            
        if playing == True and stop != True and len(com) > 1:
            player = input("choose f or b: ")
            
        if player == "f":
            count_f += 1
        elif player == "b":
            count_b += 1

        if count_b + count_f == 1 and playing == True:
            c = []
            for i in com:
                print(f"you and {i} go to r p and s")
                c.append(i)
            stop = True
            play2(c)
        elif count_b + count_f == 2 and playing == False:
            c = []
            for i in com:
                c.append(i)
            
            print(f"{c[0]} and {c[1]} go to r p and s")
            stop = True
            play2(c)
        else:
            if count_f == count_b and count_f > 1 :
                print("draw")
                
            elif count_f == 0 or count_b == 0:
                print("draw")
                
            elif count_f > count_b:
                if player == "b":
                    print("You win ,outed.")
                    print()
                    playing = False
                    #play(com)
                elif player == "f":
                    print("Go to next round.")
                    #play(com)
                
                if com!= None:
                    for i in com:
                        if com[i] == "b":
                            com_out.append(i)
                    
                    
            elif count_f < count_b:
                if player == "b":
                    print("Go to next round.")
                    
                elif player == "f":
                    print("You win,outed")
                    playing = False
                    
                
                if com != None:
                    for i in com:
                        if com[i] == "f":
                            com_out.append(i)
                    
            
            print("com out =",com_out)
            
            if com != None:
                for i in com_out:
                    if i in com.keys():
                        del com[i]
            
        if stop != True:
            play(com)
        
play(com_input(select_amount_of_com))




