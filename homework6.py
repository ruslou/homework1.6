grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades[0] = round(sum(grades[0])/len(grades[0]), 1)
grades[1] = round(sum(grades[1])/len(grades[1]), 1)
grades[2] = round(sum(grades[2])/len(grades[2]), 1)
grades[3] = round(sum(grades[3])/len(grades[3]), 1)
grades[4] = round(sum(grades[4])/len(grades[4]), 1)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
my_dict = dict(zip(sorted_students, grades))
print(my_dict)



