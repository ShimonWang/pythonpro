def copy(src, new_path):
    file1 = open(src, 'rb+')
    file2 = open(new_path, 'wb+')

    s = file1.read()
    file2.write(s)

    file2.close()
    file1.close()


if __name__ == '__main__':
    src = 'google.jpg'
    new_path = '../chap10/copy_google.jpg'
    copy(src, new_path)
    print('文件复制完毕')
