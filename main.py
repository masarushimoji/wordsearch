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
        # for loop that loops through the rows and tries to see if the word is
        # in the grid horizonatally.
        for line in self.fileContents:
            if word in line:
                return True # return true in the case that the word has been found
        
        for x in range(self.columns):
            s = "" # declare an empty string variable s
            for y in range(self.rows):
                s = s + (self.fileContents[y])[x] #loops through the "y"th column and concatenates the letters in each column into variable s
            if word in s:
                return True # return true in the case tht the word has been found
        return False #word has not been found in a row or column so return false



ws = WordSearch("/home/maru/Projects/pexipStuff/testFiles/grid.txt")
words_to_find = ["hi", "bonkers", "hello"]
for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))