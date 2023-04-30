# potion[0,0,0,0,0,0]
import random
import keyboard
import time


def key_board_move():
    # 정상적인 입력값이 나올 때까지 반복
    while True:
        # 반환 조건
        if keyboard.is_pressed('left'):
            # 입력값이 정상일 경우 정상적으로 반환
            return 'a'
        elif keyboard.is_pressed('right'):
            return 'd'
        elif keyboard.is_pressed('up'):
            return 'w'
        elif keyboard.is_pressed('down'):
            return 's'
        # 입력값이 해당 없을 경우
        else:
            # 패스 후 반복
            pass


def arr(a, b, floor, compre):
    # 임의적으로 15*15배열을 만듬 배경으로 검은색 하트를 넣음
    array = [['🖤' for col in range(15)] for row in range(15)]
    # a는 x좌표 행을 나타냄, b는 y좌표 열을 나타냄 ,초코의용이 (0,0)일때 네모서리, 네 모서리 사이, 그외의 8개가 찍히는경우 총 9가지 조건
    if a == 0 and b == 0:
        # 초코의용의 y좌표에 1을 더한값에 하트
        array[a][b + 1] = '❤'
        # 초코의용의 x좌표에 1을 더한값에 하트
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if a == 0 and 0 < b < 14:
        array[a][b - 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if 0 < a < 14 and b == 0:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if a == 14 and b == 0:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
    if a == 14 and 0 < b < 14:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
        array[a][b - 1] = '❤'
        array[a - 1][b - 1] = '❤'
    if a == 14 and b == 14:
        array[a][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a - 1][b - 1] = '❤'
    if a == 0 and b == 14:
        array[a][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b - 1] = '❤'
    if 0 < a < 14 and b == 14:
        array[a + 1][b] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a][b - 1] = '❤'
        array[a - 1][b - 1] = '❤'
    if 0 < a < 14 and 0 < b < 14:
        array[a][b - 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
        array[a - 1][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
    # 1~9까지 k값
    for k in range(1, 10):
        # 6~10까지 h값, 총 9*5 몬스터 45마리생성, 팀원과 논의로 맵크기 의 20%를 몬스터 수를 정하기로 하였음. 45마리
        for h in range(6, 11):
            # compare는 1부터 14까지 리스트를 셔플한 값임, 실행을 누를 때마다 재배치 되도록 사용
            if a - 1 <= compre[k] <= a + 1 and b - 1 <= compre[h] <= b + 1:
                # compare[k]는 x좌표, x좌표에서 1을뺀값 부터 1을 더한값까지 ,compare[h]는 y좌표, y좌표 1을 뺀값 부터 1을 더한값까지 몬스터가 표시되도록 하였음
                array[compre[k]][compre[h]] = '🐉'
    # 초코의용 생성, 초기값은 (0,0)
    array[a][b] = '🐱‍'
    # 4,5일떄만 포탈을 생성하고 6일떄는 생성안하도록
    if floor != 6:
        # 포탈생성 앞에 좌표 고정 , 뒤에좌표 floor로 한 이유는 층이 변할 때마다 랜덤으로 포탈위치를 바꾸기 위함.
        array[compre[2]][compre[floor]] = '💠'
        # array에서 생성한 배열을 15*15로 end로 붙이고 개행을 하여 배열완성하는 포문
    for i in array:
        for j in i:
            print(j, end='')
        print()
        # 리턴값으로 array를 받아서 whire_arr에서 사용하기 위함
    return array


# 1층을 통한 와일문, floor_i는 4초기값 층, compre는 1부터 14까지 셔플된 리스트-실행시마다 랜덤재배치 위함, 포션을 메인함수에서 가져옴
# uy는 의용이의 상태창
def while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn):
    # 행,x좌표
    a = 0
    # 열, y좌표
    b = 0
    # 이동을 나타내기 위한 변수
    move = 0
    # 의용이가 포탈과 만날 때까지 진행하는 반복문, 1층 반복문
    while True:
        # 방향키를 한번눌렀을 때 50%확률로 포션 획득을 위한 랜덤변수
        get = random.randint(1, 2)
        # 몇층인지 알려주는 출력문
        print(f"=={floor_i - 3}층맵==")
        # 좌변은 arr함수의 리턴값인 array를 불러오고 우변은 arr함수를 호출하기 위함
        array_while = arr(a, b, floor_i, compre)
        # keyboard를 사용하여 input 제거하고 출력문만 나타냄
        print("방향키를 입력해주세요")
        # 방향키를 한번 누를 때마다 1씩 증감하도록함
        move += 1
        print(f"{move}이동")
        # 키보드의 올바른 작동을 위해 0.1초의 시간지연을 줌
        time.sleep(0.1)
        # 1부터 13까지 랜덤값을 가지게함
        move_a = random.randint(1, 13)
        # 6부터 13까지 랜덤값을 가지게 함
        move_b = random.randint(6, 13)
        # 움직임이 3의 배수 일 때 배치가 바뀌게 하였음
        if move % 3 == 0:
            # 배열의 위치가 x좌표가 compre[0], y좌표가 compre[1] 그것을 랜덤값을 가진 move_b,move_a 로 바뀌게 하여 3턴 마다 바뀌게 하였음
            compre[0], compre[1] = compre[move_b], compre[move_a]
            compre[1], compre[7] = compre[move_b], compre[move_a]
            # 키보드 함수에서 right를 누르면 리턴값으로 d를 받기로 하였음
        if key_board_move() == 'd':
            # b가 14인경우는 벽에 닿으므로 제외하기 위한 조건
            if b < 14:
                # 오른쪽을 누르면 b에 1이 더해지므로 그위치에 몬스터가 있으면 출력문이 나오도록함
                if array_while[a][b + 1] == '🐉':
                    print("몬스터 출현했습니다")
                    # 몬스터 대결 함수를 가져오면서 매개변수로 uy, potion을 가져옴
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)
                else:
                    print("몬스터가 없습니다")
                    # 움직일떄마다 1을 더하도록함
                b += 1
                # get이란 랜덤변수는 1부터 2, 1이 될때 포션을 획득하도록 함
                if get == 1:
                    # potion[0,0]은 메인함수에서 선언하였음, 앞에 값은 포션, 뒤에 값은 엘릭서임 , 포션수를 1씩 증가하게 함
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                # 벽에 다달랐을때 값고정을 함
                b = 14
        # 왼쪽을 눌렀을때 함수에서 리턴으로 a를 가짐
        elif key_board_move() == 'a':
            # b==0을 제외하기 위함
            if b > 0:
                if array_while[a][b - 1] == '🐉':
                    print("몬스터 출현했습니다")
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)
                else:
                    print("몬스터가 없습니다")
                b -= 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                b = 0

        elif key_board_move() == 's':
            if a < 14:
                if array_while[a + 1][b] == '🐉':
                    print("몬스터 출현했습니다")
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)

                else:
                    print("몬스터가 없습니다")
                a += 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")

            else:
                a = 14

        elif key_board_move() == 'w':
            if a > 0:
                if array_while[a - 1][b] == '🐉':
                    print("몬스터 출현했습니다")
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)
                else:
                    print("몬스터가 없습니다")
                a -= 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                a = 0
        else:
            pass
        # 만약 초코의용군의 좌표(a,b)가 포탈의 위치하고 같고 floor_i가 6이 아닐때의 조건
        # floor_i는 초기값4, 1층에서는 4 2층에서는 5 3층에선 6이되므로// 1,2층에서만 발동
        if (a, b) == (compre[2], compre[floor_i]) and floor_i != 6:
            print("👏👏👏👏👏👏👏👏👏👏👏👏👏👏")
            # 브레이크를 걸어 whire_arr(1개 층을 나타내는 함수) 을 나가도록 함
            break


