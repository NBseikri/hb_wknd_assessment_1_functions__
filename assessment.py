# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def cost_w_tax(*args):
    """
    This function calculates a total cost of an item based on CA tax,
    an identified non-CA tax or a default 5% tax if the user does not include 
    a tax in in the parameter.
    """

    if len(args) == 2:
    #Evaluates whether two arguments are passed into the function (no tax rate)
        state = args[0]
        #When there are two arguments, it assigns the inputted state (arg[0]) to state
        cost = args[1]
        #When there are two arguments, it assigns the inputted cost (arg[1]) to cost
        if state == 'CA':
        #Evaluates whether state is CA
            tax = float(.07)
            #When state is CA, a 7% tax rate is assigned
        else:
        #Handles non-CA states
            tax = float(.05)
            #When state is not CA, a 5% rate is assigned
        total = cost + cost * tax
        #Assigns total as the result of cost plus cost times tax to total
    else:
    #Handles scenarios where three arguments are passed (tax is included)
        tax = args[0]
        #tax is set to arg[0] which contains the tax rate
        state = args[1]
        #state is set to arg[1] which contains the state
        cost = args[2]
        #cost is set to arg[2] which contains the cost
        if state == 'CA':
        #Evaluates whether state is CA
            tax = float(.07)
            #For California, any entered tax is overriden with 7% tax
        else:
        #This conditions handles non-CA tax
            tax = float(tax) / 100
            #This variable holds the result of the whole number representing 
            #the tax rate divided by 100 (so that it exists as a decimal)
        total = cost + cost * tax
        #Assigns total as the result of cost plus cost times tax to total

    return total
    #Returns the total resulting from the applicable conditions. 

print cost_w_tax(9, 'WA', 30)
#This line calls the functino with sample details (9 percent tax, Washington as
#the state and thirty as the base cost). The printed result is 32.7.

#I have assumed that, unlike the practice exercise, a user may input a whole
#(ex. 9) instead of a decimal (ex. .09) for the tax rate. The function either 
#assigns a decimal rate or divides a non-CA rate by 100 to get a usable decimal.
#I have also assumed that function arguments will be entered in the order they 
#appear in the instructions for the purposes of indexing.

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit_name):
    """
    This function checks to see if an inputted fruit name is either a strawberry,
    cherry or blackberry.
    """

    return fruit_name in ['strawberry', 'cherry', 'blackberry']
    #Returns a boolean value (True or False) depending on whether the passed
    #fruit_name is in the list. 

print is_berry('strawberry')
#Calls the function with the sample word strawberry and prints a True result

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit_name):
    """
    This function returns a shipping cost based on whether the fruit name is an
    identified fruit or not.
    """

    if is_berry(fruit_name) == True:
    #Evaluates if the passed fruit_name is among the fruits in the 
    #is_berry function
        return 0
        #Returns 0 for 'strawberry', 'cherry' or 'blackberry'
    else:
    #Evaluates if the passed fruit_name is not among the fruits in the
    #is_berry function
        return 5
        #Returns 5 for fruits other than 'strawberry', 'cherry' or 'blackberry'

print shipping_cost('mango')
#Calls the function with the sample fruit_name 'mango' and returns a shipping 
#cost of 5. 

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town):
    """
    This function checks to see if the town input is an identified hometown.
    """
    return town in ['Seattle', 'seattle', 'Emerald City', 'The 206']
    #Returns a boolean value (True or False) depending on whether the passed
    #town is in the list. The list accounts for a capitalization option and 
    #a couple nicknames when determining whether the input is the hometown. 

print is_hometown('Seattle')
print is_hometown('Portland')
#These lines call the function with Seattle and Portland as sample towns.
#Seattle and Portland returned True and False, respectively. 

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first, last):
    """
    This function takes first and last names as passed arguments and concatenates
    them with a space in between the names.
    """
    return first + ' ' + last
    #Returns the concatenation of the passed first name, a space and the passed 
    #last name.

print full_name('Nada', 'Bseikri')
#Calls the function and prints the concatenation produced by the return line.
#This line uses my name for sample first and last names and prints 'Nada Bseikri'.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town, first, last):
    """
    This function prints one of two greetings (each containing an inputted first 
    and last name) depending on whether someone is from an identified hometown.
    """

    if is_hometown(town) == True:
    #Checks to see if passed town argument is the hometown in the is_hometown
    #function
        return 'Hi, ' + full_name(first, last) + ', we are from the same place!'
        #When the hometown is the same, this return line concatenates 'Hi, ', a
        #result of the full_name function when a first and last name are passed
        #and, lastly, ', we are from the same place!'
    else:
    #This part of the conditional block handles towns that are not Seattle, as
    #determined by the is_hometown function. 
        return 'Hi, ' + full_name(first, last) + ', where are you from?'
        #When the hometowns are different, this return line concatenates 'Hi, ', a
        #result of the full_name function when a first and last name are passed
        #and, lastly, ', where are you from?'

print hometown_greeting('Seattle', 'Nada', 'Bseikri')
print hometown_greeting('Toronto', 'Aubrey', 'Graham')
#These lines call the function and print the greeting for myself, a Seattlite and
#Drake (using his real name) as a Toronto native. The print results, 
#respectively, are:
#       Hi, Nada Bseikri, we are from the same place!
#       Hi, Aubrey Graham, where are you from?

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################