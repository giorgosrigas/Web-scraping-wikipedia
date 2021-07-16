
# import wikipedia 1.4
import wikipedia
def wikipage2file(wikipedia_pagetitle, output_filepath):
    """
    function that searches a wikipedia page, retrieves the first 
    page of all the candidate pages and stores its content in 
    a text file.
    
    :param wikipedia_pagetitle: the string with the title of wiki page
    :param output_filepath: the folder where the content will be stored
    
    :return: writes the title followed by two blank lines  and the retrieved 
     content to a text file named by the title of wiki page non-spaced.
     """

# get all the pages you're searching for
    wiki_page = wikipedia.search (wikipedia_pagetitle)
    
# slice the first page from all of the candidate pages and try
# to avoid disambiguation error
    try:
        page = wikipedia.page(wiki_page[0]).title
    except wikipedia.exceptions.DisambiguationError as e:
        page = e.options[0]

# Define the title of the page
    wiki_title = page
    
# get the page content 
    wiki_content = wikipedia.page(wiki_title).content

# set the output file path and its name
    output_file = output_filepath + "/" + wiki_title.replace(" ", "") + ".txt"

# create a text file, write the title followed by two blank lines and its content
    with open (output_file, "w" , encoding="utf-8") as text_file:
        text_file.write (wiki_title)
        text_file.write ('\n\n\n')
        text_file.write (wiki_content)

        
def similar(x,y):
    """
    function that checks for the similarity between the words of
    two strings. 
    
    :param x: first string
    :param y: second string
    
    :return: returns a float number which is the result of the 
     division of the length of the intersection between the two strings' 
     words by the length of their union.
     """
    result = ''
    x_list = x.split() # convert string to a list for parsing
    x_list = [word.lower() for word in x_list] # transform all words to lowercase
    x_list =  list(set(x_list)) # list of  of words that appear at least one in x_list
    
    y_list = y.split() # convert string to a list for parsing
    y_list = [word.lower() for word in y_list] # transform all words to lowercase
    y_list =  list(set(y_list)) # list of words that appear at least one in y_list

    intersection = [word for word in x_list if word in y_list] # obtain the common words between x_list and y_list
    union = list(set(x_list).union(y_list)) # words that appear in both lists as well as their common ones
    result = float(len(intersection) / len(union) ) # find the coefficient of their similarity
    return result
   
