def main(stdscr):

#定义状态变换的规则
    state_action = {
            'Init': init(),
            'Win': not_game('Win'),
            'Gameover': not_game('Gameover'),
            'Game': game()
            }

    def init():
            #初始化游戏棋盘
            return('Game')

    def not_game(state):
            #画出 GameOver 或者 Win 的界面
            #读取用户输入的action，判断是重启游戏还是结束游戏
            if action == 'Restart':
                return 'Init'
            if action == 'Exit':
                return 'Exit'

    def game():
            #画出当前棋盘状态
            #读取用户输入得到action
            if action == 'Restart':
                return 'Init'
            if action == 'Exit':
                return 'Exit'
            #if 成功移动了一步:
                    if 游戏胜利了:
                        return 'Win'
                    if 游戏失败了:
                        return 'Gameover'
            return 'Game'

    #初始化状态并开始循环
    state = 'Init'
    while state != 'Exit':
        state = state_actions[state]()
