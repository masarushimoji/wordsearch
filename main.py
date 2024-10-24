class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.ROW_LENGTH = 100
        self.rows = []
        self.columns = ['' for _ in range(self.ROW_LENGTH)]
        
        for i in range(0, len(self.grid), self.ROW_LENGTH):
            self.rows.append(self.grid[i:i+self.ROW_LENGTH])
        
        for x in range(self.ROW_LENGTH):
            for y in range(self.ROW_LENGTH):
                self.columns[x] += self.rows[y][x]


    def is_present(self, word):
        for line in self.rows:
            if word in line:
                return True
        
        for line in self.columns:
            if word in line:
                return True
        
        return False 


#dir ="/usr/share/dict/words"
dir = "test.txt"
fileContents = ""
with open(dir, 'r') as file:
    fileContents = file.readline().strip().lower()

ws = WordSearch(fileContents)
words_to_find = ["hi", "abc", "aa"]

for word in words_to_find:
    if ws.is_present(word):
        print("Found {}".format(word))
    else:
        print("HAVEN't found {}".format(word))