import csv
import random

def menu():
    '''Menu for Pokedex'''
    # printing out all the options
    print("\nPokemon Super Search Engine")
    print("1. Display Pokemon with their types and statistics")
    print("2. Display the first Pokemon of a Type of your choice")
    print("3. Display all Pokemons with Total Base stat of your choice")
    print("4. Display all Pokemon with a minimum set of stats")
    print("5. Display all legendary Pokemons of specific Type1 and Type2")
    print("6. Display all caught Pokemon")
    print("0. Quit\n")

def check(num,low_limit=0,upper_limit=6):
    '''Validation for numbers between a specified range. If range not specified, default is 0 and 6 which is used for checking the range for the option variable'''
    if num.isdigit() == False: #checking if num is not a number
        return True
    # when adding more stuff to the Pokedex change the end range
    elif int(num) < low_limit or int(num) > upper_limit: # checking if choice is not in the range of 0 to 5 
        return True
    return False
    
def check_stat(stat):
    '''Validation of the stats like special attack, special defence, speed and total base stat'''
    if stat.isdigit() == False: # checking is stat is not a number
        return True
    elif int(stat) < 0: # checking if stat is negative
        return True
    return False

def print_df_left_aligned(pokemons,max_lengths):
    '''Formatting of output'''
    for i in range(len(pokemons)):
        for j in range(len(pokemons[i])):
            print(f"{pokemons[i][j]:<{max_lengths[j] + 3}}",end="") # iterating through each element in the 2D list and adding spaces
        print()

def choice1(pokemons,caught_df,weights): 
    '''Takes in the number of pokemon to be displayed and outputs only that number of pokemon'''
    num_of_pokemon = input("\nEnter number of pokemon to be displayed: ")
    # validating input
    while check(num_of_pokemon,low_limit=0,upper_limit=800):
        if num_of_pokemon.isdigit() == False:
            print("\nInvalid Input! Re-enter number of pokemon to be displayed.")
            num_of_pokemon = input("\nEnter number of pokemon to be displayed: ")
        elif int(num_of_pokemon) < 0:
            print("\nInvalid Input! Re-enter number of pokemon to be displayed.")
            num_of_pokemon = input("\nEnter number of pokemon to be displayed: ")
        else:
            print("\nPokedex does not contain that many pokemons. Re-enter number of pokemon to be displayed.")
            num_of_pokemon = input("\nEnter number of pokemon to be displayed: ")
    num_of_pokemon = int(num_of_pokemon)
    new_pokemons = [] # new list to keep track of pokemons that meet the criteria
    for i in range(num_of_pokemon + 1):
        new_pokemons.append(pokemons[i]) # appending to new list
    print_df_left_aligned(new_pokemons,max_lengths) #outputting answer using the left aligned function
    if random.randint(1,10) == 3: # check if pokemon appears
        pokemon_appear(pokemons,caught_df,weights)
    # showing menu and asking for choice again
    menu()
    choice = input("Enter option: ")
    return choice

def choice2(pokemons,caught_df,weights): 
    '''Takes in a type of pokemon and outputs the first instance of a pokemon of that type'''
    type = input("\nEnter Type: ").lower()
    # Validating input
    while type.isalpha() == False:
        print("\nInvalid Input! Re-enter the Type of Pokemon")
        type = input("\nEnter Type: ").lower()
    # filtering the data frame according to our needs
    new_pokemons = [pokemons[0]] # new list to keep track of pokemons that meet the criteria containing the header
    for i in range(1,len(pokemons)):
        if pokemons[i][2].lower() == type or pokemons[i][3].lower() == type: # checking each pokemon whether they meet the criteria
            new_pokemons.append(pokemons[i]) # appending to new list if criteria is met
            break
    # checking if filtered dataframe is empty or not
    if len(new_pokemons) > 1:
        print_df_left_aligned(new_pokemons,max_lengths) # outputting the filtered dataframe using left align function
    else:
        print("No Pokemon of this type.")
    if random.randint(1,10) == 3: # check if pokemon appears
        pokemon_appear(pokemons,caught_df,weights)
    # showing menu and asking for choice again
    menu()
    choice = input("Enter option: ")
    return choice

def choice3(pokemons,caught_df,weights): 
    '''Takes in the total base stat and outputs all pokemon with that total base stat'''
    total_base_stat = input("\nEnter Total Base Stat: ").lower()
    # Validating input
    while check_stat(total_base_stat):
        if total_base_stat.isdigit() == False:
            print("\nInvalid Input! Re-enter Total Base Stat")
            total_base_stat = input("\nEnter Total Base Stat: ").lower()
        else:
            print("Total Base Stat must be greater than 0! Re-enter Total Base Stat")
            total_base_stat = input("\nEnter Total Base Stat: ").lower()
    total_base_stat = int(total_base_stat)
    # filtering the data frame according to our needs
    new_pokemons = [pokemons[0]] # new list to keep track of pokemons that meet the criteria containing the header
    for i in range(1,len(pokemons)):
        if int(pokemons[i][4]) == total_base_stat: # checking each pokemon if they meet the critera
            new_pokemons.append(pokemons[i]) # appending to new list if criteria is met
    # checking if filtered dataframe is empty or not
    if len(new_pokemons) > 1:
        print_df_left_aligned(new_pokemons,max_lengths) # outputting the filtered dataframe using left align function
    else:
        print("No Pokemon with this Total Base Stat")
    if random.randint(1,10) == 3: # check if pokemon appears
        pokemon_appear(pokemons,caught_df,weights)
    # showing menu and asking for choice again
    menu()
    choice = input("Enter option: ")
    return choice

