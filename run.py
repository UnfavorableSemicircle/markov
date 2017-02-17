# Run me!

file = open('corpus')
import markov
markov_obj = markov.Markov(file)
markov_obj.generate_markov_text()
