def sort_by_tuple_sum(lst: list[tuple]) -> list[tuple]:
    lst.sort(key=lambda x: sum(x))
    return lst

print(sort_by_tuple_sum([(7, 3), (1, 2), (4, 5), (0, 1)])) 
