class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.ROW_LENGTH = 3
        self.gridArr = []
        
        for i in range(0, len(self.grid), self.ROW_LENGTH):
            self.gridArr.append(self.grid[i:i+3])
            

    def is_present(self, word):
        # for loop that loops through the rows and tries to see if the word is
        # in the grid horizonatally.
        for line in self.gridArr:
            if word in line:
                return True # return true in the case that the word has been found
        
        for x in range(self.ROW_LENGTH):
            s = "" # declare an empty string variable s
            for y in range(self.ROW_LENGTH):
                s = s + (self.gridArr[y])[x] #loops through the "y"th column and concatenates the letters in each column into variable s
            if word in s:
                return True # return true in the case tht the word has been found
        return False #word has not been found in a row or column so return false


#dir ="/usr/share/dict/words"
dir = "test.txt"
fileContents = ""
with open(dir, 'r') as file:
    fileContents = file.readline().strip() 
    
ws = WordSearch(fileContents)
words_to_find = ["hi", "abc", "aa"]

for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))
    else:
        print("HAVEN't found {}".format(word))