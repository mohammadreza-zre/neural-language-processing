neural language processing(NLP)

aim ----->> summerization certain number of sentence base on importance from a html page


steps : 
        1 . sending a request to the website address and get the page
        2 . parse the html by BS4(beatiful soup)
        3 . grab the paragraphs
        4 . cleaning the text by the regular expression module
        5 . cracking text to the words
        6 . scoring the words base on word frequency
        7 . score normalization
        8 . crack the text to the sentences
        9 . scoreing the sentences base on word scores
        10 . choose the number of sentences and grab the summerization
