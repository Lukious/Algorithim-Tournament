# -*- coding: utf-8 -*-
"""

Prob : https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

로봇개발자 무지는 한 달 앞으로 다가온 카카오배 로봇경진대회에 출품할 로봇을 준비하고 있습니다. 
준비 중인 로봇은 2 x 1 크기의 로봇으로 무지는 0과 1로 이루어진 N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여
 (N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 합니다. 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로
 하며 지도 내에 표시된 숫자 0은 빈칸을 1은 벽을 나타냅니다. 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다. 
로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며, 앞뒤 구분없이 움직일 수 있습니다.

로봇이 움직일 때는 현재 놓여있는 상태를 유지하면서 이동합니다. 예를 들어, 
위 그림에서 오른쪽으로 한 칸 이동한다면 (1, 2), (1, 3) 두 칸을 차지하게 되며, 
아래로 이동한다면 (2, 1), (2, 2) 두 칸을 차지하게 됩니다. 로봇이 차지하는
 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 됩니다.

로봇은 다음과 같이 조건에 따라 회전이 가능합니다.

위 그림과 같이 로봇은 90도씩 회전할 수 있습니다. 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 
회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다. 로봇이 한 칸 이동하거나 90도 
회전하는 데는 걸리는 시간은 정확히 1초 입니다.

0과 1로 이루어진 지도인 board가 주어질 때, 로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 return 하도록
solution 함수를 완성해주세요.


board의 한 변의 길이는 5 이상 100 이하입니다.
board의 원소는 0 또는 1입니다.
로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.
"""
from ctypes import *

class ST_DATA(Structure):
    _fields_ = [("v1",c_int),
               ("v2",c_int)]
symtDat = ST_DATA(1,0)
print(symtDat.v1)
print(symtDat.v2)

class Robot(Structure):
        _fields_ = [("state",c_int), # 0:가로 1:세로
                    ("N1y",c_int),
                    ("N1x",c_int),
                    ("N2y",c_int),
                    ("N2x",c_int)]
                    
def Move_down(Robot):
    if board[Robot.N1y+1][Robot.N1x] == 0 and board[Robot.N2y+1][Robot.N2x] == 0:
        Robot.N1y = Robot.N1y + 1
        Robot.N2y = Robot.N2y + 1
    else:
        print("Unable To Move Down")
        return
    Iamhere(Robot)
    
def Move_up(Robot):
    if board[Robot.N1y-1][Robot.N1x] == 0 and board[Robot.N2y-1][Robot.N2x] == 0:
        Robot.N1y = Robot.N1y - 1
        Robot.N2y = Robot.N2y - 1
        if(Robot.N1y == -1 or Robot.N2y == -1):
            Robot.N1y = Robot.N1y + 1
            Robot.N2y = Robot.N2y + 1
            print("Unable To Move Up")
            return
    else:
        print("Unable To Move Up")
        return
    Iamhere(Robot)
    
def Move_right(Robot):
    if board[Robot.N1y][Robot.N1x+1] == 0 and board[Robot.N2y][Robot.N2x+1] == 0:
        Robot.N1x = Robot.N1x + 1
        Robot.N2x = Robot.N2x + 1
        if(Robot.N1x == 5 or Robot.N2x == 5):
            Robot.N1x = Robot.N1x - 1
            Robot.N2x = Robot.N2x - 1
            print("Unable To Move Left")
            return
    else:
        print("Unable To Move Right")
        return
    Iamhere(Robot)
        
def Move_left(Robot):
    if board[Robot.N1y][Robot.N1x-1] == 0 and board[Robot.N2y][Robot.N2x-1] == 0:
        Robot.N1x = Robot.N1x - 1
        Robot.N2x = Robot.N2x - 1
        if(Robot.N1x == -1 or Robot.N2x == -1):
            Robot.N1x = Robot.N1x + 1
            Robot.N2x = Robot.N2x + 1
            print("Unable To Move Left")
            return
    else:
        print("Unable To Move Left")
        return
    Iamhere(Robot)
        
def Iamhere (Robot):
    print("=============Stage============")
    print("N1 = ("+str(Robot.N1y)+","+str(Robot.N1x)+")")
    print("N2 = ("+str(Robot.N2y)+","+str(Robot.N2x)+")")
    
def solution(board):
    answer = 0
    robot = Robot(0,0,0,0,1)
    Iamhere(robot)

    


    return answer

#board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
board = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]	
solution(board)