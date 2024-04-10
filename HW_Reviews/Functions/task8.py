# --------------------------------- Задача 8. -------------------------------- #
# Да се напише програма, която да намира сечението на два списъка използвайки lambda.

l1 = [1,2,3,2]
l2 = [2,3,4]

find_lists_intersection=lambda l1,l2: set(l1).intersection(set(l2))

print(find_lists_intersection(l1,l2))