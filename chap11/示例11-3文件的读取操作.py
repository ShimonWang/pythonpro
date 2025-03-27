def my_read(filename):
    file = open(filename, 'w+', encoding='utf-8')
    file.write('你好啊')
    file.seek(0)
    # s = file.read()
    # s = file.read(2)
    # s = file.readline()
    # s = file.readline(2)
    # s = file.readlines()
    file.seek(3)
    s = file.read()
    print(type(s), s)
    file.close()


if __name__ == '__main__':
    my_read('d.txt')