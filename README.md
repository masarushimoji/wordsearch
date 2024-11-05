# wordsearch
wordsearch is a simple python program that tries to find a word within a grid of letters from a-z either horizontally or vertically.
# Optimisations
* The substrings for the rows and columns are precomputed when the object is instatiated to ensure that this isn't done every time the object is used.
* The wordsFound list has been turned into a hashmap as this improves the time complexity of searching a word from o(n) to o(1).
# Side note
* The code has taken around 8-10 hours as I had to refresh my understanding of python syntax before undertaking the task.
* Please note that all the testing for the code has been done on a machine running the latest release of arch linux.
# Further improvements
Due to time constraints I sadly haven't included all of the improvements I had hoped to add to my program.  
If I had more time I would improve the code by implementing the grid as a hashmap which would improve the space complexity.  
In addition, I would split each row / column into chunks of 26 as this is the maximum length of each word. This would mean that if the word is found within a chunk, the code does not need to iterate through the rest of the row or column (which can save a lot of time if it is a very large grid). Of course, there is worst case scenario where a word overlaps these chunks in which case the program would have to iterate through the whole row or column instead. However, the chance of the word being within each chunk is significantly higher (especially since the average word length is 9). Thus, I believe this approach would save time for a large grid.  
A multicore system could be used to increase the performance of my algorithm significantly as it could be used to search through multiple rows / columns at the same time through the use of parallelisation.