def choice4(pokemons,caught_df,weights): 
    '''Takes in 3 variables special attack, special defence and speed and outputs all the pokemon that have at least those stats or better'''
    attack = input("\nEnter min Special Attack Stat: ")
    # Validating input 1
    while check_stat(attack):
        if attack.isdigit() == False:
            print("\nInvalid Input! Re-enter Special Attack Stat")
            attack = input("\nEnter min special attack stat: ")
        else:
            print("Special Attack Stat must be greater than 0! Re-enter Special Attack Stat")
            attack = input("\nEnter min Special Attack stat: ")
    attack = int(attack)
    defence = input("Enter min Special Defence Stat: ")
    # Validating input 2
    while check_stat(defence):
        if defence.isdigit() == False:
            print("\nInvalid Input! Re-enter Special Defence Stat")
            defence = input("\nEnter min Special Defence stat: ")
        else:
            print("Special Defence Stat must be greater than 0! Re-enter Special Defence Stat")
            defence = input("\nEnter min Special defence stat: ")
    defence = int(defence)
    speed = input("Enter min Speed Stat: ")
    # Validating input 3
    while check_stat(speed):
        if speed.isdigit() == False:
            print("\nInvalid Input! Re-enter Special Speed Stat")
            speed = input("\nEnter min Special Speed stat: ")
        else:
            print("Special Speed Stat must be greater than 0! Re-enter Special Speed Stat")
            speed = input("\nEnter min Special Speed stat: ")
    speed = int(speed)
    # filtering the data frame according to our needs
    new_pokemons = [pokemons[0]] # new list to keep track of pokemons that meet the criteria containing the header
    for i in range(1,len(pokemons)):
        # checking each pokemon if they meet the criteria
        if int(pokemons[i][8]) >= attack and int(pokemons[i][9]) >= defence and int(pokemons[i][10]) >= speed:
            new_pokemons.append(pokemons[i]) # appending to new list if criteria is met
    # checking if filtered dataframe is empty or not
    if len(new_pokemons) > 1:
        print_df_left_aligned(new_pokemons,max_lengths) # outputting filtered dataframe using left align function
    else:
        print("No Pokemon has such powerful stats")
    if random.randint(1,10) == 3: # check if pokemon appears
        pokemon_appear(pokemons,caught_df,weights)
    # showing menu and asking for choice again
    menu()
    choice = input("Enter option: ")
    return choice

def choice5(pokemons,caught_df,weights):
    '''Takes in 2 types and outputs all legendaries with those 2 types'''
    type1 = input("\nEnter Type1: ").lower()
    # Validating input 1
    while type1.isalpha() == False:
        print("\nInvalid Input! Re-enter Type1")
        type1 = input("\nEnter Type1: ").lower()
    type2 = input("Enter Type2: ").lower()
    # Validating input 2
    while type2.isalpha() == False:
        print("\nInvalid Input! Re-enter Type2")
        type2 = input("\nEnter Type2: ").lower()
    # filtering the data frame according to our needs
    new_pokemons = [pokemons[0]] # new list to keep track of pokemons that meet the criteria containing the header
    for i in range(1,len(pokemons)):
        # checking each pokemon if they meet the critera
        ## After looking at remarks from Poh Siang, i need to change the line to this:
        # if pokemons[i][12] == "TRUE" and (pokemons[i][2].lower() == type1 and pokemons[i][3].lower() == type2) or (pokemons[i][2].lower() == type2 and pokemons[i][3].lower() == type1)
        if pokemons[i][12] == "TRUE" and pokemons[i][2].lower() == type1 and pokemons[i][3].lower() == type2: 
            new_pokemons.append(pokemons[i]) # appending to new list if criteria is met
    
    # checking if filtered dataframe is empty or not
    if len(new_pokemons) > 1:
        print_df_left_aligned(new_pokemons,max_lengths) # outputting filtered dataframe using left align function
    else:
        print("No such legendary Pokemon.")
    if random.randint(1,10) == 3: # check if pokemon appears
        pokemon_appear(pokemons,caught_df,weights)
    # showing menu and asking for choice again
    menu()
    choice = input("Enter option: ")
    return choice

