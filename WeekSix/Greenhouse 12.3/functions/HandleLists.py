

my_dict = {}

def makeList(key, value):
    if key in my_dict:
        my_dict[key].insert(0, value)             
    else:
        my_dict[key] = [value]

    return my_dict.get(key, [])

def get_averaqge(list, decimal = None):
    sum = 0
    if list == []:
        return 0
    else:
        for item in list:
            sum = sum + item
    return round((sum / len(list)), decimal)

def get_maximum(list):
    max_num = 0

    if list == []:
        return 0
    else:
        for item in list:
            if item > max_num:
                max_num = item
    return max_num

def get_minimum(list):
    min_num = float('inf')

    if list == []:
        return 0
    else:
        for item in list:
            if min_num > item:
                min_num = item
    return min_num