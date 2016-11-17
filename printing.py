from reports import *

def count_games_print():
    print(count_games(file_name))
    return count_games(file_name)

#count_games_print()

def decide_print():
    year = input("Enter a year: ")
    print(decide(file_name, year))
    return decide(file_name, year)

#decide_print()

def get_latest_print():
    print(get_latest(file_name))
    return get_latest(file_name)

#get_latest_print()

def count_by_genre_print():
    genre = input("Enter a genre: ")
    print(count_by_genre(file_name, genre))
    return count_by_genre(file_name, genre)

#count_by_genre_print()

def get_line_number_by_title_print():
    title = input("Enter a title: ")
    print(get_line_number_by_title(file_name, title))
    return get_line_number_by_title(file_name, title)

#get_line_number_by_title_print()

def sort_abc_print():
    print(sort_abc(file_name))
    return sort_abc(file_name)

#sort_abc_print()

def get_genres_print():
    print(get_genres(file_name))
    return get_genres(file_name)

#get_genres_print()

def when_was_top_sold_fps_print():
    print(when_was_top_sold_fps(file_name))
    return when_was_top_sold_fps(file_name)

#when_was_top_sold_fps_print()