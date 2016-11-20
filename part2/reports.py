from operator import itemgetter
import math

# Input file
file_name = input("Enter a filename: ")
with open(file_name) as file_name:
    text = file_name.read()

# Text indexing
text_count_game = text.split("\n")
index = [elem.strip().split("\t") for elem in text_count_game]
del index[-1]   # If you run test.py in terminal(not in VS-Code) -> use # before this line!!!
type_index = list(zip(*index))

# Report functions
def get_most_played(file_name):
    counter = 0
    played_float = []
    for i in type_index[1]:
        played_float.append(float(type_index[1][counter]))
        counter += 1
    played_million_index = max(enumerate(played_float), key=itemgetter(1))[0]
    return type_index[0][played_million_index]

def sum_sold(file_name):
    counter = 0
    played_float = []
    for i in type_index[1]:
        played_float.append(float(type_index[1][counter]))
        counter += 1
    return sum(played_float)

def get_selling_avg(file_name):
    counter = 0
    played_float = []
    for i in type_index[1]:
        played_float.append(float(type_index[1][counter]))
        counter += 1
    played_float_sum = sum(played_float)
    avg_sum = played_float_sum/len(type_index[1])
    return avg_sum

def count_longest_title(file_name):
    longest_title = 0
    for i in type_index[0]:
        if len(i) > longest_title:
            longest_title = len(i)
    return longest_title

def get_date_avg(file_name):
    date_avg = 0
    for i in type_index[2]:
        date_avg += int(i)
    return int(math.ceil((date_avg/(len(type_index[2]))/1.0))) * 1

def get_game(file_name, title):
    counter = 0
    for i in type_index[0]:
        if title == i:
            game = index[counter]
            game[1] = float(game[1])
            game[2] = int(game[2])
            return game
        counter += 1

def count_grouped_by_genre(file_name):
    genre_dict = {}
    for i in type_index[3]:
        if i not in genre_dict:
            genre_dict[i] = 1
        elif i in genre_dict:
            genre_dict[i] += 1
    return genre_dict

def get_date_ordered(file_name):
    name_date_dict = {}
    counter = 0
    for i in type_index[0]:
        name_date_dict[i] = type_index[2][counter]
        counter += 1
    name_date_dict_new = sorted(name_date_dict.items(), key=lambda t: t[0])
    name_date_dict_new_list = []
    for i in name_date_dict_new:
        name_date_dict_new_list.append(list(i))
    for i in range(len(name_date_dict_new_list)-1, 0, -1):
        for j in range(i):
            if name_date_dict_new_list[j][1] < name_date_dict_new_list[j+1][1]:
                temp = name_date_dict_new_list[j]
                name_date_dict_new_list[j] = name_date_dict_new_list[j+1]
                name_date_dict_new_list[j+1] = temp
    name_date_dict_end = []
    counter_new = 0
    for i in name_date_dict_new_list:
        name_date_dict_end.append(name_date_dict_new_list[counter_new][0])
        counter_new += 1
    return name_date_dict_end
