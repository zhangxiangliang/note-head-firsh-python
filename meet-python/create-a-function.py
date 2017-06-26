def loop_lists (items):
    for item in items:
        if isinstance(item,list) : loop_lists(item)
        else: print(item)

