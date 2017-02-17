class Markov:
    def __init__(self, text, splitter="", chain_length=3):
        self.text = text
        self.db = {}
        # Enable letter-by-letter splitting
        if splitter:
            self.words = text.split(splitter)
        else:
            self.words = list(text)
        self.chain_length = chain_length
        self.db_gen()
    
    def gen_chains(self):
        if len(self.words) < self.chain_length:
            raise Exception("Input text too short")
        for i in range(len(self.words)-(self.chain_length - 1)): # that's disgusting
            yield self.words[i], self.words[i+1], self.words[i+2]
    
    def db_gen(self):
        for i in self.gen_chains():
            key = i[:-1]
            if key in self.db:
                self.db[key].append(i[-1])
            else:
                self.db[key] = [i[-1]]
        return self.db
