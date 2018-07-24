def bubble_sort(a_list, order_type):
    a_list_length = len(a_list)

    for i in range(a_list_length - 1, 0, -1):

        for j in range(i):
            if sort_order_type(a_list[j], a_list[j + 1], order_type):
                tmp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = tmp

    return a_list


def sort_order_type(pre_val, next_val, order_type):
    if order_type == 'DESC':
        return pre_val < next_val

    elif order_type == 'ASC':
        return pre_val > next_val


if __name__ == "__main__":
    a_list = list(map(int, input("Enter Numbers:").strip().split()))

    print('ASC : ', bubble_sort(a_list, 'ASC'))
    print('DESC : ', bubble_sort(a_list, 'DESC'))
