import random

LENGTH_OF_CODE = 4

ALLOWED_CHARACTERS = ['1', '2', '3', '4']

def generate_code():
    """
    Returns secret code, which is a randomly generated four-element list of 
    numbers between 1-4.

    >>> generate_code()
    ['1', '4', '3', '2']
    >>> generate_code()
    ['4', '4', '1', '3']
    >>> generate_code()
    ['2', '3', '4', '3']
    """
    return [random.choice(['1', '2', '3', '4']) for num in range(1, 5)]

def wrong_code_length(code_breaker_attempt):
    """
    Returns True if the length of the code_breaker_attempt is not the allowed length set
    LENGTH_OF_CODE.

    >>> wrong_code_length(['1', '2', '4', '3'])
    False
    >>> wrong_code_length(['1', '2', '4', '5', '4'])
    True
    >>> wrong_code_length(['1', '2'])
    True
    """
    if len(code_breaker_attempt) == LENGTH_OF_CODE:
        return False
    else:
        print("Wrong Length")
        return True

for x in ALLOWED_CHARACTERS:
    """
    Returns True if code_breaker_attempt contains characters that are not allowed,
    which is set by ALLOWED_CHARACTERS.

    >>> wrong_characters(['1', '2', '4', '3'])
    False
    >>> wrong_characters(['b', 'e', 'e', 'p'])
    True
    >>> wrong_characters(['m', 'a', 'r', 's'])
    True
    """

    def wrong_characters(code_breaker_attempt):
        for i in code_breaker_attempt:
            if i == x:
                return False
            else:
                print("Wrong characters")
                return True

def get_code_breaker_attempt():
    """
    The code breaker attempts to guess the secret code. This functions returns that
    attempt as a four-element list. This function also checks to make sure if the 
    attempt is valid (the right length and using valid letters). If not, then it
    continues to ask for a valid answer until one is given. 

    """
    code_breaker_attempt = [str(i) for i in input()]
    wrong_code_length(code_breaker_attempt)
    wrong_characters(code_breaker_attempt)
    return code_breaker_attempt


def check_numbers(code, code_breaker_attempt):
    """ 
    Checks if colors guessed by the code breaker exist in the secret code. Returns
    the number of correct numbers.

    >>> check_numbers(['1', '1', '2', '4'], ['1', '1', '2', '4'])
    4
    >>> check_numbers(['1', '1', '2', '4'], ['2', '1', '3', '4'])
    3
    >>> check_numbers(['2', '1', '2', '1'], ['3', '1', '4', '1'])
    2
    """

    right_numbers = []
    for i in code_breaker_attempt:
        if i in code:
            right_numbers.append(i)
    numbers_check = len(right_numbers)
    return numbers_check



def check_order(code, code_breaker_attempt):
    """
    Checks if numbers are in the same position as the corresponding number in
    the code. Returns the number of colors in the correct position.

    >>> check_order(['1', '1', '2', '4'], ['1', '1', '2', '4']))
    4
    >>> check_order(['1', '1', '2', '4'], ['2', '1', '3', '4'])
    2
    >>> check_order(['2', '1', '2', '1'], ['3', '1', '4', '3'])
    1
    """

    index = 0
    right_position = 0
    while index <= 3:
        if code_breaker_attempt[index] == code[index]:
            index+=1
            right_position+=1
        else:
            index+=1
    return right_position
   


def get_key_pegs(numbers_check, order_check):
    """
    Key pegs returns feedback to code breaker about how much of their code is correct.

    Red: Number is in the right position
    White: Number is in the wrong position
    Empty: Number (or duplicate of number) does not exist in the secret code.
    """

    pegs = []
    while order_check > 0:
        pegs.append("Red")
        order_check -= 1
        if len(pegs) == 4:
            break
      
    while numbers_check > 0:
        pegs.append("White")
        numbers_check -= 1
        if len(pegs) == 4:
            break

    while len(pegs) != 4:
        pegs.append("Empty")
        if len(pegs) == 4:
            break

    return pegs



def give_player_feedback(key_pegs):

    print(key_pegs)


MAX_ATTEMPTS = 10

def continue_game_condition(key_pegs, attempts, code):
    
    if not "Red" and "White" and "Empty" not in key_pegs:
        print("You Won! The code was:")
        print(code)
        return False
    else:            
        print("Wrong code! You have:", str(attempts), "attempts left!")
        return True
    


def mastermind():
    print("Welcome to Mastermind! Please enter your code!")
    code = generate_code()
    attempts = MAX_ATTEMPTS
    
    while attempts > 0:
        attempts -= 1
        code_breaker_attempt = get_code_breaker_attempt()
        numbers_check = check_numbers(code, code_breaker_attempt)
        order_check = check_order(code, code_breaker_attempt)
        key_pegs = get_key_pegs(numbers_check, order_check)
        give_player_feedback(key_pegs)
        chance = continue_game_condition(key_pegs, attempts, code)
        if chance == False:
            break
    if attempts == 0:
        print("Game Over! The code was:", code)

mastermind()