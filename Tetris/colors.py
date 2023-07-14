class Colors:
    grey = (25, 30, 40)
    green = (50, 230, 25)
    red = (230, 20, 20)
    orange = (225, 115, 20)
    yellow = (240, 235, 5)
    purple = (165, 0, 250)
    cyan = (21, 205, 210)
    blue = (15, 65, 215)

    @classmethod
    def get_cell_colors(cls):
        return [cls.grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]