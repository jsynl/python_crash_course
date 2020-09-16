# 游戏设置模块
class Settings():
    """ 存储《外星人》的所有设置的类"""

    def __init__(self):
        """ 初始化游戏设置 """
        # 屏幕设置
        self.title = 'Alien Invation'  # 屏幕标题
        self.screen_width = 1200  # 屏幕宽度
        self.screen_height = 750  # 屏幕高度
        self.bg_color = (230, 230, 230)  # 背景色

        # 设置飞船速度
        self.ship_speed_factor = 1.5
