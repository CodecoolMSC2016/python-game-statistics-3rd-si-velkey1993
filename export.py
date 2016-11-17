from reports import *
from printing import *

export_file = open("export.txt", "w")

print("\nQuestions:\n1 - How many games are in the file?\n2 - Is there a game from a given year?\n3 - Which was the latest game?\n4 - How many games do we have by genre?\n5 - What is the line number of the given game (by title)?")
print("\nExtra questions:\n6 - What is the alphabetical ordered list of the titles?\n7 - What are the genres?\n8 - What is the release date of the top sold 'First-person shooter' game?")
print("\nE - Exit")
question = input("\nEnter your question-number(1-8) or exit(E): ")

while question != 'E':
    if question == "1":
        export_file.write("How many games are in the file?\n" + (str(count_games_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "2":
        export_file.write("Is there a game from a given year?\n" + (str(decide_print())) + "\n" )
        question = input("\nEnter your question-number: ")
    elif question == "3":
        export_file.write("Which was the latest game?\n" + (str(get_latest_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "4":
        export_file.write("How many games do we have by genre?\n" + (str(count_by_genre_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "5":
        export_file.write("What is the line number of the given game (by title)?\n" + (str(get_line_number_by_title_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "6":
        export_file.write("What is the alphabetical ordered list of the titles?\n" + (str(sort_abc_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "7":
        export_file.write("What are the genres?\n" + (str(get_genres_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "8":
        export_file.write("What is the release date of the top sold 'First-person shooter' game?\n" + (str(when_was_top_sold_fps_print())) + "\n")
        question = input("\nEnter your question-number: ")
    else:
        print("Try again!")
        question = input("\nEnter your question-number: ")
export_file.close()
exit()