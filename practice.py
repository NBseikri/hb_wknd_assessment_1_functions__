"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """
    This function prints 'Hello World' without taking an argument.
    """

    print 'Hello World'
    #Prints 'Hello World' when the function is called. 

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """
    This function takes a name as an argument and prints a greeting with that name in it.
    """

    print 'Hi ' + name
    #Prints a concatenatino of 'Hi' and the name argument passed through the function.

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(n1, n2):
    """
    This function multiplies two inputted integers and prints the result.
    """

    return n1 * n2
    #Returns the result of n1 * n2
    print print_product
    #Prints the result of the function with two inputted variables

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(word, number):
    """
    This function repeats an inputted string by a number that is also inputted. 
    """

    a_number = int(number)
    #Sets the number entry as a integer
    print word * a_number
    #Prints the string repeated a number of times equal to the value of a_number


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(number):
    """
    This function evaluates an inputted number and prints a message indicating 
    whether the number is higher than, lower than or equal to zero. 
    """

    if number > 0:
    #Evaluates whether number is greater than zero
        print "Higher than 0"
        #Prints a message that the number is greater than zero
    elif number < 0:
    #Evaluates whether number is less than zero
        print "Lower than 0"
        #Prints a message that the number is less than zero
    else:
    #Captures the only other remaining scenario (number == 0)
        print "Zero"
        #Prints a message that the number is zero

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(number):
    """
    This function returns whether a number is divisible by three. 
    """
    return number % 3 == 0
    #Returns a True or False if number is divisible by three (or, more accurately,
    #has a remainder of 0 when divided by three).

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(words):
    """
    This function counts the number of spaces in an inputted sentence string. 
    """

    spaces = 0
    #Sets a counter to capture the number of spaces identified in the for loop
    for word in words:
    #Evaluates each word in words (the sentence string).
        if ' ' in word:
        #Evaluates whether there is a space between words (' ').
            spaces = spaces + 1
            #When there is a space between words, the counter increases by 1.

    return spaces
    #Returns the final count contained in the spaces variable

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(*args):
    """
    This function calculates the total meal price with either (a) an inputted base
    price and tip percentage or (b) just an inputted base price using a default 15%
    tip. 
    """

    if len(args) == 1:
    #Conditional statement evaluates whether input contains just a base price 
    #(a length of one indicates a single base price input)
        price = args[0]
        #Sets the price variable to the intial and only index of args
        total_meal_price = price + price * float(.15)
        #Variable is set as the result of price * a default tip of 15% added to 
        #the price
    else:
    #This conditional handles alternative inputs containing both price and tip
        price = args[0]
        #Sets the price variable to the initial index of args
        tip = args[1]
        #Sets the price variable to the first index of args
        #If the doctest didn't already have the input as a decimal and
        #the input was a whole number (ex. 20 for 20%), the function would need
        #to divide that entry by 100 (ex. tip = args[1] / float(100))
        total_meal_price = price + price * tip
        #Variable is st as the result of price * the inputted tip added to
        #the price
 
    return total_meal_price
    #Returns the total from the executed conditional

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def sign_and_parity(num):
    """
    This function evaluates whether an inputted number is positive or negative 
    and even or odd.
    """

    num_info = []
    #Value of this variable will be the list items added by the for loop
    if num > 0 and num % 2 == 0:
    #Evaluates whether num is (1) greater than 0 and (2) is even (divisible 
    #by two without a remainder)
        num_info.extend(['Even', 'Positive'])
        #Populates the num_info variable with ['Even', 'Positive']
    elif num < 0 and num % 2 == 0:
    #Evaluates whether num is (1) less than 0 and (2) is even (divisible 
    #by two without a remainder)
        num_info.extend(['Even', 'Negative'])
        #Populates the num_info variable with ['Even', 'Negative']
    elif num > 0 and num % 2 == 1: 
    #Evaluates whether num is (1) greater than 0 and (2) is odd (divisible 
    #by two with a remainder of 1)
        num_info.extend(['Odd', 'Positive'])
        #Populates the num_info variable with ['Odd', 'Positive']
    elif num < 0 and num % 2 == 1: 
    #Evaluates whether num is (1) less than 0 and (2) is odd (divisible 
    #by two with a remainder of 1)
        num_info.extend(['Odd', 'Negative'])
        #Populates the num_info variable with ['Odd', 'Negative']
    else:
    #Caputures the only remaining scenario, that the input is zero
        print 'Your number is zero.'
        #Prints a message indicating that the number is zero

    return num_info
    #Returns the now populated num_info variable

parity, sign = sign_and_parity(3)
#Unpacks the num_info results of the function into two new variables: parity and sign. 
print [parity, sign]
#Prints the values of parity and sign
################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def full_title(*args):
    """
    #Formats inputted name or name and title as a name and title string.
    """

    if len(args) == 1:
    #This condition captures whether just one argument has passed through the
    #function (this represents just entry of a name without a title)
        name = args[0]
        #Variable is set to the value initial and only index in args
        title_and_name = 'Engineer ' + name
        #Concatenates default 'Engineer' string (used when no title is entered)
        #with the inputted name; result is set as the value of the title_and_name
        #variable
    else:
    #This condition captures scenarios where args is not merely a name without
    #a title
        name = args[0]
        #Variable is set to the value of the initial index containing the name
        title = args[1]
        #Variable is set to the value of the first index containing the title
        title_and_name = title + " " + name
        #Concatenates title, a space and name; result is set as the value of 
        #the title_and_name variable  
 
    return title_and_name
    #Returns the title_and_name variable (which contain the resulting con-
    #catenation)

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(recipient1, recipient2, sender):
    """
    This function incorporates the return from the previous function into this new
    function that creates a letter text.
    """

    title_and_name = full_title(recipient1, recipient2)
    #The value of this variable is the return from the full_title function
    print "Dear %s, I think you are amazing! Sincerely, %s" % (title_and_name, sender)
    #This line prints a message with string formatting that replaces the %s
    #symbols with the title_and_name variable and the inputted sender, respectively.

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
