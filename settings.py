class Settings():
    def __init__(self):
        # экран
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 20)

        # звук
        self.high_volume = 1
        self.med_volume = 0.05
        self.low_volume = 0.25
        # количество жизней
        self.ship_limit = 3

        # пуля
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (250, 10, 10)
        self.bullets_allowed = 3

        # скорость приближения врага
        self.fleet_drop_speed = 10

        # динамика ускорения
        self.alien_speed_scale = 1.1
        self.ship_speed_scale = 1.05
        self.alien_score_multiplier = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.10
        self.bullet_speed_factor = 1.55
        self.alien_speed_factor = 0.4
        self.fleet_direction = 0.4

    def increase_speed(self):
        self.ship_speed_factor *= self.ship_speed_scale
        self.bullet_speed_factor *= self.ship_speed_scale
        self.alien_speed_factor *= self.alien_speed_scale
        self.alien_score_multiplier *= 1.5
