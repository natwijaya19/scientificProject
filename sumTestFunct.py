# sum_integers_list.py
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list_of_integers = [1, 2, 3, 5]
print(my_sum(1, 2, 3, 5))

