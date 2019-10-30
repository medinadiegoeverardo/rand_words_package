import pandas as pd
import numpy as np

# import os
# file = input('file: ');
# filename, file_extension = os.path.splitext(file)
# if filename != 'webarchive' or 'txt':

with open('/Users/diego/Documents/LambdaUnit3/classes/words.webarchive') as inpt:
    dictionary = inpt.read()
    words = dictionary.splitlines()

class Random():

    def __init__(self, words):
        self.words = words

    def select_words_range(self, number_of_words, first_word_number=0, last_word_number=None):
        numbers = []
        sentence = []
        if last_word_number == None:
            last_word_number = len(self.words)
            """
            randomly pick x numbers from here to here
            """
            for i in range(0, number_of_words):
                numbers.append(np.random.randint(first_word_number, last_word_number))
            for i in numbers:
                sentence.append(self.words[i])
            return " ".join(sentence)

    def make_df_rows(self, rows): # self is object with words
        """
        This function is useful when the user wants to provide list of words
        and separate them by number of rows

        make_df_rows(10) yields 10 rows of x list
        """
        data_for_df = np.array_split(self.words, rows)
        df = pd.DataFrame(data=data_for_df)
        return df

# -----------------

# attempt to give user more freedom to input dif files of words/letters


# import pandas as pd
# import numpy as np
# import os

# file = input('file: ');
# filename, file_extension = os.path.splitext(file)

# if filename != 'webarchive' or 'txt':
#     with open('/Users/diego/Documents/LambdaUnit3/classes/words.webarchive') as inpt:
#         dictionary = inpt.read()
#         words = dictionary.splitlines()
        
#         else:
#             with open(file) as inpt:
#                 dictionary = inpt.read()
#                 words = dictionary.splitlines()
                
#                 class Random():
                    
#                     def __init__(self, words):
#                     self.words = words
                    
#                     def select_words_range(self, number_of_words, first_word_number=0, last_word_number=None):
#                         numbers = []
#                         sentence = []
#                         if last_word_number == None:
#                             last_word_number = len(self.words)
#                             for i in range(0, number_of_words):
#                                 numbers.append(np.random.randint(first_word_number, last_word_number))
#                             for i in numbers:
#                                 sentence.append(self.words[i])
#                             return " ".join(sentence)
                            
#                     def make_df_rows(self, rows):
#                         data_for_df = np.array_split(self.words, rows)
#                         df = pd.DataFrame(data=data_for_df)
#                         return df