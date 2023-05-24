letter = 'Hey my name is {} and i am from {}'

country = 'INDIA'
name = 'SHAD'

print(letter.format(name,country))
print(letter.format(country,name)) #This has a problem


letter = 'Hey my name is {1} and i am from {0}'

country = 'INDIA'
name = 'SHAD'

print(letter.format(name,country)) #this has a problem, it returns name as index 0 and countey as index 1 and hence it'll go wrong
print(letter.format(country,name)) 

#not a efficient method to do

#here it comes a fsttring


print(f"hey my name is {name} and i am from {country}")

name = 'assish'
country ='pakistan'

price = 20.09999
text = f'for only {price:.2f} dollers'# .2f will return 2 decimal value 
# print(text.format(price = 49.099))
print(text)

val = 'Geeks'
print(f"{val} for {val} is a portal for {val}.")
name = "Tushar"
age = 23
print(f"Hello, my name is {name} and i'm {age} years old.")

print(f"{2*30}")

print(f"hey my name is {{name}}") #will print literally and will displayed as it is



#-------------------DocStrings----------------
#python doctrings are the string literals that appear right after the defination of a fucntion,class etc

def square(n):
    '''takes in a number n, returns the 
    square of n''' #it isnt a comment, it is the doc strings, which is always writen rihgt after defining a func or class


    print(n**2)
square(5)
print(square.__doc__) #returns the doc string

def square(n):
    print(n)
    '''takes in a number n, returns the 
    square of n''' #it isnt a comment, it is the doc strings, which is always writen rihgt after defining a func or class


    print(n**2)
square(5)
print(square.__doc__) #returns the doc string as none because print statement comes right after defining the func, rather it should be docstirng



def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
print(add(1,2))
print(add.__doc__) #will print all the doc string

#pep 8 is a guideline and provides best practice, developed in 2001, foucus was making a program readble,maintable,consistent,
#pep - python enjance proposal

#zenofpython 
import this
#will print a poem, a really good poem lol
