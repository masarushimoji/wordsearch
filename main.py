class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.fileContents = []
        with open(self.grid, 'r') as file: 
            for line in file:
                self.fileContents.append(line)
        self.columns = len(fileContents[0])
        self.rows = len(fileContents)
        
    

    
    def is_present(self, word):
        wordLen = len(word)

        
            
        return False

  

ws = WordSearch("/home/maru/Projects/pexipStuff/testFiles/grid.txt")
words_to_find = ["asdf", "helloworld"]
for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))