# 몬스터들의 클래스
class monster():
    # 이름 , hp , 공격력, 발생확률
    # 몬스터의 능력치는 성장을 안해서 recent_hp (최근 hp), normal_hp(최대 hp)등으로 분화를 안함
    def __init__(self, name, hp, power, occur_rate):
        self.name = name
        self.hp = hp
        self.power = power
        self.occur_rate = occur_rate

    # 전투하는 메서드, 타겟이라는 매개변수를 받음, 전투에서 공격하는 대상을 나타냄
    def attack(self, target):
        print("몬스터의 턴입니다")
        # 공격 받는 대상이 클래스가 되므로
        print(f'{target.name}의 현재 hp{round(target.recent_hp)} 현재 mp{round(target.recent_mp)}')
        print(f"{self.name}의 체력: {round(self.hp)}")
        print(f'{target.name}의 체력: {round(target.recent_hp)}')
        print(f"{self.name}이 {round(self.power)}만큼의 피해를 입혔습니다.")
        target.recent_hp -= self.power
        print(f'{target.name}의 체력: {round(target.recent_hp)}')
        # 공격 받는 대상이 0보다 작게되면 패배하게함
        if target.recent_hp <= 0:
            print(f'{target.name}의 체력:0')
            print(f'{target.name}은 패배하였습니다')


# 이름, 최대 hp, 현재 hp, 최대 mp, 현재 mp, 공격력
# 상속만을 위한 클래스 영웅을 나타냄
class heroes():
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        self.name = name
        self.normal_hp = normal_hp
        self.recent_hp = recent_hp
        self.normal_mp = normal_mp
        self.recent_mp = recent_mp
        self.power = power


