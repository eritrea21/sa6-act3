def find_intersection(list1, list2):
    # Use filter() to keep only the elements in list1 that are also in list2
    intersection = list(filter(lambda x: x in list_2, list_1))
    return intersection


list_1 = [1, 2, 3, 4, 5, 10]
list_2 = [4, 5, 6, 7, 8, 9, 10]
intersection = find_intersection(list_1, list_2)
print("Intersection numbers are :", intersection)
