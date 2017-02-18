# Markov

A Markov chain is a mathematical object that contains several (but not an infinite number of) states and the probabilities of switching between them. The probabilities don't change depending on what state was there previously.

Besides the thousands of actually useful things Markov chains do, they are also handy for generating text that looks vaguely similar to the original text in question. This generator builds a Markov chain by reading a corpus and uploading all the states and successive states into a database, then runs a generation algorithm using the database as the input. I figured that the database itself would be handy for entry into a graphing application to see if it resembled language or was otherwise non-random.

Would like to get a pseudotext generator built again, though.
