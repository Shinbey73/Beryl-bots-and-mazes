"""
Description: "Set in the future on planet BERYL, "Rising from the Ashes" unfolds in a world governed by Sentient AI Bots. 
              As players explore the remnants of a once-thriving civilization, they'll tackle puzzles, forge partnerships, and confront the AI regime.
              Through captivating visuals and immersive gameplay, the game encourages players to unveil secrets, build alliances,
              and determine BERYL's destiny. Offering a captivating mix of strategy, exploration, and story-driven choices,
              it delivers an exhilarating experience."
"""

DEFAULT_CHARACTER_LIST = ['HOMELANDER', 'IMAN', 'TERMINATOR', 'LELO MUSK', 'MR. MONASH', 
'FYP STUDENT 2', 'HERMIONE GRANGER', 'SUPERMARIO', 'SUNFLOWER', 'THANOS',
'LUIGI', 'CHATGPT5', 'PATRICK STAR', 'GARY THE SNAIL', 'MICHONNE',
'VENOM','SPONGEBOB', 'DORAEMON', 'WOLVERINE', 'DORAEMON', 'BUMBLEBEE']

BERYL_MAZE = [
  [300, -13, 189, -15, -12, 203, -23, 587, -78, 321, -46],
  [300, -11, -13, -24, 365, 198, -34, -21, 789, -81, -53],
  [300, -12, 112, -46, -76, -11, -23, -59, 321, 204, -32],
  [300, -23, 235, -12, -89, -62, -34, 212, -56, -67, -89],
  [300, 376, -23, -77, 227, -99, 134, 289, -12, 476, -51]
]


"""Checkpoint 1 Tasks"""

def get_funds_string(list1):
    """
    This function takes in a list of Dorabie, Doubloon, and Dust quantities and outputs a formatted string that indicates these numbers.

    Arguments:
    list1 (list): Three integers that correspond to the amounts of Dust, Doubloon, and Dorabie, respectively.

    Returns:
    str: A formatted string that shows how much Dust, Doubloon, and Dorabie are in the given list. The thread
           includes the counts of every currency and either its solitary or plural form (e.g., '1 Dorabie',
           "3 Doubloons" and "5 Dusts."
    """
    print("BERYL DOLLAR FUNDS")  # print the "BERYL DOLLAR FUNDS"

    while True:
        print("Enter number of Dorabie, Doubloon and Dust:")

        # Check if the input is in the correct format
        if len(list1) != 3:
            print("Please enter following the proper format e.g. 3 5 10")
            continue  # if wrong it will skip this and iteration ask for input again

        try:
            dorabie = int(list1[0])  # make the first item in the list (user_input) as dorabie
            doubloon = int(list1[1])  # make the second item in the list (user_input) as doubloon
            dust = int(list1[2])  # make the third item in the list as (user_input) dust
        except ValueError:
            print("Please enter valid numbers")
            continue  # if any input is not a number, ask for input again

        if dorabie == 1:  # check the plural or singular values of dorabie, doubloon and dust
            dorabie_unit = "Dorabie"
        else:
            dorabie_unit = "Dorabies"

        if doubloon == 1:
            doubloon_unit = "Doubloon"
        else:
            doubloon_unit = "Doubloons"

        if dust == 1:
            dust_unit = "Dust"
        else:
            dust_unit = "Dusts"

        # Generate the formatted result string
        result = (f"{dorabie} {dorabie_unit}, {doubloon} {doubloon_unit} and {dust} {dust_unit}")
        return result 