# 영웅을 상속받는 워리어(직업)
class warrior(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    # 전투하는 메서드 공격대상이 몬스터
    def attack_skill(self, enemy):
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{enemy.hp}')
        skill_selection = int(input("0. 일반공격 1. 파워스트라이크, 2. 몸통박치기, 3.동귀어진"))
        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")
        # 마나가 없으면 일반공격을 하게 하였음
        if skill_selection == 1 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")
        # 마나가 100이상이면 스킬을 사용하게함
        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}이 (파워 스트라이크) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 1.5)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - round(self.power * 1.5)
            # 현재 mp가 100만큼 달게하였음
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        # 마나가 200미만이면 일반공격을 하게함
        if skill_selection == 2 and self.recent_mp < 200:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 2 and self.recent_mp >= 200:
            print(f"{self.name}이 (몸통박치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 2)}만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power * 2)
            self.recent_mp = round(self.recent_mp) - 200
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 3 and self.recent_mp < 300:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 3 and self.recent_mp >= 300:
            print(f"{self.name}이 (동귀어진) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 3)}만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power * 3)
            self.recent_mp = round(self.recent_mp) - 300
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        # 공격을 받고 몬스터의 피가 0 초과라면 체력을 나타내도록함
        if enemy.hp > 0:
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        # 체력이 0미만이면 죽게하였음
        else:
            print(f'{enemy.name}이(가) 죽었습니다.')
            pass


class bard(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    # 공격하는 메서드인 attack_skill에서 매개변수를 h1,h2,h3,h4를 받게함, hn은 영웅들을 이름, 영웅들의 능력치 상승을 위함
    def attack_skill(self, enemy, h1, h2, h3, h4):
        print("바드의 노래시간입니다")
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{enemy.hp}')
        skill_selection = int(input("0. 일반공격 1. 수호의 연주, 2. 죽음의 전주곡, 3.폭풍의 서곡"))
        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")
        # 바드가 스킬을 쓰면 공격력이 2퍼센트 상승됨
        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}이 (수호의연주) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            h1.power += round(h1.power * 1.02)
            h2.power += round(h2.power * 1.02)
            h3.power += round(h3.power * 1.02)
            h4.power += round(h4.power * 1.02)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 2 and self.recent_mp < 200:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 2 and self.recent_mp >= 200:
            print(f"{self.name}이 (죽음의 전주곡) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            h1.power += round(h1.power * 1.04)
            h2.power += round(h2.power * 1.04)
            h3.power += round(h3.power * 1.04)
            h4.power += round(h4.power * 1.04)
            self.recent_mp = self.recent_mp - 200
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")

        if skill_selection == 3 and self.recent_mp < 300:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 3 and self.recent_mp >= 300:
            print(f"{self.name}이 (폭풍의 서곡) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            h1.power += round(h1.power * 1.06)
            h2.power += round(h2.power * 1.06)
            h3.power += round(h3.power * 1.06)
            h4.power += round(h4.power * 1.06)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")

        if enemy.hp > 0:
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        else:
            print(f'{enemy.name}이(가) 죽었습니다.')
            pass


class medi_fighther(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    # 공격하는 메서드에서 3개의 공격스킬과 3개의 약제조 스킬을 갖게함. 약제조 스킬시 potion[0,0,0,0,0,0]에 담기위해 가져왔고 ,medi_turn은 다음턴에 사용하기 위한 리스트값
    def attack_skill(self, enemy, potion, medi_turn):
        skill_selection = int(input("0. 일반공격 1.약하게 치기, 2. 몸통박치기, 3.쎄게 치기 4.기력 포션제조 5. 활력 포션제조 6. 하프엘릭서 제조"))
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{enemy.hp}')

        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp - self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}이 (약하게 치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 1.5)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - round(self.power * 1.5)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 2 and self.recent_mp < 200:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 2 and self.recent_mp >= 200:
            print(f"{self.name}이 (몸통박치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 2)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - round(self.power * 2)
            self.recent_mp = round(self.recent_mp) - 200
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 3 and self.recent_mp < 300:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 3 and self.recent_mp >= 300:
            print(f"{self.name}이 (쎄게 치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 3)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - (self.power * 3)
            self.recent_mp = round(self.recent_mp) - 300
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 4 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")
        # 약을 제조하면 medi_turn[0]값이 1이되게 하여 다음턴에 사용 할 수 있게함
        if skill_selection == 4 and self.recent_mp > 99:
            print("기력 포션을 제조합니다")
            self.recent_mp = self.recent_mp - 100
            medi_turn[0] = 1
            potion[3] += 1
        if skill_selection == 5 and self.recent_mp <= 199:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 5 and self.recent_mp > 199:
            print("활력 포션을 제조합니다")
            self.recent_mp = round(self.recent_mp) - 200
            medi_turn[0] = 1
            potion[4] += 1
        if skill_selection == 6 and self.recent_mp <= 299:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 6 and self.recent_mp > 299:
            print("하프 엘리서를 제조합니다")
            self.recent_mp = self.recent_mp - 300
            medi_turn[0] = 1
            potion[5] += 1
        if enemy.hp > 0:
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        else:
            print(f'{enemy.name}이(가) 죽었습니다.')

        return medi_turn


class archer(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    def attack_skill(self, enemy):
        skill_selection = int(input("0.일반공격 1.폭풍활, 2.폭풍화살, 3.용의 일격"))
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{round(enemy.hp)}')

        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp) - round(self.power)
            if enemy.hp > 0:
                print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print('=' * 50)
                print(f'[{enemy.name}]가 죽었습니다.')

        if skill_selection == 1 and self.recent_mp <= 99:

            print(f"{enemy.name}의 hp:[{round(enemy.hp)}]")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다.")

            enemy.hp = round(enemy.hp) - round(self.power)
            if enemy.hp > 0:
                print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
                print(f"{enemy.name}의 남은 체력:[{round(enemy.hp)}]")

            else:
                print(f'[{enemy.name}]이(가) 죽었습니다.')

        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}가  폭풍활 사용")
            print(f'적에게 일반 공격 두번 합니다')
            print(f"{enemy.name}의 hp:{round(enemy.hp)}")
            enemy.hp = round(enemy.hp) - round(self.power * 2)
            self.recent_mp = round(self.recent_mp) - 100

            print(f"{enemy.name}에 [{round(self.power) * 2}]만큼의 피해를 입혔습니다.")
            print(f"{self.name}의 남은 mp:[{round(self.recent_mp)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}] 죽었습니다.')

        if skill_selection == 2 and self.recent_mp < 200:
            print('mp가 부족합니다')
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            print(f"{enemy.name}의 hp:{round(enemy.hp)}")

            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print('[{enemy.name}] 죽었습니다.')

        if skill_selection == 2 and self.recent_mp >= 200:

            print(f"{self.name}가 폭풍화살 사용")
            print(f"{enemy.name}의 hp:[{round(enemy.hp)}]")
            print(f"{enemy.name}에 [{round(self.power * 3)}]만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power) * 3
            self.recent_mp = round(self.recent_mp) - 200
            print(f"{self.name}의 남은 mp:[{round(self.recent_mp)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}] 죽었습니다.')

        if skill_selection == 3 and self.recent_mp < 300:
            print('mp가 부족합니다')
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            print(f"[{enemy.name}]의 hp:[{enemy.hp}]")

            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}]이(가) 죽었습니다.')

        if skill_selection == 3 and self.recent_mp >= 300:

            print(f"[{self.name}]이 용의 일격 사용")
            print(f"[{enemy.name}]의 hp:[{round(enemy.hp)}]")
            print(f"[{enemy.name}]에 [{round(self.power * 5)}]만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power * 5)
            self.recent_mp = round(self.recent_mp) - 300
            print(f"[{self.name}]의 남은 mp:[{round(self.recent_mp)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}] 죽었습니다.')

        if enemy.hp <= 0:
            print(f"[{enemy.name}]을 죽었습니다.")
        else:
            print(f"[{enemy.name}]의 hp가 [{round(enemy.hp)}]이 되었습니다.")
            pass


# 몬스터를 상속받는 일반 몬스터
class normal(monster):
    def __init__(self, name, hp, power, occur_rate):
        monster.__init__(self, name, hp, power, occur_rate)


# 몬스터를 상속받는 보스 몬스터
class boss(monster):
    def __init__(self, name, hp, power, occur_rate):
        monster.__init__(self, name, hp, power, occur_rate)


# 일반 몬스터를 상속받는 좀비 클래스
# 호출시 zombie()를 하면 이름,hp,power,occur_rate 등이 불러와짐, 호출을 위해 스테이터스창을 작성해줌
class zombie(normal):
    def __init__(self):
        self.name = '좀비'
        self.hp = random.randint(300, 500)
        self.power = 100
        self.occur_rate = 46.5


class ghoul(normal):
    def __init__(self):
        self.name = '구울'
        self.hp = random.randint(450, 700)
        self.power = 180
        self.occur_rate = 30


class skull(normal):
    def __init__(self):
        self.name = '해골'
        self.hp = random.randint(480, 800)
        self.power = 220
        self.occur_rate = 12


class bugbear(normal):
    def __init__(self):
        self.name = '버그베어'
        self.hp = random.randint(550, 900)
        self.power = 350
        self.occur_rate = 5


# 보스몬스터를 상속받는 아르헨도
class arhendo(boss):
    def __init__(self):
        self.name = '아르헨도'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class chulmom(boss):
    def __init__(self):
        self.name = '철몸'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class gubum(boss):
    def __init__(self):
        self.name = '규범이'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class minju(boss):
    def __init__(self):
        self.name = '민주석'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class ilsung(boss):
    def __init__(self):
        self.name = '일성김'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class uyoun(boss):
    def __init__(self):
        self.name = '우연이'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class diabloc(boss):
    def __init__(self):
        self.name = '디아복로'
        self.hp = random.randint(10000, 20000)
        self.power = random.randint(2500, 3000)
        self.occur_rate = 0.2


# 전사의 직업을 상속받는 초코의용군
class choco(warrior):
    def __init__(self):
        self.name = '초코의용'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


class kingtae(bard):
    def __init__(self):
        self.name = '킹기태'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


class bumgu(medi_fighther):
    def __init__(self):
        self.name = '약범규'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


class bowhunjae(archer):
    def __init__(self):
        self.name = '보우현재'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


# hn은 용사들을 의미, growth는 랜덤값, potion=[0,0,0,0,0,0] 포션을 담기 위함 g=[0,0,0,0,0,0,0] 보스몬스터를 담기위함, 메디턴은 다음텀에 사용하기 위해 메인함수에서 가져옴
def battle(h1, h2, h3, h4, growth, potion, g, medi_turn):
    # nn은 일반몬스터를 상속하기 위함
    n1 = zombie()
    n2 = ghoul()
    n3 = skull()
    n4 = bugbear()
    turn = 0
    # bn은 보스몬스터를 나타냄
    b1 = arhendo()
    b2 = chulmom()
    b3 = gubum()
    b4 = minju()
    b5 = ilsung()
    b6 = uyoun()
    b7 = diabloc()
    # 엔딩 크레딧을 위해 보스리스트를 만듬
    b_list = [b1, b2, b3, b4, b5, b6, b7]
    occur = random.randint(1, 1000)
    # 영웅의 공격대상이 일정환 확률일때 정해지도록 함
    if occur <= 465:
        mob = n1
    elif occur <= 765:
        mob = n2
    if occur <= 885:
        mob = n3
    elif occur <= 935:
        mob = n4
    elif occur <= 945:
        mob = b1
    elif occur <= 955:
        mob = b2
    elif occur <= 965:
        mob = b3
    elif occur <= 975:
        mob = b4
    elif occur <= 985:
        mob = b5
    elif occur <= 995:
        mob = b6
    elif occur <= 1000:
        mob = b7
    # 함께라면 다음턴에 먹게 하기 위함
    count = 0
    # 전투를 돌리기 위한 반복문
    while True:
        select = int(input("1.싸운다 2.포션 먹기 3.도망간다 4.기력 포션 먹기 5.활력 포션 먹기 6.하프 엘릭서 먹기 7.엘릭서 먹기 8.당신과 함께라면 먹기 "))
        # 1번을 고를떄와 몹이 영웅을 4번공격하므로 h1의 hp가 0보다 클때 진행되도록함
        if select == 1 and h1.recent_hp > 0:
            print("용사턴=======")
            # 초코의용군(클래스)이 몹(매개변수)을 공격(메서드)함
            h1.attack_skill(mob)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")
                # i가 비리스트에 있을때 까지 돌게하고 mob이 보스리스트의 순서에 맞으면 g[i]가 1이되게함
                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                # 진행상황을 알기 위한 g리스트
                print("[아르헨도, 철몸, 규범, 민주, 일성, 우연, 디아블로]", g)
                # g리스트가 모두 1로바뀌면 엔딩을 하기 위한 조건문
                if 0 not in g:
                    print("마왕군을 무찔렀습니다 !!!========")
                    print("용사팀의 승리입니다 !!!=======")
                    print("=======================")
                    exit()
                # 전투가 끝나고 포션을 획득 할 수 있도록 하였음
                potion_class(potion).liquid_get()
                # 전투가 끝나고 영웅들이 성장을 하게하는 함수를 호출함
                grooth(h1, h2, h3, h4, growth, potion)
                if count != 0:
                    potion_class(potion).ramen_recovery(h1, h2, h3, h4)
                break
            # 메디턴의 리스트를 약범규가 스킬을 사용하기 이전에 초기화 시킴
            medi_turn[0] = 0
            h2.attack_skill(mob, potion, medi_turn)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")
                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                print("[아르헨도, 철몸, 규범, 민주, 일성, 우연, 디아블로]", g)

                if 0 not in g:
                    print("마왕군을 무찔렀습니다 !!!========")
                    print("용사팀의 승리입니다 !!!=======")
                    print("=======================")
                    exit()
                grooth(h1, h2, h3, h4, growth, potion)
                if count != 0:
                    potion_class(potion).ramen_recovery(h1, h2, h3, h4)
                break

            h3.attack_skill(mob)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")
                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                print("[아르헨도, 철몸, 규범, 민주, 일성, 우연, 디아블로]", g)
                if 0 not in g:
                    print("마왕군을 무찔렀습니다 !!!========")
                    print("용사팀의 승리입니다 !!!=======")
                    print("=======================")
                    exit()
                grooth(h1, h2, h3, h4, growth, potion)
                if count != 0:
                    potion_class(potion).ramen_recovery(h1, h2, h3, h4)
                break

            h4.attack_skill(mob, h1, h2, h3, h4)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")

                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                print("[아르헨도, 철몸, 규범, 민주, 일성, 우연, 디아블로]", g)
                if 0 not in g:
                    print("마왕군을 무찔렀습니다 !!!========")
                    print("용사팀의 승리입니다 !!!=======")
                    print("=======================")
                    exit()
                grooth(h1, h2, h3, h4, growth, potion)
                if count != 0:
                    potion_class(potion).ramen_recovery(h1, h2, h3, h4)
                break

        # 포션을 선택했을떄
        if select == 2:
            hero_select = int(input('1.초코의용, 2.약범규 3.보우현재 4.킹기태  캐릭터를 선택해주세요'))
            if hero_select == 1:
                # 포션이 0개 초과 이면 포션 리커버리 메서드를 활용하여 초코의용군을 회복시킴
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h1)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass
            if hero_select == 2:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h2)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass
            if hero_select == 3:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h3)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass
            if hero_select == 4:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h4)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass

        if select == 3:
            run = random.randint(1, 10)
            if run <= 1:
                print("도망에 성공 했다")
                if count != 0:
                    potion_class(potion).ramen_recovery(h1, h2, h3, h4)
                return
            else:
                # 도망에 실패하면 몬스터가 영웅4명을 모두 공격하도록 함
                print("도망에 실패했다")
                mob.attack(h1)
                mob.attack(h2)
                mob.attack(h3)
                mob.attack(h4)
                if count != 0:
                    potion_class(potion).ramen_recovery(h1, h2, h3, h4)
                    # 용사 4명이 모두 죽으면 끝나도록함
                if h1.recent_hp <= 0 and h2.recent_hp <= 0 and h3.recent_hp <= 0 and h4.recent_hp <= 0:
                    print("용사팀의 패배입니다")
                    exit()
                    #  약범규가 약제조스킬을 사용하면 메디턴 리스트의 요소값이 1이되므로
        if select == 4 and medi_turn[0] == 1:
            if potion[3] > 0:
                # 약범규가 제조한약은 4영웅을 회복시켜서 4명의 영웅을 매개변수로 가져옴
                potion_class(potion).mana_potion(h1, h2, h3, h4)
                potion[3] -= 1
                pass
            else:
                print("포션의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                pass
            #
        if select == 5 and medi_turn[0] == 1:
            if potion[4] > 0:
                potion_class(potion).health_potion(h1, h2, h3, h4)
                potion[4] -= 1
                pass
            else:
                print("포션의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                pass
        if select == 6 and medi_turn[0] == 1:
            if potion[5] > 0:
                potion_class(potion).half_elixer(h1, h2, h3, h4)
                potion[5] -= 1
                pass
            else:
                print("포션의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                pass
            # 엘렉서를 선택할때
        if select == 7:
            if potion[1] <= 0:
                print("포션의 갯수가 0개입니다")
                pass
            else:
                # 턴의 조기값은 0 엘릭서를 쓰면 턴은 10이되고 턴이 0초과일때 몬스터턴을 스킵하도록 하였음
                potion[1] -= 1
                turn = 10
                print("엘릭서를 사용합니다")
                print("남은 무적 턴의 숫자:", turn)
                print("엘릭서 사용하고 남은 갯수", potion[1])

        if select == 8:
            if potion[2] > 0:
                potion[2] -= 1
                print("당신과 함께라면을 먹기 위해서 제조 중입니다. 다음 턴에 제조한 라면을 먹으면 모든 파티원들의 hp와 mp가 의용군 현재 hp의 50%만큼 회복됩니다.")
                count += 1
                continue
            else:
                print("라면의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                continue
                # 엘릭서를 안썻을떄는 turn=0일때 몬스터 턴이 되도록함
        if select == 1 and turn == 0:
            print("몬스터턴==============")
            # 몬스터가 영웅 1명씩 총4명을 공격하게 하였음
            mob.attack(h1)
            if h1.recent_hp <= 0:
                print("초코의용은 죽었습니다")
                # exit()
                pass
            mob.attack(h2)
            if h2.recent_hp <= 0:
                print("약범규는 죽었습니다.")
                pass
            mob.attack(h3)
            if h3.recent_hp <= 0:
                print("보우현재는 죽었습니다.")
                pass
            mob.attack(h4)
            if h4.recent_hp <= 0:
                print("킹기태는 죽었습니다.")
                pass
            if h1.recent_hp and h2.recent_hp <= 0 and h3.recent_hp <= 0 and h4.recent_hp <= 0:
                print("용사팀 패배")
                exit()
                # 턴이 0이 아니고 턴이 0보다 클때 턴이 1씩 감소하게 하였음
        elif turn > 0:
            turn -= 1
            print(f"엘릭서의 효과발동!!!!!!!! 남은 무적턴:{turn}")
            pass
        if select == 8:
            if potion[2] > 0:
                potion[2] -= 1
                print("당신과 함께라면을 먹기 위해서 제조 중입니다. 다음 턴에 제조한 라면을 먹으면 모든 파티원들의 hp와 mp가 의용군 현재 hp의 50%만큼 회복됩니다.")
                count += 1
                continue
            else:
                print("라면의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                continue
        else:
            print("잘못된 키 입력입니다 다시눌러주세요")
            pass
    return g


# 포션을 나타내는 클래스
class potion_class:
    def __init__(self, potion):
        self.potion = potion

    # 포션을 얻는 메서드, 포션을 얻을때 일정확률로 라면과 엘릭서를 생성하고, 포션얻는 메서드를 호출하기 위함
    def liquid_get(self):
        get = random.randint(1, 10)
        elixer_get = random.randint(1, 1000)
        r = random.randint(1, 10)
        # 일반 포션 획득확률
        if get <= 3:
            self.potion[0] += 1
            print(f"포션을 얻었습니다.!!!!!!! 현재 포션의 갯수:{self.potion[0]}")
            # 엘릭서 획득 확률
            if elixer_get <= 5:
                self.potion[1] += 1
                print(f"엘릭서를 얻었습니다 엘릭서의 갯수:{self.potion[1]}", )
            else:
                pass
            if r <= 3:
                self.potion[2] += 1
                print('당신과 함께라면을 획득하였습니다.')
            else:
                pass
        else:
            pass
        # return self.potion

    # 포션을 썼을때 회복을 위한 메서드
    def liquid_recovery(self, hiro):
        self.potion[0] -= 1
        print("^^^^^^")
        print('포션 갯수', self.potion[0])
        # 30%~80%를 나타내기 위함
        recovery_rate = (random.randint(3, 8) * 0.1)
        # 영웅의 현재 hp,mp기준으로 늘어나게 하도록 함
        hiro.recent_hp += (hiro.recent_hp * recovery_rate)
        print(f"포션먹고 hp:{round(hiro.recent_hp)}")
        if hiro.normal_hp < hiro.recent_hp:
            hiro.recent_hp = hiro.normal_hp
            print(f"수정 hp:{hiro.recent_hp}")
        hiro.recent_mp += (hiro.recent_mp * recovery_rate)

    def ramen_recovery(self, h1, h2, h3, h4):
        print('파티원들이 라면을 먹기 시작합니다. 의용군 현재 체력,마나 50%만큼 파티원들의 체력, 마나가 회복됩니다.')
        print(f'초코의용 회복 전 체력 : {round(h1.recent_hp)}, 마나 : {round(h1.recent_mp)}')
        print(f'약범규 회복 전 체력 : {round(h2.recent_hp)}, 마나 : {round(h2.recent_mp)}')
        print(f'보우현재 회복 전 체력 : {round(h3.recent_hp)}, 마나 : {round(h3.recent_mp)}')
        print(f'킹기태 회복 전 체력 : {round(h4.recent_hp)}, 마나 : {round(h4.recent_mp)}')
        h1.recent_hp += round(h1.recent_hp * 0.5)
        h1.recent_mp += round(h1.recent_mp * 0.5)
        if h1.recent_hp > h1.normal_hp:
            h1.recent_hp = h1.normal_hp
        if h1.recent_mp > h1.normal_mp:
            h1.recent_mp = h1.normal_mp
        h2.recent_hp += round(h1.recent_hp * 0.5)
        h2.recent_mp += round(h1.recent_mp * 0.5)
        if h2.recent_hp > h2.normal_hp:
            h2.recent_hp = h2.normal_hp
        if h2.recent_mp > h2.normal_mp:
            h2.recent_mp = h2.normal_mp
        h3.recent_hp += round(h1.recent_hp * 0.5)
        h3.recent_mp += round(h1.recent_mp * 0.5)
        if h3.recent_hp > h3.normal_hp:
            h3.recent_hp = h3.normal_hp
        if h3.recent_mp > h3.normal_mp:
            h3.recent_mp = h3.normal_mp
        h4.recent_hp += round(h1.recent_hp * 0.5)
        h4.recent_mp += round(h1.recent_mp * 0.5)
        if h4.recent_hp > h4.normal_hp:
            h4.recent_hp = h4.normal_hp
        if h4.recent_mp > h4.normal_mp:
            h4.recent_mp = h4.normal_mp
        print(f'초코의용 회복 후 체력 : {round(h1.recent_hp)}, 마나 : {round(h1.recent_mp)}')
        print(f'약범규 회복 후 체력 : {round(h2.recent_hp)}, 마나 : {round(h2.recent_mp)}')
        print(f'보우현재 회복 후 체력 : {round(h3.recent_hp)}, 마나 : {round(h3.recent_mp)}')
        print(f'킹기태 회복 후 체력 : {round(h4.recent_hp)}, 마나 : {round(h4.recent_mp)}')

    # 약범규가 제조하는 기력포션은 4명의 마나를 60퍼 채우므로 매개변수로 4명을 가져옴
    def mana_potion(self, h1, h2, h3, h4):
        print("기력 포션을 사용합니다 파티원들의 마나를 60%채웁니다")
        # 현재 mp기준으로 60퍼가 차게함 , 4명 모두 차게 설정하였음
        h1.recent_mp += (h1.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h1.normal_mp < h1.recent_mp:
            h1.recent_mp = h1.normal_mp
            print(f"수정 mp:{h1.normal_mp}")
        print("===========================")
        h2.recent_mp += (h2.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h2.normal_mp < h2.recent_mp:
            h2.recent_mp = h2.normal_mp
            print(f"수정 mp:{h2.normal_mp}")
        print("===========================")
        h3.recent_mp += (h3.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h3.normal_mp < h3.recent_mp:
            h3.recent_mp = h3.normal_mp
            print(f"수정 mp:{h3.normal_mp}")
        print("===========================")
        h4.recent_mp += (h4.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h4.normal_mp < h4.recent_mp:
            h4.recent_mp = h4.normal_mp
            print(f"수정 mp:{h4.normal_mp}")

    def health_potion(self, h1, h2, h3, h4):
        print("활력 포션을 사용합니다 파티원들의 체력을 60%채웁니다")
        h1.recent_hp += (h1.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h1.normal_hp < h1.recent_hp:
            h1.recent_hp = h1.normal_hp
            print(f"수정 hp:{h1.normal_hp}")
        print("===========================")
        h2.recent_hp += (h2.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h2.normal_hp < h2.recent_hp:
            h2.recent_hp = h2.normal_hp
            print(f"수정 hp:{h2.normal_hp}")
        print("===========================")
        h3.recent_hp += (h3.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h3.normal_hp < h3.recent_hp:
            h3.recent_hp = h3.normal_hp
            print(f"수정 hp:{h3.normal_hp}")
        print("===========================")
        h4.recent_hp += (h4.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h4.normal_hp < h4.recent_hp:
            h4.recent_hp = h4.normal_hp
            print(f"수정 hp:{h4.normal_hp}")

    def half_elixer(self, h1, h2, h3, h4):
        print("하프 엘릭서를 사용합니다 파티원들의 체력을 80%채웁니다")
        h1.recent_hp += (h1.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h1.normal_hp < h1.recent_hp:
            h1.recent_hp = h1.normal_hp
            print(f"수정 hp:{h1.normal_hp}")
        print("===========================")
        h2.recent_hp += (h2.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h2.recent_hp)}")
        if h2.normal_hp < h2.recent_hp:
            h2.recent_hp = h2.normal_hp
            print(f"수정 hp:{h2.normal_hp}")
        print("===========================")
        h3.recent_hp += (h3.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h3.recent_hp)}")
        if h3.normal_hp < h3.recent_hp:
            h3.recent_hp = h3.normal_hp
            print(f"수정 hp:{h3.normal_hp}")
        print("===========================")
        h4.recent_hp += (h4.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h4.recent_hp)}")
        if h4.normal_hp < h4.recent_hp:
            h4.recent_hp = h4.normal_hp
            print(f"수정 hp:{h4.normal_hp}")


# 4명의 영웅들을 성장시키는데 4번을 써야 하므로 성장하는 함수를 제작하였음
def grooth(h1, h2, h3, h4, growth, potion):
    h1.power += (h1.power * growth)
    h1.recent_hp += (h1.recent_hp * growth)
    h1.recent_mp += (h1.recent_mp * growth)
    h1.normal_hp += (h1.normal_hp * growth)
    h1.normal_mp += (h1.normal_mp * growth)
    h2.power += (h2.power * growth)
    h2.recent_hp += (h2.recent_hp * growth)
    h2.recent_mp += (h2.recent_mp * growth)
    h2.normal_hp += (h2.normal_hp * growth)
    h2.normal_mp += (h2.normal_mp * growth)
    h3.power += (h3.power * growth)
    h3.recent_hp += (h3.recent_hp * growth)
    h3.recent_mp += (h3.recent_mp * growth)
    h3.normal_hp += (h3.normal_hp * growth)
    h3.normal_mp += (h3.normal_mp * growth)
    h4.power += (h4.power * growth)
    h4.recent_hp += (h4.recent_hp * growth)
    h4.recent_mp += (h4.recent_mp * growth)
    h4.normal_hp += (h4.normal_hp * growth)
    h4.normal_mp += (h4.normal_mp * growth)
    return h1, h2, h3, h4, growth, potion


# 약범규 약의 다음턴을 위한 메디턴, 성장함수에서 쓰는 랜덤변수 growth, 4명의 영웅 클래스를 변수에 저장
def main():
    medi_turn = [0]
    g = [0, 0, 0, 0, 0, 0, 0]
    growth = random.randint(2, 5) * 0.01
    h1 = choco()
    h2 = bumgu()
    h3 = bowhunjae()
    h4 = kingtae()
    potion = [0, 0, 0, 0, 0, 0]
    floor_i = 4
    # 이 리스트를 이용해 몬스터, p값 생성, 맵의 초기 좌표가 (0,0)이므로 겹치지 않게 하기 위해 1부터 시작하게 하였음.
    compre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # 셔플을 주어 실행을 할떄마다 랜덤한 위치에 생성하도록 함
    random.shuffle(compre)
    # 앞에 것은 포션, 뒤에 것은 엘릭서
    # 1층에대한 함수 호출
    while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn)
    print("2층 맵을 시작합니다 ==========")
    # 층을 증가시키기 위한 증감식
    floor_i += 1
    # 2층에대한 함수 호출
    while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn)
    print("3층 맵을 시작합니다 ==========")
    floor_i += 1
    # 3층에 대한 함수 호출
    while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn)


# 1~3층이 들어가있는(while_arr)을 호출하기 위한 메인함수 호출
main()






