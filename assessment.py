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

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

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