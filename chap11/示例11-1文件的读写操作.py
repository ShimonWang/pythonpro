def my_write():
    file = open('a.txt', 'w', encoding='utf-8')
    file.write('伟大的中国梦')
    file.close()


def my_read():
    file = open('a.txt', 'r', encoding='utf-8')
    s = file.read()
    print(type(s), s)
    file.close()


if __name__ == '__main__':
    my_write()
    my_read()