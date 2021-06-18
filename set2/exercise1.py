"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

# it will print the set letters/symbols that equal "some_words" in a list format
for word in some_words:
    print(word)  # it printed 'what, does, this, line, do, ?' in a list formart

#it will print the set words within the square brackets which involve defining lists
for x in some_words:
    print(x) #it printed 'what, does, this, line, do, ?' in a list formart

# prints what equals "some_words", the equal value means to the user and computer what components are associted when typing that phrase
print(some_words) #printed '['what', 'does', 'this', 'line', 'do', '?']'

#this is used as a boolean and determines whether or not in the set list within "some_words" it has more than three words
if len(some_words) > 3:
    print('some_words contains more than 3 words') #has more than three words so it printed 'some_words contains ore than 3 words'

# platform.uname() provides information on the computer such as the OS
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction() # it printed uname_result(system='Windows', node='DESKTOP-7LDOP9I', release='10', version='10.0.19041', machine='AMD64', processor='Intel64 Family 6 Model 142 Stepping 10, GenuineIntel')
