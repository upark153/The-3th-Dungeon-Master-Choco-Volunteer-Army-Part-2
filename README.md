# The-3th-Dungeon-Master-Choco-Volunteer-Army-Part-2
I implemented character movement, battle, and ending with a python console window.

![image](https://user-images.githubusercontent.com/115389450/235337167-3f369075-db19-4a01-a144-a4b6d4c05acb.png)
![image](https://user-images.githubusercontent.com/115389450/235337185-10e6236d-3b08-47b3-8fad-d4feacc68e1d.png)
```
board = []
for i in range(15):
    map = []
    for j in range(15):
        map.append(" ")
    board.append(map)

def CreateMap():
    for i in range(15):
        board[0][i] = "-"
        board[14][i] = "-"
    y = 1
    while y<14:
        board[y][0] = "|"
        board[y][14] = "|"
        y += 1
    for j in board:
        print(" ".join(j))

class hero:
    x = 1
    y= 1
    player = "🤴"
    def Position(self):
        board[self.y][self.x] = self.player

Hero = hero()
Hero.Position()
CreateMap()
```
![image](https://user-images.githubusercontent.com/115389450/235337226-47c3af41-5714-470b-824c-f4a6d14d8331.png)
![image](https://user-images.githubusercontent.com/115389450/235337244-6768afcc-28e3-4122-bbbe-914f230eb7a8.png)
```
import os
import keyboard
import time
import random
import copy


def CreateMap():
    board = []
    for i in range(15):
        map = []
        for j in range(15):
            a = random.randint(1, 100)
            if a <= 70:
                a = " "  # 길
            elif 71 <= a <= 80:
                a = "!"  # 몬스터
            elif 81 <= a <= 90:
                a = "o"  # 포션
            else:
                a = "#"  # 포탈
            map.append(a)
        board.append(map)
    for i in range(15):
        board[0][i] = "-"
        board[14][i] = "-"
    y = 0
    while y<14:
        board[y][0] = "|"
        board[y][14] = "|"
        y += 1
    return board


def printboard(board):
    for k in board:
        print(" ".join(k))

def fogboard(board):
    map1 = copy.deepcopy(board)
    for i in range(1, len(map1)-1):
        for j in range(1, len(map1[i])-1):
            if not Hero.y-2 < i < Hero.y+2 or not Hero.x-2 < j < Hero.x+2:
                map1[i][j] = "@"
    for k in map1:
        print(" ".join(k))



def move_event():
    map2 = b.copy()
    for i in range(1, len(map2) - 1):
        for j in range(1, len(map2[i]) - 1):
            if map2[i][j] != Hero.player:
                map2[i][j] = random.randint(1, 100)
                if map2[i][j] <= 70:
                    map2[i][j] = " "  # 길
                elif 71 <= map2[i][j] <= 80:
                    map2[i][j] = "!"  # 몬스터
                elif 81 <= map2[i][j] <= 90:
                    map2[i][j] = "o"  # 포션
                else:
                    map2[i][j] = "#"  # 포탈
    for k in map2:
        print(" ".join(k))

def move(board):
    while 1:
        if keyboard.is_pressed(72):
            if board[Hero.y-1][Hero.x] != " ":
                board[Hero.y][Hero.x] = Hero.player
                print("이동할 수 없습니다.")
                print("현재위치 : ", Hero.y, Hero.x)
                time.sleep(0.2)
                return board
            else:
                print("▲ 방향키 입력")
                time.sleep(0.2)
                board[Hero.y][Hero.x] = " "
                Hero.y -= 1
                board[Hero.y][Hero.x] = Hero.player
                print("현재위치 : ", Hero.y, Hero.x)
                if Hero.y %3 ==0:
                    move_event()
                return board

        if keyboard.is_pressed(75):
            if board[Hero.y][Hero.x - 1] != " ":
                    # and board[Hero.y][Hero.x-1] != "X" \
                    # and board[Hero.y][Hero.x-1]!="o":
                board[Hero.y][Hero.x] = " "
                board[Hero.y][Hero.x] = Hero.player
                print("이동할 수 없습니다.")
                print("현재위치 : ", Hero.y, Hero.x)
                time.sleep(0.2)
                return board
            else:
                print("◀ 방향키 입력")
                time.sleep(0.2)
                board[Hero.y][Hero.x] = " "
                Hero.x -= 1
                board[Hero.y][Hero.x] = Hero.player
                print("현재위치 : ", Hero.y, Hero.x)
                if Hero.x %3 ==0:
                    move_event()
                return board

        if keyboard.is_pressed(77):
            if board[Hero.y][Hero.x + 1] != " ":
                board[Hero.y][Hero.x] = " "
                board[Hero.y][Hero.x] = Hero.player
                print("이동할 수 없습니다.")
                print("현재위치 : ", Hero.y, Hero.x)
                time.sleep(0.2)
                return board
            else:
                print("▶ 방향키 입력")
                time.sleep(0.2)
                board[Hero.y][Hero.x] = " "
                Hero.x += 1
                board[Hero.y][Hero.x] = Hero.player
                print("현재위치 : ", Hero.y, Hero.x)
                if Hero.x%3 ==0:
                    move_event()
                return board

        if keyboard.is_pressed(80):
            if board[Hero.y+1][Hero.x] != " ":
                board[Hero.y][Hero.x] = " "
                board[Hero.y][Hero.x] = Hero.player
                print("이동할 수 없습니다.")
                print("현재위치 : ", Hero.y, Hero.x)
                time.sleep(0.2)
                return board
            else:
                print('▼ 방향키 입력')
                time.sleep(0.2)
                board[Hero.y][Hero.x] = " "
                Hero.y += 1
                board[Hero.y][Hero.x] = Hero.player
                print("현재위치 : ", Hero.y, Hero.x)
                if Hero.y %3 ==0:
                    move_event()
                return board


# 3칸 이동할 경우의 수( y값이 감소 했을 때)
# y == y - 3
# y == y-2 and x == x-1 or y == y-2 and x == x+1
# y == y-1 and x == x-2 or y == y-1 and x == x+2
#
# 3칸 이동할 경우의 수( x값이 감소 했을 때)
# x == x - 3
# x == x-2 and y== y-1 or x == x-2 and y == y+1
# x == x-1 and y== y-2 or x == x-1 and y == y+2
#
#
# 3칸 이동할 경우의 수( x 값이 증가 했을 때)
# x == x +3
# x == x+2 and y == y-1 or x == x+2 and y == y+1
# x == x+1 and y == y-2 or x == x+1 and y == y+2
#
# 3칸 이동할 경우의 수 ( y 값이 증가 했을 때)
# y == y+3
# y == y+2 and x == x-1 or y == y+2 and x == x+1
# y == y+1 and x == x-2 or y == y+1 and x
def clear():
    os.system('cls')


class hero():
    def __init__(self):
        self.position = [1, 1]
        self.player = "C"
    x = 1
    y = 1
    player = "C"
    def Position(self):
        CreateMap()[self.y][self.x] = self.player


Hero = hero()
Hero.Position()
a = CreateMap()
b = move(a)

while True:
    printboard(a)
    fogboard(a)
    move(a)
    clear()
```

test
:-: 
<video src='https://user-images.githubusercontent.com/115389450/235337326-a21003d9-4793-4d45-a5be-85ff5128733a.mp4' width=180/></video>
