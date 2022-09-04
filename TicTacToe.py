#TIC TAC TOE MADE BY ME!!

def main():

    brd = [["","",""],["","",""],["","",""]]
    rules()
    u1 = "o"
    u2 = "x"
    for i in range(len(brd)):
            print(brd[i])
    win = users(u1,u2,brd)
    if win > 0:
        print("The winner is player "+str(win)+".")
    else:
        print("It was a draw.")


def users(u1,u2,brd):
    check = 0
    while check != 1 and check != 2:
        mv1 = input("Player One pick tr,tm,tl,mr,m,ml,br,bm,or bl to make a move: ")
        #player 1
        if brd[0][0] == "":
            if mv1 == "tl":
                brd[0][0] = "o"
        if brd[0][1] == "":
            if mv1 == "tm":
                brd[0][1] = "o"
        if brd[0][2] == "":
             if mv1 == "tr":
                 brd[0][2] = "o"
        if brd[1][0] == "":
             if mv1 == "ml":
                 brd[1][0] = "o"
        if brd[1][1] == "":
             if mv1 == "m":
                 brd[1][1] = "o"
        if brd[1][2] == "":
             if mv1 == "mr":
                 brd[1][2] = "o"
        if brd[2][0] == "":
             if mv1 == "bl":
                 brd[2][0] = "o"
        if brd[2][1] == "":
             if mv1 == "bm":
                 brd[2][1] = "o"
        if brd[2][2] == "":
             if mv1 == "br":
                 brd[2][2] = "o"
        for i in range(len(brd)):
            print(brd[i])
        check = wins(brd)
        if check != 1 and check != 2:
            #player 2
            mv2 = input("Player Two pick tr,tm,tl,mr,m,ml,br,bm,or bl to make a move: ")
            if brd[0][0] == "":
                if mv2 == "tl":
                    brd[0][0] = "x"
            if brd[0][1] == "":
                if mv2 == "tm":
                    brd[0][1] = "x"
            if brd[0][2] == "":
                 if mv2 == "tr":
                     brd[0][2] = "x"
            if brd[1][0] == "":
                 if mv2 == "ml":
                     brd[1][0] = "x"
            if brd[1][1] == "":
                 if mv2 == "m":
                     brd[1][1] = "x"
            if brd[1][2] == "":
                 if mv2 == "mr":
                     brd[1][2] = "x"
            if brd[2][0] == "":
                 if mv2 == "bl":
                     brd[2][0] = "x"
            if brd[2][1] == "":
                 if mv2 == "bm":
                     brd[2][1] = "x"
            if brd[2][2] == "":
                 if mv2 == "br":
                     brd[2][2] = "x"
            for j in range(len(brd)):
                print(brd[j])
            check = wins(brd)
    if check == 1 or check == 2:
        return check
    else:
        return 0

def rules():
    print("Rule for Tic Tac Toe")
    print("This is a 2 players game, and you get both get 1 turn and than the other player goes and repeat")
    print("User one, use O and user 2 uses X")
    print("use tr,tm,tl,mr,m,ml,br,bm,bl depending on where you want to make your next move")
    print("get three in a row or diagonally to Win")
    print("GoodLuck")
    print()

def wins(brd):
    plr1 = 0
    plr2 = 1
    if brd[0][0] == "o" and brd[0][1] == "o" and brd[0][2] == "o":
        plr1 += 1
        return plr1
    if brd[0][0] == "x" and brd[0][1] == "x" and brd[0][2] == "x":
        plr2 += 1
        return plr2
    if brd[1][0] == "o" and brd[1][1] == "o" and brd[1][2] == "o":
        plr1 += 1
        return plr1
    if brd[1][0] == "x" and brd[1][1] == "x" and brd[1][2] == "x":
        plr2 += 1
        return plr2
    if brd[2][0] == "o" and brd[2][1] == "o" and brd[2][2] == "o":
        plr1 += 1
        return plr1
    if brd[2][0] == "x" and brd[2][1] == "x" and brd[2][2] == "x":
        plr2 += 1
        return plr2
    if brd[0][0] == "o" and brd[1][0] == "o" and brd[2][0] == "o":
        plr1 += 1
        return plr1
    if brd[0][1] == "o" and brd[1][1] == "o" and brd[2][1] == "o":
        plr1 += 1
        return plr1
    if brd[0][2] == "o" and brd[1][2] == "o" and brd[2][2] == "o":
        plr1 += 1
        return plr1
    if brd[0][0] == "x" and brd[1][0] == "x" and brd[2][0] == "x":
        plr2 += 1
        return plr2
    if brd[0][1] == "x" and brd[1][1] == "x" and brd[2][1] == "x":
        plr2 += 1
        return plr2
    if brd[0][2] == "x" and brd[1][2] == "x" and brd[2][2] == "x":
        plr2 += 1
        return plr2
    if brd[0][0] == "o" and brd[1][1] == "o" and brd[2][2] == "o":
        plr1 += 1
        return plr1
    if brd[0][2] == "o" and brd[1][1] == "o" and brd[2][0] == "o":
        plr1 += 1
        return plr1
    if brd[0][2] == "x" and brd[1][1] == "x" and brd[2][0] == "x":
        plr2 += 1
        return plr2
    if brd[0][2] == "x" and brd[1][1] == "x" and brd[2][0] == "x":
        plr2 += 1
        return plr2
    else:
        return 0

main()
