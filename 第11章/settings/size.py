# width = 800
# height = 600

_width = 800
_height = 600
def change(w, h):
    global _width
    _width = w
    global _height
    _height = h

def getWidth():
    global _width
    return _width

def getHeight():
    global _height
    return _height