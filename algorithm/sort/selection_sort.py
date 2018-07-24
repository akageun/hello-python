def selection_sort(a_list):
    a_list_length = len(a_list)

    for i in range(a_list_length - 1):
        min_index = i

        for j in range(i + 1, a_list_length):  # 최소값 찾기
            if a_list[j] < a_list[min_index]:
                min_index = j

        # 위치 변경
        tmp = a_list[i]
        a_list[i] = a_list[min_index]
        a_list[min_index] = tmp

    return a_list


if __name__ == "__main__":
    a_list = list(map(int, input("Enter Numbers:").strip().split()))

    print('선택 정렬 : ', selection_sort(a_list))
