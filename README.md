# wordsearch
wordsearch is a simple python program that tries to find a word within a grid of letters from a-z either horizontally or vertically.
# Optimisations
* The substrings for the rows and columns are precomputed when the object is instatiated to ensure that this isn't done every time the object is used.
* The wordsFound list was turned into a hashmap as this improves the time complexity of searching a word from o(n) to o(1).
# Side note
* The code has taken around 8-10 hours as I had to refresh my understanding of python syntax before undertaking the task.
* Please note that all the testing for the code has been done on a machine running the latest release of arch linux.
