import random

def start_rule_ask(start_rules):
    if (start_rules == "START"):
        symbol_ask()
    elif (start_rules == "RULES"):
        rules_tutorial()
    else:
        print("\n\t\tIt seems that you have not entered one of the two options presented.")
        start_rules = input("\t\tPlease enter either \"START\" OR \"RULES\" depending on your preferred next step: ")
        start_rule_ask(start_rules)

def rules_tutorial():
    print("\n\n\t\t\t\tRules Tutorial:")
    print("\nThe rules of Tic-Tac-Toe are rather simple. The goal is to make a straight line out of three symbols in a row.")
    print("You, the player, will either choose to take the first turn or the second, or have the turn order randomly selected.")
    print("After this you and the program will alternate placing symbols on a 3x3 grid.")
    print("The first one to create a straight line of three symbols in the grid wins!")
    print("Each space will correspont to a number-letter coordinate pair.")
    print("\nHere is what the game board will look like\n")
    print("\t\t\t\t\t\t    1      2     3 \n")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\tA       #     #     ")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\t   #################")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\tB       #     #     ")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\t   #################")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\tC       #     #     ")
    print("\t\t\t\t\t\t        #     #     ")
    print("\nFor example, if the player wished to place their symbol in the center box, they would enter \"B2\".)")
    print("Remember to enter first the letter, then the number, in the same way that you do in the popular game Battleship!")
    ready_to_play = input("\nWhen you are ready to play, click enter: ")
    symbol_ask()

def symbol_picker_x():
    global variable_x
    variable_x = input("\n\t\t\t\tPlease enter the symbol to use for X: ")
    if (len(variable_x) != 1):
        print("\nPlease enter exactly one (1) character to use for the symbol.")
        symbol_picker_x()
    elif (variable_x == "X"):
        print("Now why exactly would you go through all that trouble just to do that? Ok then...")
        return variable_x
    else:
        return variable_x


def symbol_picker_o():
    global variable_o
    variable_o = input("\n\t\t\t\tPlease enter the symbol to use for O: ")
    if (len(variable_o) != 1):
        print("\nPlease enter exactly one (1) character to use for the symbol.")
        symbol_picker_o()
    elif (variable_o == "O" and variable_x == "X"):
        print("Well now you're just being cheeky.")
        return variable_o
    else:
        return variable_o
 
def symbol_w_redo():
    global variable_x
    global variable_o
    variable_x = symbol_picker_x()
    variable_o = symbol_picker_o()
    print(f"\n\t\t\t\tYour chosen variables are {variable_x} and {variable_o}.")
    redo_ask = input("If you are happy with these selections, click enter to continue, if not enter \"REDO\": ")
    if (redo_ask == "REDO"):
        symbol_w_redo()

def win_sequence(win_binary):
    global turn_num
    global variable_x
    global variable_o
    global user_var
    global comp_var
    global var_a1
    global var_a2
    global var_a3
    global var_b1
    global var_b2
    global var_b3
    global var_c1
    global var_c2
    global var_c3
    global line_1
    global line_2
    global line_3
    global line_4
    global line_5
    global line_6
    global line_7
    global line_8
    global line_9
    global line_10
    global line_11
    global line_12
    if (win_binary == 1):
        print("\n\t\t\t\tYou win! Congradulations!")
    elif (win_binary == 2):
        print("\n\t\t\t\tThe computer wins.")
    else:
        print("\n\t\t\t\tThe game is a tie, give it another try!")
    again_ask = input("\n\t\t\t\tIf you wish to play again, type \"AGAIN\": ")
    if (again_ask == "AGAIN"):
        turn_num = 0
        variable_x = "X"
        variable_o = "O"
        user_var = ""
        comp_var = ""
        win_binary = 0
        var_a1 = " "
        var_a2 = " "
        var_a3 = " "
        var_b1 = " "
        var_b2 = " "
        var_b3 = " "
        var_c1 = " "
        var_c2 = " "
        var_c3 = " "
        line_1 = str(f"\t\t\t\t\t\t     1     2     3 \n")
        line_2 = str(f"\t\t\t\t\t\t        #     #     ")
        line_3 = str(f"\t\t\t\t\t\tA    {var_a1}  #  {var_a2}  #  {var_a3}  ")
        line_4 = str(f"\t\t\t\t\t\t        #     #     ")
        line_5 = str(f"\t\t\t\t\t\t   #################")
        line_6 = str(f"\t\t\t\t\t\t        #     #     ")
        line_7 = str(f"\t\t\t\t\t\tB    {var_b1}  #  {var_b2}  #  {var_b3}  ")
        line_8 = str(f"\t\t\t\t\t\t        #     #     ")
        line_9 = str(f"\t\t\t\t\t\t   #################")
        line_10 = str(f"\t\t\t\t\t\t        #     #     ")
        line_11 = str(f"\t\t\t\t\t\tC    {var_c1}  #  {var_c2}  #  {var_c3}  ")
        line_12 = str(f"\t\t\t\t\t\t        #     #     ")
        symbol_ask()

