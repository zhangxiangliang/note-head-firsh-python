def find_closest(look_for, target_data):
    def whats_the_differeence(first, second):
        if first == second: return(0)
        elif first < second: (first, second) = (second, first)
        return(first - second)

    max_diff = 9999999
    for each_thing in target_data:
        diff = whats_the_differeence(each_thing, look_for)
        if diff == 0:
            found_it = each_thing
        elif diff < max_diff:
            max_diff = diff
            found_it = each_thing

    return(found_it)
