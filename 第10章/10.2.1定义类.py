class ClassName:
    "类的帮助信息"
    pass


class Geese:
    """大雁类"""

    def __init__(self, beak, wing, claw):
        print("我是大雁类！我有以下特征：", self)
        print(beak)
        print(wing)
        print(claw)

    def fly(my, state):
        print(state)


beak_1 = "喙的基部较高，长度和头部的长度几乎相等"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是蹼状的"
wildGoose = Geese(beak_1, wing_1, claw_1)
wildGoose.fly("我飞行的时候，一会儿排成个人字，一会儿排成个一字")
print(wildGoose)
