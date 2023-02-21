import random

numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
print(new_list)

name = 'Natalia'
new_list = [letter for letter in name]
print(new_list)

new_list = [n * 2 for n in range(1, 5)]
print(new_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

import random
import pandas as pd

# student_scores = {name: random.randint(1, 100) for name in names}
# print(student_scores)
student_scores = {'student': ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'],
                  'scores': [56, 45, 67, 78, 63, 39]}
# passed_students = {name: score for (name, score) in student_scores.items() if score > 50}
# print(passed_students)

student_scores_df = pd.DataFrame(student_scores)

for (key, row) in student_scores_df.iterrows():
    print(row.student)