def turn_generator():
    global turn_num
    global user_var
    global comp_var
    global var_a1
    global var_a2
    global var_a3
    global var_b1
    global var_b2
    global var_b3
    global var_c1
    global var_c2
    global var_c3
    global line_1
    global line_2
    global line_3
    global line_4
    global line_5
    global line_6
    global line_7
    global line_8
    global line_9
    global line_10
    global line_11
    global line_12
    while (turn_num <= 9):
        if ((turn_num % 2) == 0):
            
            #User Win Matrix
            if (var_a1 == user_var and var_a2 == user_var and var_a3 == user_var):
                win_sequence(1)
            elif (var_a1 == user_var and var_b2 == user_var and var_c3 == user_var):
                win_sequence(1)
            elif (var_a1 == user_var and var_b1 == user_var and var_c1 == user_var):
                win_sequence(1)
            elif (var_a2 == user_var and var_b2 == user_var and var_c2 == user_var):
                win_sequence(1)
            elif (var_a3 == user_var and var_b3 == user_var and var_c3 == user_var):
                win_sequence(1)
            elif (var_a3 == user_var and var_b2 == user_var and var_c1 == user_var):
                win_sequence(1)
            elif (var_b1 == user_var and var_b2 == user_var and var_b3 == user_var):
                win_sequence(1)
            elif (var_c1 == user_var and var_c2 == user_var and var_c3 == user_var):
                win_sequence(1)
            
            #Computer Move Matrix
            comp_string = ""
            if (var_a1 != user_var):
                  comp_string += "1,"
            if (var_a2 != user_var):
                  comp_string += "2,"
            if (var_a3 != user_var):
                  comp_string += "3,"
            if (var_b1 != user_var):
                  comp_string += "4,"
            if (var_b2 != user_var):
                  comp_string += "5,"
            if (var_b3 != user_var):
                  comp_string += "6,"
            if (var_c1 != user_var):
                  comp_string += "7,"
            if (var_c2 != user_var):
                  comp_string += "8,"
            if (var_c3 != user_var):
                  comp_string += "9,"

            number_roll = -1
            while (number_roll == -1):
                maybe_num = str(random.randint(1, 9))
                find_maybe = comp_string.find(maybe_num)
                if (find_maybe  == -1):
                    number_roll = -1
                else:
                    number_roll = maybe_num
            number_roll = int(number_roll)

            if (number_roll == 1):
                var_a1 = comp_var
            elif (number_roll == 2):
                var_a2 = comp_var
            elif (number_roll == 3):
                var_a3 = comp_var
            elif (number_roll == 4):
                var_b1 = comp_var
            elif (number_roll == 5):
                var_b2 = comp_var
            elif (number_roll == 6):
                var_b3 = comp_var
            elif (number_roll == 7):
                var_c1 = comp_var
            elif (number_roll == 8):
                var_c2 = comp_var
            elif (number_roll == 9):
                var_c3 = comp_var

            line_1 = str(f"\t\t\t\t\t\t     1     2     3 \n")
            line_2 = str(f"\t\t\t\t\t\t        #     #     ")
            line_3 = str(f"\t\t\t\t\t\tA    {var_a1}  #  {var_a2}  #  {var_a3}  ")
            line_4 = str(f"\t\t\t\t\t\t        #     #     ")
            line_5 = str(f"\t\t\t\t\t\t   #################")
            line_6 = str(f"\t\t\t\t\t\t        #     #     ")
            line_7 = str(f"\t\t\t\t\t\tB    {var_b1}  #  {var_b2}  #  {var_b3}  ")
            line_8 = str(f"\t\t\t\t\t\t        #     #     ")
            line_9 = str(f"\t\t\t\t\t\t   #################")
            line_10 = str(f"\t\t\t\t\t\t        #     #     ")
            line_11 = str(f"\t\t\t\t\t\tC    {var_c1}  #  {var_c2}  #  {var_c3}  ")
            line_12 = str(f"\t\t\t\t\t\t        #     #     ")
            
            print("\nThe computer makes their move!\n")
            print(line_1)
            print(line_2)
            print(line_3)
            print(line_4)
            print(line_5)
            print(line_6)
            print(line_7)
            print(line_8)
            print(line_9)
            print(line_10)
            print(line_11)
            print(line_12)
            turn_num += 1
            
        
            #Computer Win Matrix
            if (var_a1 == comp_var and var_a2 == comp_var and var_a3 == comp_var):
                win_sequence(2)
            elif (var_a1 == comp_var and var_b2 == comp_var and var_c3 == comp_var):
                win_sequence(2)
            elif (var_a1 == comp_var and var_b1 == comp_var and var_c1 == comp_var):
                win_sequence(2)
            elif (var_a2 == comp_var and var_b2 == comp_var and var_c2 == comp_var):
                win_sequence(2)
            elif (var_a3 == comp_var and var_b3 == comp_var and var_c3 == comp_var):
                win_sequence(2)
            elif (var_a3 == comp_var and var_b2 == comp_var and var_c1 == comp_var):
                win_sequence(2)
            elif (var_b1 == comp_var and var_b2 == comp_var and var_b3 == comp_var):
                win_sequence(2)
            elif (var_c1 == comp_var and var_c2 == comp_var and var_c3 == comp_var):
                win_sequence(2)
            turn_num + 1
        else:
            coordinate = input("\nEnter the coordinates of the space that you would like to mark: ")
            if (len(coordinate) != 2):
                print("\nPlease enter exactly two (2) characters corresponding to the box that you desire to fill.")
                turn_generator()
            first_coor = coordinate[0]
            second_coor = coordinate[1]
            if (first_coor != "A" and first_coor != "B" and first_coor != "C"):
                print("\nPlease only enter letter values of \"A\" or \"B\" or \"C\".")
                print("Also, make sure that you type the letter first, then the number (e.g. 3B).")
            elif (second_coor != "1" and second_coor != "2" and second_coor != "3"):
                print("\nPlease only enter number values of \"1\" or \"2\" or \"3\".")
                print("Also, make sure that you type the letter first, then the number (e.g. 3B).")
            if(first_coor == "A"):
                if (second_coor == "1"):
                    var_a1 = str(f"{user_var}")
                elif (second_coor == "2"):
                    var_a2 = str(f"{user_var}")
                else:
                    var_a3 = str(f"{user_var}")
            elif(first_coor == "B"):
                if (second_coor == "1"):
                    var_b1 = str(f"{user_var}")
                elif (second_coor == "2"):
                    var_b2 = str(f"{user_var}")
                else:
                    var_b3 = str(f"{user_var}") 
            else:
                if (second_coor == "1"):
                    var_c1 = str(f"{user_var}")
                elif (second_coor == "2"):
                    var_c2 = str(f"{user_var}")
                else:
                    var_c3 = str(f"{user_var}")
                    
            line_1 = str(f"\t\t\t\t\t\t     1     2     3 \n")
            line_2 = str(f"\t\t\t\t\t\t        #     #     ")
            line_3 = str(f"\t\t\t\t\t\tA    {var_a1}  #  {var_a2}  #  {var_a3}  ")
            line_4 = str(f"\t\t\t\t\t\t        #     #     ")
            line_5 = str(f"\t\t\t\t\t\t   #################")
            line_6 = str(f"\t\t\t\t\t\t        #     #     ")
            line_7 = str(f"\t\t\t\t\t\tB    {var_b1}  #  {var_b2}  #  {var_b3}  ")
            line_8 = str(f"\t\t\t\t\t\t        #     #     ")
            line_9 = str(f"\t\t\t\t\t\t   #################")
            line_10 = str(f"\t\t\t\t\t\t        #     #     ")
            line_11 = str(f"\t\t\t\t\t\tC    {var_c1}  #  {var_c2}  #  {var_c3}  ")
            line_12 = str(f"\t\t\t\t\t\t        #     #     ")
            
            print("\nThe board now displays:\n")
            print(line_1)
            print(line_2)
            print(line_3)
            print(line_4)
            print(line_5)
            print(line_6)
            print(line_7)
            print(line_8)
            print(line_9)
            print(line_10)
            print(line_11)
            print(line_12)
            turn_num += 1
    win_sequence(3)