def choice6(pokemons,caught_df,weights):
    '''Printing caught Pokemon'''
    print()
    if len(caught_df) > 1: # checking if caught pokemon data frame is empty or not
        print_df_left_aligned(caught_df,max_lengths) #outputting caught pokemon
    else:
        print("No caught Pokemon!")
    # showing menu and asking for choice again
    if random.randint(1,10) == 3: # check if pokemon appears
        pokemon_appear(pokemons,caught_df,weights)
    menu()
    choice = input("Enter option: ")
    return choice

def catch_pokemon(pokemon_details,upper_limit,caught_df):
    catch_num = random.randint(1,upper_limit) # random number
    pokeball = input(f"Enter a number between 1 and {upper_limit} to try and catch the pokemon: ")
    # validating input
    while check(pokeball,1,upper_limit):
        print("Invalid Input! Re-enter your number to catch the pokemon")
        pokeball = input(f"Enter a number between 1 and {upper_limit} to try and catch the pokemon: ")
    if int(pokeball) == catch_num: # caught pokemon 
        print(f"\nCongratulations, You just caught a {pokemon_details[1]}!")
        caught_df.append(pokemon_details) # inserting new row
    else:
        print("\nBetter luck next time!")
    return caught_df

def pokemon_appear(pokemons,caught_df,weights):
    # using weights made previously to pick a random pokemon
    pokemon = random.choices([x for x in range(0,800)],weights=weights,k=1)[0]
    pokemon_details = pokemons[pokemon] # getting detials of pokemon
    weight = weights[pokemon] # weight of pokemon
    print(f"\nYou encounter a wild {pokemon_details[1]}!")
    # call function catch_pokemon based on weight
    if weight <= 20:
        caught_df = catch_pokemon(pokemon_details,20,caught_df)
    if weight <= 40:
        caught_df = catch_pokemon(pokemon_details,10,caught_df)
    else:
        caught_df = catch_pokemon(pokemon_details,5,caught_df)

pokemons = [] # list to keep track of pokemons
# reading data from csv file
with open("Pokemon.csv","r") as file:
    reader = csv.reader(file) # read data in csv file
    for i in reader: # iteratre through each line and append it to pokemons list giving us a 2D list
        pokemons.append(i)
max_lengths = [0] * len(pokemons[0]) # list to check for the max length in each column
for i in range(len(pokemons)):
    for j in range(len(pokemons[i])):
        # iterating through each element in the 2D list
        if len(pokemons[i][j]) > max_lengths[j]: # checking if element lenght is more than max length for that column
            max_lengths[j] = int(len(pokemons[i][j])) # updating max length if true
caught_df = [pokemons[0]] # creating new list for caught pokemon
weights = [] # creating list for weights for each pokemon, lower weight for higher stats pokemon and vice versa
for row in pokemons[1:]: # weight calculation
    if row[2] != "" and row[3] != "" and row[12] == "TRUE":
        weights.append(10)
    elif row[12] == "TRUE":
        weights.append(20)
    elif int(row[4]) >= 600 or int(row[5]) >= 200 or int(row[6]) >= 150 or int(row[7]) >= 180 or int(row[8]) >= 160 or int(row[9]) >= 180 or int(row[10]) >= 150:
        weights.append(30)
    elif int(row[4]) >= 450 or int(row[5]) >= 150 or int(row[6]) >= 100 or int(row[7]) >= 100 or int(row[8]) >= 110 or int(row[9]) >= 110 or int(row[10]) >= 90:
        weights.append(40)
    elif int(row[4]) >= 250 or int(row[5]) >= 80 or int(row[6] )>= 50 or int(row[7]) >= 50 or int(row[8]) >= 60 or int(row[9]) >= 60 or int(row[10]) >= 40:
        weights.append(50)
    else:
        weights.append(70)
weights = tuple(weights) # making weight tuple
# displaying menu and taking input for the option
menu()
choice = input("Enter option: ")
while choice != "0": # checking if choice is 0 or not and loop accordingly
    while check(choice): # Validating choice
        if choice.isdigit() == False:
            print("\nInvalid Input! Re-enter option")
            menu()
            choice = input("Enter option: ")
        else:
            print("\nNot implemented yet? Please choose a valid option.")
            menu()
            choice = input("Enter option: ")
    # checking for chosen option and then calling appropriate function
    if int(choice) == 1:
        choice = choice1(pokemons,caught_df,weights)
    elif int(choice) == 2:
        choice = choice2(pokemons,caught_df,weights)
    elif int(choice) == 3:
        choice = choice3(pokemons,caught_df,weights)
    elif int(choice) == 4:
        choice = choice4(pokemons,caught_df,weights)
    elif int(choice) == 5:
        choice = choice5(pokemons,caught_df,weights)
    elif int(choice) == 6:
        choice = choice6(pokemons,caught_df,weights)
# outputting bye as the final statement
print("\nBye!\n\nThank you for using Pokemon search engine!")