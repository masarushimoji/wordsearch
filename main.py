class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.fileContents = []
        with open(self.grid, 'r') as file:
            for line in file: self.fileContents.append(line)
        self.fileContents = [s[:-1] for s in self.fileContents] 
        self.columns = len(self.fileContents[0])
        self.rows = len(self.fileContents)


    def is_present(self, word):
        wordLen = len(word)
        #print(self.columns)
        #print(self.rows)
        #print(self.fileContents)
        for line in self.fileContents:
            if word in line:
                return True
        
        for x in range(self.columns):
            s = ""
            for y in range(self.rows):
                s = s + (self.fileContents[y])[x]
            print(s)
            if word in s:
                return True



        return False

  

ws = WordSearch("/home/maru/Projects/pexipStuff/testFiles/grid.txt")
words_to_find = ["hi", "bonkers", "hello"]
for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))