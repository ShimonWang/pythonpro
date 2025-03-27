def my_write(s):
    file = open('b.txt', 'a', encoding='utf-8')
    file.write(s)
    file.write('\n')
    file.close()


def my_write_list(file, lst):
    f = open(file, 'a', encoding='utf-8')
    f.writelines(lst)
    f.close()


if __name__ == '__main__':
    my_write('伟大的中国梦')
    my_write('北京欢迎你')

    lst = ['姓名\t', '年龄\n', '成绩\n', '张三\t', '30\t', '98']
    my_write_list('c.txt', lst)


