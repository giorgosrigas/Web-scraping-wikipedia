# Web-scraping-wikipedia

###  wikipage2file function
1.Searches all Wikipedia pages that can be retrieved with the wikipedia_pagetitle string.

2.Retrieves the first candidate Wikipedia page and obtains two strings: the title and the content of that page.

3. Writes a text file named wikipage.txt, where wikipage is replaced by the Wikipedia page's title and the text of the file is the contents of the particular wikipedia page


###  similar function

Calculates the similarity of two different wikipedia pages x and y.

1.Computes the set containing every word that occurs in x at least once. Do the same for y.

2. Obtains the set of the words that are contained both in x and in y.

3. Obtains the set of all the words contained in x or y (including words contained in both x and y).

4. Returns the result of dividing the length of the set in (2) by the length of the set in (3). The function returns a value between 0 and 1 (with 0 being no
similarity)

##  Requirements
programming language: Python 3

libraries: Wikipedia API
