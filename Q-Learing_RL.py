# 建立日期：2019.8.1
# 主题：Q-Learning算法学习
# 作者：黄江南

# 一、小例子
# date:2019.8.1
# author:morvanzhou
# editor:hjn

# 1、要点

# -o---T
# T 就是宝藏的位置, o 是探索者的位置
# Q-learning 是一种记录行为值 (Q value) 的方法, 
# 每种在一定状态的行为都会有一个值 Q(s, a), 
# 就是说 行为 a 在 s 状态的值是 Q(s, a).
# s 在上面的探索者游戏中, 就是 o 所在的地点了. 
# 而每一个地点探索者都能做出两个行为 left/right, 这就是探索者的所有可行的 a 啦.
# 如果在某个地点 s1, 探索者计算了他能有的两个行为, a1/a2=left/right, 
# 计算结果是 Q(s1, a1) > Q(s1, a2), 那么探索者就会选择 left 这个行为. 
# 这就是 Q learning 的行为选择简单规则.

# 2、预设值

import numpy as np
import pandas as pd
import time

np.random.seed(2)  # reproducible

N_STATES = 6  # 1维世界的宽度
ACTIONS = ['left', 'right']  # 探索者的可用动作
EPSILON = 0.9  # 贪婪度 greedy
ALPHA = 0.1  # 学习度
GAMMA = 0.9  # 奖励递减度
MAX_EPISODES = 13  # 最大回合数
FRESH_TIME = 0.3  # 移动间隔时间

# 2、Q表


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # q_talbe的值初始化为0
        columns=actions,  # columns对应的是行为名称
    )
    return table

# q_table:
# """
#    left  right
# 0   0.0    0.0
# 1   0.0    0.0
# 2   0.0    0.0
# 3   0.0    0.0
# 4   0.0    0.0
# 5   0.0    0.0
# """

# 3、定义动作

# 在某个state地点，选择行为


def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 选出这个state的所有action值
    if(np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非贪婪 or 这个state还没有探索过
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.argmax()  # 贪婪模式
    return action_name

# 4、环境反馈 S_, R

# S_:下一个state
# S:上一个state
# reward规则：只有当 o 移动到了 T, 探索者才会得到唯一的一个奖励,
# 奖励值 R=1, 其他情况都没有奖励.

def get_env_feedback(S,A):
    # This is how agent will interact with the environment
    if A == 'right': # move right
        if S == N_STATES - 2: # terminate
            S_ = "terminal"
            R = 1
        else:
            S_ = S+1
            R = 0
    else: # move left
        R = 0
        if S == 0:
            S_ = S # reach the wall
        else:
            S_ = S - 1
    return S_,R

# 5、环境更新

def update_env(S,episode,step_counter):
    #This is how environment be updated
    env_list = ['-']*(N_STATES-1) +['T'] # '------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1,step_counter)
        print('\r{}'.format(interaction),end='')
        time.sleep(2)
        print('\r                       ',end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction),end='')
        time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_STATES,ACTIONS) # 初始化 q_table
    for episode in range(MAX_EPISODES): # 回合
        step_counter = 0
        S = 0 # 回合初始位置
        is_terminated = False # 是否回合结束
        update_env(S,episode,step_counter) # 环境更新
        while not is_terminated:

            A = choose_action(S,q_table) # 选行为
            S_, R = get_env_feedback(S,A) # 实施行为并得到环境的反馈
            q_predict = q_table.loc[S,A] # 估算的（状态-行为）值
            if S_ != 'terminal':
                q_target = R +GAMMA * q_table.iloc[S_,:].max() # 实际的（状态-行为）值（回合没结束）
            else:
                q_target = R # 实际的（状态-行为）值（回合结束）
                is_terminated = True # terminate this episode
            
            q_table.loc[S,A] += ALPHA * (q_target - q_predict) # q_table 更新
            S = S_ # 探索者移动到下一个state
            
            update_env(S, episode, step_counter+1) # 环境更新

            step_counter += 1
    return q_table

# 主函数

if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)