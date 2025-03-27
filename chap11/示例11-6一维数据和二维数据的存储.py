def my_write():
    lst = ['张三', '李四', '王五', '陈六', '麻七']
    with open('student.csv', 'w') as file:
        file.write(','.join(lst))


def my_read():
    with open('student.csv', 'r') as file:
        s = file.read()
        lst = s.split(',')
        print(lst)


def my_write_table():
    lst = [
        ['商品', '单价', '采购数量'],
        ['水杯', '98.5', '20'],
        ['鼠标', '89', '100']
    ]
    with open('table.csv', 'w', encoding='utf-8') as file:
        for item in lst:
            line = ','.join(item)
            file.write(line)
            file.write('\n')


def my_read_table():
    data = []
    with open('table.csv', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        # print(type(lst), lst)
        for item in lst:
            new_lst = item[:len(item)-1].split(',')
            data.append(new_lst)

    print(data)


if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()