# Input file
file_name = input("Enter a text filename: ")
with open(file_name) as f:
    text = f.read()

# Text indexing
text_count_game = text.split("\n")
index = [elem.strip().split("\t") for elem in text_count_game]
del index[-1]
type_index = list(zip(*index))

# Report functions
def count_games(file_name):
    return len(index)

def decide(file_name, year):
    if str(year) in type_index[2]:
        return True
    else:
        return False

def get_latest(file_name):
    year = max(type_index[2])
    year_index = type_index[2].index(year)
    return type_index[0][year_index]

def count_by_genre(file_name, genre):
    return type_index[3].count(genre)

def get_line_number_by_title(filename, title):
    return (type_index[0].index(title))+1

def sort_abc(file_name):
    return sorted(type_index[0])

def get_genres(file_name):
    genres = sorted(type_index[3])
    genres_new = []
    for i in genres:
        if i not in genres_new:
            genres_new.append(i)
    genres_new = sorted(genres_new, key=lambda s: s.lower())
    return genres_new

def when_was_top_sold_fps(file_name):
    counter = 0
    top_sold = []
    for i in type_index[3]:
        if i == "First-person shooter":
            top_sold.append(float(type_index[1][counter]))
        counter += 1
    counter_new = 0
    for i in type_index[1]:
        if float(i) == max(top_sold):
            year = type_index[2][counter_new]
            return int(year)
        counter_new += 1