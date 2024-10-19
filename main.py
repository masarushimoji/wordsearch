class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.fileContents = []
        rowLength = 10


        with open(self.grid, 'r') as file:
            self.fileContents = file.read().split()
        

    def is_present(self, word):
        print(self.fileContents)
        return False


ws = WordSearch("/home/maru/Projects/pexipStuff/testFiles/grid.txt")

words_to_find = ["asdf", "helloworld"]

for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))