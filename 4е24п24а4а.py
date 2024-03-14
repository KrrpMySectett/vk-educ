def mid(data_in):
    list_num = list(map(int, data_in.split()))
    return sum(list_num) / len(list_num)
    
while True:
    data = input()
    if not data:
        break
    print(mid(data))