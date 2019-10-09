class Gomoku:
    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]
        self.cur_step = 0  # 步数

    def move_lstep(self):
        # 玩家落子
        while True:
            try:
                pos_x = int(input('x:'))  # 接受玩家的输入
                pos_y = int(input('y:'))
                if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:   # 判断这个格子能否落子
                    if self.g_map[pos_x][pos_y] == 0:
                        self.g_map[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError:  # 玩家输入不正确的情况
                continue

    def game_result(self):
        # 判断游戏的结局。0为游戏进行中，1为玩家获胜，2为电脑获胜，3为平局
        pass

    def ai_move_lstep(self):
        # 电脑落子
        pass

    def show(self):
        # 显示游戏内容
        pass