def x_or_o():
    global variable_x
    global variable_o
    global user_var
    global comp_var
    print(f"\nDo you wish to play with {variable_x}'s or {variable_o}'s?")
    x_or_o_ask = input(f"Enter \"{variable_x}\" or \"{variable_o}\": ")
    if (x_or_o_ask == variable_x):
        user_var = variable_x
        comp_var = variable_o
    elif (x_or_o_ask == variable_o):
        user_var = variable_o
        comp_var = variable_x
    else:
        print("Please enter either \"{variable_x}\" or \"variable_o}\".")
        x_or_o()

def game():
    global variable_x
    global variable_o
    global turn_num
    print("\nIf you want to go first, enter \"FIRST\".")
    print("If you want the program to go first, enter \"SECOND\".")
    first_turn_ask = input("If you this to be randomized, enter \"RANDOM\": ")
    if (first_turn_ask == "FIRST"):
        turn_num = 1
    elif (first_turn_ask == "SECOND"):
        turn_num = 2
    elif (first_turn_ask == "RANDOM"):
        turn_num = random.randint(1, 2)
    else:
        print("Please enter one of the options listed above.")
        game()
    x_or_o()
    print("\nHere is the game board!\n")
    print("\t\t\t\t\t\t     1     2     3 \n")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\tA       #     #     ")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\t   #################")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\tB       #     #     ")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\t   #################")
    print("\t\t\t\t\t\t        #     #     ")
    print("\t\t\t\t\t\tC       #     #     ")
    print("\t\t\t\t\t\t        #     #     ")
    turn_generator()
            

