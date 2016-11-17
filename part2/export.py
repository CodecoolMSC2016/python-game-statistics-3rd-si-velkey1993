from reports import *
from printing import *

export_file = open("/home/pata/Desktop/Ubuntu/Máté doksik/Codecool - Harmadik otthoni hét/python-game-statistics-3rd-si-velkey1993-master/part2/export.txt", "w")

print("\nQuestions:\n1 - What is the title of the most played game?\n2 - How many copies have been sold total?\n3 - What is the average selling?\n4 - How many characters long is the longest title?\n5 - What is the average of the release dates?\n6 - What properties has a game?")
print("\nExtra questions:\n7 - How many games are there grouped by genre?\n8 - What is the date ordered list of the games?")
print("\nE - Exit")
question = input("\nEnter your question-number(1-8) or exit(E): ")

while question != 'E':
    if question == "1":
        export_file.write("What is the title of the most played game?\n" + (str(get_most_played_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "2":
        export_file.write("How many copies have been sold total?\n" + (str(sum_sold_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "3":
        export_file.write("What is the average selling?\n" + (str(get_selling_avg_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "4":
        export_file.write("How many characters long is the longest title?\n" + (str(count_longest_title_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "5":
        export_file.write("What is the average of the release dates?\n" + (str(get_date_avg_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "6":
        export_file.write("What properties has a game?\n" + (str(get_game_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "7":
        export_file.write("How many games are there grouped by genre?\n" + (str(count_grouped_by_genre_print())) + "\n")
        question = input("\nEnter your question-number: ")
    elif question == "8":
        export_file.write("What is the date ordered list of the games?\n" + (str(get_date_ordered_print())) + "\n")
        question = input("\nEnter your question-number: ")
    else:
        print("Try again!")
        question = input("\nEnter your question-number: ")
export_file.close()
exit()