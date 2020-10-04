"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

def hometowns (my_hometown, your_hometown):
    if my_hometown == your_hometown:
        result = True
    else:
        result = False
    return result
    print(result)
    print(type(result))

my_hometown = 'Milwaukee'
your_hometown = input("What is your hometown? ")
hometowns(my_hometown, your_hometown)


"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

def add_names (first_name, last_name):
    print(full_name)

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + ' ' + last_name

add_names(first_name, last_name)


"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

def greeting (full_name, your_hometown):
    if my_hometown == your_hometown:
        print(f"Hi {full_name}, we're from the same place!")
    else:
        print(f"Hi {full_name}, I'd like to visit {your_hometown}!")
greeting (full_name, your_hometown)


"""PROMPT 4

Write a function that returns True if a fruit is a berry.
if this thing is on the berry list, then it is a berry


Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

def is_berry(fruit):
    if fruit in berries:
        result = True
    else:
        result = False
    print(result)

berries = ['strawberry', 'raspberry', 'blackberry', 'currant']
is_berry("strawberry")


"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""
def shipping_cost(fruit):
    berry_cost = 0
    other_cost = 5
    if fruit in berries:
        shipped_cost = berry_cost
    else:
        shipped_cost = other_cost
    print(f"The cost to ship a {fruit} is {shipped_cost}")
shipping_cost("strawberry")


"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""
def cost_of_item(cost, state, tax):
    if state == "CA":
        total_price = (cost * tax) + cost
    else:
        total_price = cost + tax
    print(total_price)

state = input("What state are you in? ")
purchase = int(input("How much does it cost? "))

if state == "CA":
    tax = 0.03
elif state == "PA":
    tax = 2
elif state == "MA":
    if purchase <= 100:
        tax = 1.0
    else:
        tax = 3.0
cost_of_item(10, "CA", tax)

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

#this function would require some sort of %arg or &arg function that I can't quite get yet
#it also requires a potential "infinite" list
#the end of the function would turn out the list that you were visualizing

# Write your function here


"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here

#this function would start with a simple word - something like hi
#you would then create a function that makes space for the "hi" to grow
#you would multiply this list *3
#the output would be -> 'hi', 'hihihi' to create the tuple