def symbol_ask():
    print("\nDo you wish to choose customized symbols or use the default \"X\" and \"O\"?")
    custom_ask = input("If you wish to choose customized symbols, enter \"CUSTOM\". Otherwise, click enter to continue: ")
    if (custom_ask == "CUSTOM"):
        symbol_w_redo()
        game()
    elif (custom_ask == ""):
        game()
    else:
        print("\nPlease either hit enter or type CUSTOM if you wish to create custom symbols for this game: ")
        symbol_ask()

turn_num = 0    

variable_x = "X"
variable_o = "O"
user_var = ""
comp_var = ""
win_binary = 0

var_a1 = " "
var_a2 = " "
var_a3 = " "
var_b1 = " "
var_b2 = " "
var_b3 = " "
var_c1 = " "
var_c2 = " "
var_c3 = " "

line_1 = str(f"\t\t\t\t\t\t     1     2     3 \n")
line_2 = str(f"\t\t\t\t\t\t        #     #     ")
line_3 = str(f"\t\t\t\t\t\tA    {var_a1}  #  {var_a2}  #  {var_a3}  ")
line_4 = str(f"\t\t\t\t\t\t        #     #     ")
line_5 = str(f"\t\t\t\t\t\t   #################")
line_6 = str(f"\t\t\t\t\t\t        #     #     ")
line_7 = str(f"\t\t\t\t\t\tB    {var_b1}  #  {var_b2}  #  {var_b3}  ")
line_8 = str(f"\t\t\t\t\t\t        #     #     ")
line_9 = str(f"\t\t\t\t\t\t   #################")
line_10 = str(f"\t\t\t\t\t\t        #     #     ")
line_11 = str(f"\t\t\t\t\t\tC    {var_c1}  #  {var_c2}  #  {var_c3}  ")
line_12 = str(f"\t\t\t\t\t\t        #     #     ")

print("\t\t\t\tWelcome to virtual Tic-Tac-Toe!")
print("\nIf you are familiar with the rules for this game, please enter \"START\".")
print("If you would like a quick explaination of the rules for this game, please enter \"RULES\".")

start_rules = input("\n\t\t\t\tHow would you like to proceed? : ")

start_rule_ask(start_rules)
