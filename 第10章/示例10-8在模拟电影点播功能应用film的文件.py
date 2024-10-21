class TVshow:
    list_film = ['满江红', '流浪地球2', '中国乒乓球之绝地反击', '无名']
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show

    @show.setter
    def show(self, value):
        if value in TVshow.list_film:
            self.__show = '您选择了《' + value + '》，稍后将播放'
        else:
            self.__show = ('您点播的电影不存在')


tvshow = TVshow('满江红')
print('正在播放：《', tvshow.show, "》")
print('您可以从', tvshow.list_film, "中选择要点播的电影")
tvshow.show = '流浪地球2'
print(tvshow.show)
