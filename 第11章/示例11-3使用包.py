import settings.size
if __name__ == '__main__':
    print(settings.size.width)
    print(settings.size.height)

from settings import size
if __name__ == '__main__':
    print(size.width)
    print(size.height)

from settings.size import width,height
if __name__ == '__main__':
    print(width)
    print(height)