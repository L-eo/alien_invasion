class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (200, 200, 200)

        # 飞船的设置
        self.ship_speed = 0.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 0, 255, 255

        # 外星人的设置
        self.alien_speed = 0.06

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变"""
        self.ship_speed = 0.5
        self.bullet_speed = 1
        self.alien_speed = 0.06

        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        self.alien_points = 50  # 计分
        self.score_scale = 1.5  # 外星人点数的提高速度

    def increase_speed(self):
        """设置提高速度和提高点数"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)