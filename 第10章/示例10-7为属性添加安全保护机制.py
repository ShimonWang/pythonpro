class TVshow:
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show


tvshow = TVshow('正在播放《满江红》')
print('默认', tvshow.show)
tvshow.show = '正在播放《流浪地球2》'
print('修改后：', tvshow.show)