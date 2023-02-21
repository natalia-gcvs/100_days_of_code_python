# def backwards(int):
#     int_list = list(str(int))
#     for i in range(int_list, -1):
#         return int_list

list_str = list(str(12345))
int_list = []
for i in list_str:
    i = int(i)
    int_list.append(i)


def backwards(int):
    list_str = list(str(int))
    int_list = []
    for i in list_str:
        i = int(i)
        int_list.append(i)

    for i in range(int_list[-1], int_list[0], -1):
        backwards_list.append(i)
    return backwards_list




print(backwards(36790))