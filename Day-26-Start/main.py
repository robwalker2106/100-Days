student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index, row)

# Keyword Method with iterrows()
new_list = {index: row for (index, row) in student_data_frame.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_letters = {row.letter: row.code for _, row in nato_df.iterrows()}
print(nato_letters)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def word_to_code(word):
    return [nato_letters[x] for x in word]


code = input("Input the word to change to code: ").upper()
print(word_to_code(code))

