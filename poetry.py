#to dumb things down I have written comments on EVERYTHING
import random
#this is to import a python3 library that makes a psuedo randome choice!

poem = "If you are a dreamer, come in,#If you are a dreamer, a wisher, a liar,#A hope-er, a pray-er, a magic bean buyer…#If you’re a pretender, come sit by my fire#For we have some flax-golden tales to spin.#Come in!#Come in!"
#this is a global variable which is for some reason out of scope to the rest of the world other than my bottom print statement

def lines_printed_backwards():
    #this is me defining a function lines_printed_backwards
    poem = "If you are a dreamer, come in,#If you are a dreamer, a wisher, a liar,#A hope-er, a pray-er, a magic bean buyer…#If you’re a pretender, come sit by my fire#For we have some flax-golden tales to spin.#Come in!#Come in!"
    #this is poem, the string variable (you will see her a lot)
    poem = poem.split(" ")
    #This turns poems into a list of words
    poem = " ".join(poem)
    #this joins her back into a string for later splitting
    poem = poem.split("#")
    #this seperates the poem into lines
    poem = poem[::-1]
    #this reverses the order of those lines
    num = len(poem) + 1
    #say hi to num, he is our incrimentore
    for line in poem:
        #this for loop looks threw each item in the list poem.
        num -= 1
        #this deincriments num
        print(str(num) + ". " + str(line))
        #now we get to see the results!


def lines_printed_random():
    #this is me defining lines_printed_random
    poem = "If you are a dreamer, come in,#If you are a dreamer, a wisher, a liar,#A hope-er, a pray-er, a magic bean buyer…#If you’re a pretender, come sit by my fire#For we have some flax-golden tales to spin.#Come in!#Come in!"
    #long time no see. poem says hello!
    poem = poem.split(" ")
    #this splits her into words in a list
    poem = " ".join(poem)
    #this joins her back together for later splitting
    poem = poem.split("#")
    #she is now seperated by lines
    for _ in poem:
        #this for loop looks threw each item in the list poem
        num = random.randint(0, len(poem) - 1)
        #num is now a randim number generator. Thank him!
        print("Rand Lines: " + poem[num])
        #becuase of num, we are able to go threw the list randomly, and select pecifically chosen lines by num. Who knew he could be such a poet

def words_printed_random():
    #this is me defining lines_printed_random
    poem = "If you are a dreamer, come in,#If you are a dreamer, a wisher, a liar,#A hope-er, a pray-er, a magic bean buyer…#If you’re a pretender, come sit by my fire#For we have some flax-golden tales to spin.#Come in!#Come in!"
    #long time no see. poem says hello!
    poem = poem.split(" ")
    #this splits her into words in a list
    poem = " ".join(poem)
    #this joins her back together for later splitting
    poem = poem.split("#")
    #she is now seperated by lines
    poem = " ".join(poem)
    #totally not the same as the last function
    for _ in poem:
        #this for loop looks threw each item in the list poem
        num = random.randint(0, len(poem) - 1)
        #num is now a randim number generator. Thank him!
        print("Rand Words: " + poem[num])
        #becuase of num, we are able to go threw the list randomly, and select pecifically chosen lines by num. Who knew he could be such a poet

def rev_poetry():
    #this is me defining rev_poetry (aka my custom function)
    poem = "If you are a dreamer, come in,#If you are a dreamer, a wisher, a liar,#A hope-er, a pray-er, a magic bean buyer…#If you’re a pretender, come sit by my fire#For we have some flax-golden tales to spin.#Come in!#Come in!"
    #poem is defined as a string! And a long one at that!
    poem = poem.split("#")
    #poem is sperated into lines
    num = 0
    #he's back as our incrimentor
    for line in poem:
        #again looks threw each item in poem
        rev = line[::-1]
        #instead of using reversed which gives us reversed object for some reason (who would want that?) I used [::-1] to rev EVERYTHING
        num += 1
        #He's growing :3
        print(str(num) + ". " + str(rev))
        #See the results of a completely backwards spell casting poem!


lines_printed_backwards()
lines_printed_random()
rev_poetry()
print(poem)
# runs my dumb little program!