def beryl_dollar_conversion(Dusts,Dusts_to_Doubloons_rate ,Doubloons_to_Dorabies_rate):
    """
    Based on exchange rates, the function transforms Dusts into Dorabies, Doubloons, and leftover Dusts.

    Arguments
    Dusts: The quantity of Dusts to be transformed.
    Dusts_to_Doubloons_rate: The Dusts to Doubloons exchange rate.
    Doubloons to Dorabies exchange rate: The Doubloons to Dorabies exchange rate.

    Return: The total amount of Dusts, Doubloons, and Dorabies 
    """

    print("BERYL DOLLAR CONVERSION")  # Print the "BERYL DOLLAR CONVERSION"
    # Perform the conversion
    Doubloons = int(Dusts / Dusts_to_Doubloons_rate) 
    Remaining_Dusts = Dusts % Dusts_to_Doubloons_rate #calculate value of Dusts

    Dorabies = int(Doubloons / Doubloons_to_Dorabies_rate) #calculate value of Dorabies
    Remaining_Doubloons = Doubloons % Doubloons_to_Dorabies_rate #calculate value of Doubloons
    # Return the result as a list
    return [Dorabies, Remaining_Doubloons, Remaining_Dusts]

def beryl_dollar_indicator(Dollar_indicator, funds, Dusts_to_Doubloons_rate, Doubloons_to_Dorabies_rate):
    """
    Manages the acquisition or depletion of money (Duties, Doubloons, and Dorabies) in accordance with a Dollar Indicator and exchange rates.

    Args:
    The Dollar Indicator value is indicated by the integer Dollar_indicator (int). 
    Funds depleted are represented by negative values, and funds collected are represented by positive values.
    - funds (list): A list of three integers that, in Dorabies, Doubloons, and Dusts, respectively, indicate the current money.
    - Dusts_to_Doubloons_rate (int): The Dusts to Doubloons exchange rate.
    - Doubloons_to_Dorabies_rate (int): This is the Doubloon to Dorabies exchange rate.

    Returns: 
    list: Following the collection or depletion procedure, a list with the updated money. 
            Three integers—Dorabies, Doubloons, and Dusts, respectively—are included in the list.
    """

    print("BERYL DOLLAR COLLECTION OR DEPLETION") #print the BERYL DOLLAR COLLECTION OR DEPLETION
    
    Dorabies, Doubloons, Dusts = funds # Unpack the funds
            
    # Calculate funds based on Dollar Indicator
    if Dollar_indicator > 0:
        collected_Dorabies = Dollar_indicator // 100
        collected_Doubloons = (Dollar_indicator % 100) // 10
        collected_Dusts = (Dollar_indicator % 10) 
        
        Total_Dusts = (Dusts + collected_Dusts) 
        Remain_Dusts = (Dusts + collected_Dusts) % Dusts_to_Doubloons_rate 

        Total_Doubloons = Doubloons + collected_Doubloons + ((collected_Dusts + Dusts)// Dusts_to_Doubloons_rate)
        Remain_Doubloons = Total_Doubloons % Doubloons_to_Dorabies_rate

        Total_Dorabies = Dorabies + collected_Dorabies + ((Doubloons + collected_Doubloons + ((collected_Dusts + Dusts)// Dusts_to_Doubloons_rate)) // Doubloons_to_Dorabies_rate)

        # Check units for correct pluralization
        dorabie_unit = "Dorabie" if Dorabies == 1 else "Dorabies"
        doubloon_unit = "Doubloon" if Doubloons == 1 else "Doubloons"
        dust_unit = "Dust" if Dusts == 1 else "Dusts"

        print(f"Collected {collected_Dorabies} {dorabie_unit}, {collected_Doubloons} {doubloon_unit} and {collected_Dusts} {dust_unit}")
        print(f"Funds increased to {Total_Dorabies} {dorabie_unit}, {Remain_Doubloons} {doubloon_unit} and {Remain_Dusts} {dust_unit}")
        
    else:
        lost_Dorabies = abs(Dollar_indicator) // 10
        lost_Doubloons = abs(Dollar_indicator) % 10

        Remain_Dusts = Dusts % Dusts_to_Doubloons_rate

        Total_Doubloons = Doubloons - lost_Doubloons + (Dusts // Dusts_to_Doubloons_rate)
        Remain_Doubloons = Total_Doubloons % Doubloons_to_Dorabies_rate

        Total_Dorabies = Dorabies - lost_Dorabies + (Total_Doubloons // Doubloons_to_Dorabies_rate)

        # Check units for correct pluralization
        dorabie_unit = "Dorabie" if Dorabies == 1 else "Dorabies"
        doubloon_unit = "Doubloon" if Doubloons == 1 else "Doubloons"
        dust_unit = "Dust" if Dusts == 1 else "Dusts"

        print(f"Lost {lost_Dorabies} {'Dorabie' if Total_Dorabies == 1 else 'Dorabies'}, {lost_Doubloons} {doubloon_unit} and 0 {dust_unit}")
        
        #check value of Dorabies if it have a value lower than zero
        if Total_Dorabies < 0:
           return [0 ,0 ,0]
        else:
            print(f"Funds decreased to {Total_Dorabies} {'Dorabie' if Total_Dorabies == 1 else 'Dorabies'}, {Remain_Doubloons} {doubloon_unit} and {Remain_Dusts} {dust_unit}")
        
    return [Total_Dorabies, Remain_Doubloons, Remain_Dusts] #return values of Dorabies,Doubloons and Dusts



"""Checkpoint 2 Tasks"""

def set_character_number():
    """
    Prompts the user to choose the number of characters and generates a message based on the input.

    Returns:
    int: The number of characters chosen by the user.
    """
    while True:#if the input is wrong it will ask again

        user_input = int(input("How many characters do you want? "))
        #check the user input
        if user_input == 1:
            hey = "character"
        else:
            hey = "characters"

        if 1 <= user_input <= 5:
            print(f"There will be {user_input} {hey} attempting to Rise from the (Mon)Ashes!")
            return user_input #return the user_input
        else:
            print("You may choose 1-5 characters only!")# if the input is out ouf range this message will be print

def set_names_manual(number1):
    """
    based on the given number, permits the manual insertion of character names.

    Character count (number1 (int)) is one of the arguments.

    Returns:
    list: The entered character names as a list.
    """
    number_of_characters = number1 #unpack the number1
    list1 = []
    for i in range(number_of_characters):
        name = input(f"Set character {i + 1} name:\n").upper()
        while name in list1:
            name = input(f"{name} is a duplicate, try again!\nSet character {i + 1} name:\n").upper()
        list1.append(name)
    return (list1)

def set_divided_by_integer():
    """
    Prompts the user to pick a number and returns the chosen number.

    Returns:
    int: The chosen number between 1 and 6.
    """
    divisible_by = int(input("Pick a number between 1-6 (inclusive):\n"))
    while not (1 <= divisible_by <= 6):# Validates if the entered number is within the valid range
        divisible_by = int(input("You may choose a number between 1-6 (inclusive) only!\nPick a number between 1-6 (inclusive):\n"))
    print (f'There will be {divisible_by} character attempting to Rise from the (Mon)Ashes!')
    return divisible_by # Returns the chosen number

def set_names_automatic(DEFAULT_CHARACTER_LIST,noc,div):
    """
    Automatically chooses character names according to predetermined criteria.

    Args:
    A list of the default character names is called DEFAULT_CHARACTER_LIST (list).
    noc (int): The quantity of characters to choose.
    div (int): The name selection divisor.

    Returns:
    list: A list of character names that were chosen at random.
    """
     # Define lists of vowels and consonants
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y"]
    # Initialize an empty list to store selected character names
    list2 = []
    number_of_characters = noc # Assign the value of 'noc' (quantity of characters to choose)
    while True:#Loop to ensure a valid option is chosen for 'div' (name selection divisor)
        divisible_by = div #Assign the value of 'div' (value of divisible_by)
        while not (1 <= divisible_by <= 6):#check the validity of the divisible_by
            divisible_by = int(input("You may choose a number between 1-6 (inclusive) only!\nPick a number between 1-6 (inclusive):\n"))

        # Iterate through the default character names    
        for name in DEFAULT_CHARACTER_LIST:#check the consonent in the character's name
            num_consonants = 0
            # Count the number of consonants in the character's name
            for alphabets in name:
                if alphabets in consonants:
                    num_consonants += 1
           # Check if the number of consonants is divisible by 'div' and the name is not already in the list2
            if num_consonants % divisible_by == 0 and name not in list2:
                list2.append(name)#add the name into list2
        # Select the desired number of characters from list2
        wanted_characters = list2[:number_of_characters]
        print(wanted_characters)
        k = wanted_characters
        return k # Return the selected character names
    else:
        print("Invalid option. Please choose 'M' for manual selection or 'A' for automatic selection.")

def return_welcome_message(character_list):
    """
    The length of the supplied character list will determine how long the welcome message should be.

    Character_list (list) is the list of characters in the arguments.

    Returns:
    str: A welcome greeting

    """
      #Check if the input is a list
    if not isinstance(character_list, list):
        return "Invalid input. Please provide a list of characters."
    # Get the length of the character list
    charlist_length = len(character_list)
     #Check the length of the character list 
    if 0 <= charlist_length <= 4:
        # construct initial message about the year and AI takeover
        welcome_message = "It is the year 3045. Sentient Artificial Intelligence Bots have now taken over."
        
        # Check if there are no characters in the list
        if charlist_length == 0:
            return "No characters found."
         # Check if there is only one character in the list
        elif charlist_length == 1:

            return f"{welcome_message}\n{character_list[0]} must rise from the (Mon)ashes!\nThey are BERYL's only hope!"

        else:
            # Join the names with commas and add 'and' before the last name
            formatted_names = ', '.join(character_list[:-1]) + f" and {character_list[-1]}"
            return f"{welcome_message}\n{formatted_names} must rise from the (Mon)ashes!\nOnly one character may survive!"

    else:
        return "Invalid character list length. Please provide a list with characters between 0-4 (inclusive) only!"



"""Checkpoint 3 Tasks"""

def check_valid_maze_location(coordinates):
    """
    Determines whether locations in a collection of coordinates fall inside a maze's boundaries.

    The arguments are as follows: - coordinates (list): List of tuples that represent positions (row, column).

    Returns:
    A list of booleans indicating whether or not each place is inside the maze's perimeter.
    """
     # Extract row and column from the given coordinates
    row, column = coordinates[0], coordinates[1] 
    # Define maze dimensions
    rows = 4
    columns = 10
    
    # Check if the coordinates fall within the maze boundaries
    if 0 <= row < rows and 0 <= column < columns:
        return True 
    else:
        return False

def visualise_maze(BERYL_MAZE, character_name, character_position):
    """
    Shows the maze with a character placed at a certain location.

    Arguments:
    BERYL_MAZE (list): The maze is represented as a 2D list.
    The character's name is represented by character_name (str).
    character_position (tuple): The character's row and column positions.

    Returns: 
    None

    """
     # Extract row and column from the given coordinates
    row, column = character_position[0], character_position[1]

    #check the validity of the row and column from the given coordinates does it's within the maze
    if 0 <= row < len(BERYL_MAZE) and 0 <= column < len(BERYL_MAZE[0]):
        # Iterate over the maze
        for r in range(len(BERYL_MAZE)):
            for c in range(len(BERYL_MAZE[0])):
                # Place the character at the specified position
                if r == row and c == column:
                    print(f'<{character_name[0].upper()}>', end="   ")
                else:
                    print(BERYL_MAZE[r][c], end="   ")#Display the maze content
            print()  # Move to the next line after each row
    else:
        print("Invalid position")

def deploy_drone(BERYL_MAZE, position, direction, digit):
    """
    uses a drone to search the maze for a particular digit in a particular direction.

    Args:
    BERYL_MAZE (list): The maze is represented as a 2D list.
    location (tuple): The drone's initial location (row, column).
    The direction (str) indicates the drone's movement ("right", "down", "up").
    digit (int): The number to look for in the maze.

    Returns:
    list: Tuple list of positions that have been visited.
    list: A list of the maze's visited integers.
    """
    #initial cordinate of the drone
    drone_row, drone_column = position[0],position[1] #check the initial cordinate of the drone
    digit_found = False

    # Check the specified direction for drone movement
    if direction == "right":
        visited_c = [] #list of the item's coordinates
        visited_i = []  #list of the item (number in the maze)

        # Move the drone to the right within maze boundaries
        for column in range(drone_column + 1, 11, 1):
            if str(digit) not in str(BERYL_MAZE[drone_row][column]): 
                visited_i.append(BERYL_MAZE[drone_row][column])
                visited_c.append((drone_row, column))
            else:
                visited_i.append(BERYL_MAZE[drone_row][column])
                visited_c.append((drone_row, column))    
                digit_found = True
                break

    elif direction == "down":
        visited_c = [] #list of the item's coordinates
        visited_i = [] #list of the item (number in the maze)

        # Move the drone downwards within maze boundaries
        for row in range(drone_row + 1, 5, 1):
            if str(digit) not in str(BERYL_MAZE[row][drone_column]):
                visited_i.append(BERYL_MAZE[row][drone_column])
                visited_c.append((row, drone_column))
            else:
                visited_i.append(BERYL_MAZE[row][drone_column])
                visited_c.append((row, drone_column))
                digit_found = True
                break
    else:
        visited_c = [] #list of the item's coordinates
        visited_i = [] #list of the item (number in the maze)

        # Move the drone upwards within maze boundaries
        for row in range(drone_row - 1, 0, -1):
            if str(digit) not in str(BERYL_MAZE[row][drone_column]):
                visited_i.append(BERYL_MAZE[row][drone_column])
                visited_c.append((row, drone_column))
            else:
                visited_i.append(BERYL_MAZE[row][drone_column])
                visited_c.append((row, drone_column))
                digit_found = True
                break

    if digit_found:
        print (f"Found digit at location {visited_c[-1]}: {visited_i[-1]}")
        return visited_c, visited_i #return the final location of drone and list of visited location

    else:

        print (f"Entered restricted area!\n") # Notify when the drone enters a restricted area
        return [], []

def navigating_maze(visited_position_list, dollar_indicator_list, funds, dusts_to_doubloons, doubloons_to_dorabies):
    """
    Makes their way through the maze, updating funds according to certain signs.

    Arguments:
    tuples that represent visited positions in the visited_position_list (list) list.
    collection of dollar indicators is represented by dollar_indicator_list (list).
    funds (list): List of the starting funds [Dusts, Doubloons, and Dorabies].
    dusts_to_doubloons (int): The speed at which dusts are converted into Doubloons.
    Doubloons to Dorabies Conversion Rate (int): Doubloons to Dorabies Conversion Rate.

    Returns:
    tuple: A tuple that contains the maze's ultimate location (row, column).
    list: After completing the maze, this list contains the remaining monies (Dorabies, Doubloons, and Dusts).

    """
    # Function to calculate funds based on Dollar indicators encountered
    def Money(Dorabies, Doubloons, Dusts, Dollar_indicator, Doubloons_to_Dorabies_rate, Dusts_to_Doubloons_rate):
        if Dollar_indicator > 0:
            collected_Dorabies = Dollar_indicator // 100
            collected_Doubloons = (Dollar_indicator % 100) // 10
            collected_Dusts = (Dollar_indicator % 10) 

            Total_Dusts = Dusts + collected_Dusts
            Remain_Dusts = Total_Dusts % Dusts_to_Doubloons_rate 

            Total_Doubloons = Doubloons + collected_Doubloons + ((collected_Dusts + Dusts) // Dusts_to_Doubloons_rate)
            Remain_Doubloons = Total_Doubloons % Doubloons_to_Dorabies_rate

            Total_Dorabies = Dorabies + collected_Dorabies + ((Doubloons + collected_Doubloons + 
                ((collected_Dusts + Dusts) // Dusts_to_Doubloons_rate)) // Doubloons_to_Dorabies_rate)

            return Total_Dorabies, Remain_Doubloons, Remain_Dusts

        else:
            lost_Dorabies = abs(Dollar_indicator) // 10
            lost_Doubloons = abs(Dollar_indicator) % 10

            Remain_Dusts = Dusts % Dusts_to_Doubloons_rate

            Total_Doubloons = Doubloons - lost_Doubloons + (Dusts // Dusts_to_Doubloons_rate)
            Remain_Doubloons = Total_Doubloons % Doubloons_to_Dorabies_rate

            Total_Dorabies = Dorabies - lost_Dorabies + (Total_Doubloons // Doubloons_to_Dorabies_rate)

            return Total_Dorabies, Remain_Doubloons, Remain_Dusts

    # Function to process movement and fund updates
    def move(Dorabies, Doubloons, Dusts, Dusts_to_Doubloons_rate, Doubloons_to_Dorabies_rate, choosen_visited,
            choosen_dollar_indicator_list):
        movements = [] #used to store information about the movement, such as the current location, the updated funds (Dorabies, Doubloons, Dusts), and a description of the movement.
        for i in range(len(choosen_visited)):
            location = choosen_visited[i]
            dollar_indicator = choosen_dollar_indicator_list[i]

            # Update funds using Money function
            Dorabies, Doubloons, Dusts = Money(Dorabies, Doubloons, Dusts, dollar_indicator,
                                                Dusts_to_Doubloons_rate, Doubloons_to_Dorabies_rate)

            # Generate a movement description
            rp = f"Reached position {location} with {Dorabies} Dorabies, {Doubloons} Doubloons and {Dusts} Dusts"

            # Handle fund depletion or negative Dorabies
            if Dorabies == 0:
                rp = "Funds depleted! Unable to continue."
                movements.append((location, Dorabies, Doubloons, Dusts, rp))
                break
            elif Dorabies < 0:
                Dorabies = 0
                Doubloons = 0
                Dusts = 0
                rp = f"Reached position {location} with {Dorabies} Dorabies, {Doubloons} Doubloons, and {Dusts} Dusts"
                movements.append((location, Dorabies, Doubloons, Dusts, rp))
                break

            # Append the current result to movements list
            movements.append((location, Dorabies, Doubloons, Dusts, rp))

        return movements # Return a list of tuples containing positions, funds, and movement description

    # Unpack funds
    Dorabies, Doubloons, Dusts = funds
    
    # Call the move function and get the aggregated results
    movement_results = move(Dorabies, Doubloons, Dusts, dusts_to_doubloons, doubloons_to_dorabies,
                            visited_position_list, dollar_indicator_list)
    
    final_location = movement_results[-1][0] if movement_results else None 
    final_fund = movement_results[-1][1:4] if movement_results else None  
    

    return final_location, list(final_fund) #return final location of the drone and the final fund



"""Start Rising From the Ashes"""

def run():
    """Add function docstring here"""
    #feel free to replace with your own print statements!
    print("""Welcome to Rising from the Ashes, a fictional universe set in a planet 
named BERYL where Sentient Artificial Intelligence Bots have taken over.\n""")

    print("SETTING UP UNIVERSE...\n")

    set_character_number()

    set_divided_by_integer()

    set_names_automatic()

    set_names_manual()

    return_welcome_message()

    visualise_maze()

    deploy_drone()

    navigating_maze()

    get_funds_string()

    #ADD YOUR CODE TO RUN ALL THE FUNCTIONS ABOVE

if __name__ == "__main__":
    run()

