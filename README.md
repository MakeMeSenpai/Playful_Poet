# Playful Poet

A peom mixer, that mixes and matches a hard coded poem in different arrangements. Run with ```$python3 poetry.py``` in terminal

***Requirements***

You can store your poem as a multi line string in Python, you do not need to read from a file.

Your code should implement the lines_printed_backwards() function. This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed. For example, if you poem is Invitation by Shel Silverstein:


then your function will print:

7 Come in!
6 Come in!
5 For we have some flax-golden tales to spin.
4 If you’re a pretender, come sit by my fire
3 A hope-er, a pray-er, a magic bean buyer…
2 If you are a dreamer, a wisher, a liar,
1 If you are a dreamer, come in,

Your code should implement the lines_printed_random() function which will randomly select lines from a list of strings and print them out in random order. Repeats are okay and the number of lines printed should be equal to the original number of lines in the poem (line numbers don't need to be printed). Hint: try using a loop and randint()

Your code should implement a function of your choice that rearranges the poem in a unique way, be creative! Make sure that you carefully comment your custom function so it's clear what it does.

Feel free to use any poem of your choice.

Stretch Requirements/Challenges (Optional)

Modify your program to read the poem from a file
Modify your program to read the poem from user input
Modify your program to randomly rearrange the words on each line
