def cooking_time(eggs):
    max_eggs = 8
    boil = 5
    if eggs == 0:
        return 0
    if eggs == max_eggs:
        return 5
    if eggs < max_eggs:
        return 5
    while eggs > max_eggs:
       eggs - 8
       boil = boil + 5
    return boil 

      