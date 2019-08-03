# 建立日期：2019.8.2
# 主题：Q-learning算法更新
# 作者：黄江南

# 二、Q-learning算法更新

# 1、要点

# 让探索者学会走迷宫.
# 黄色的是天堂 (reward 1),
# 黑色的地狱 (reward -1).
# 大多数 RL 是由 reward 导向的,
# 所以定义 reward 是 RL 中比较重要的一点.

# 2、算法的代码形式

# 首先我们先 import 两个模块, 
# maze_env 是我们的环境模块, 已经编写好了, 
# 大家可以直接在这里下载, maze_env 模块我们可以不深入研究, 
# 如果你对编辑环境感兴趣, 
# 可以去看看如何使用 python 自带的简单 GUI 模块 tkinter 来编写虚拟环境. 
# 我也有对应的教程. maze_env 就是用 tkinter 编写的. 
# 而 RL_brain 这个模块是 RL 的大脑部分

# 2.1 算法的包引入部分

import sys

sys.path.append('C:\\Users\\HJN\\AppData\\Local\\conda\\conda\\envs\\tensorflow')
sys.path.append('E:\\software Design\\python\\workset\\Q-Learning\\2、Q-learning_maze')

from maze_env import Maze
from RL_brain import QLearningTable

# 2.2 算法的迭代更新部分

def update():
    # 学习100回合
    for episode in range(100):
        # 初始化state的观测值
        observation = env.reset()

        while True:
            # 更新可视化环境
            env.render()

            # RL 大脑根据state的观测值挑选action
            action = RL.choose_action(str(observation))

            # 探索者在环境中实施这个action,
            # 并得到环境返回的下一个state观测值，
            # reward和done（是否掉下地狱或者升上天堂）
            observation_, reward, done = env.step(action)

            # RL从这个序列（state,action,reward,state_）中学习
            RL.learn(str(observation), action, reward, str(observation_))
            
            # 将下一个state的值传到下一次循环
            observation = observation_

            # 如果掉下地狱或者升上天堂，这回合就结束了
            if done:
                break
    
    # 结束游戏并关闭窗口
    print('game over')
    env.destroy()

if __name__ == "__main__":
    # 定义环境env和RL方式
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    # 开始可视化环境env
    env.after(100,update)
    env.mainloop()