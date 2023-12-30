import pandas
nato_alphabets_data = pandas.read_csv("nato_alphabets.csv")
nato_dictionary = {row.letters : row.words for (index,row) in nato_alphabets_data.iterrows()}
print(nato_dictionary)
user_input = input("Your message : ").upper()
# final_list = [nato_dictionary[item] for item in user_input if item >= 'A' and item <= 'Z']
final_list = [nato_dictionary[item] for item in user_input if item in nato_dictionary]
print(final_list)