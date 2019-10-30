"""

This function can be used with or without primary function.
first input should be an array of words. second input is how many rows you want 
in the dataframe.

input will be turned into a dataframe like so:
example: function(words, 10)

Note: calculate number of words before inputting to get dataframe shape you desire

words = len(words_input)
>> 60
rows = 10

words / rows will yield 6 columns

"""

# -----

# for reference. this function works when I import like so:
# from ran_words import second_function as s
# s.make_dataframe_pick_num_rows(words, 10)

# import pandas as pd
# import numpy as np

# def make_dataframe_pick_num_rows(words, rows):
#   data_for_df = np.array_split(words.split(" "), rows)
#   return pd.DataFrame(data=data_for_df)