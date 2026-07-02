import sys
from player import Player
from monster import Mushroom
from battle import BattleManager
from game import Game

# monster.py를 수정하지 않고 main.py에서 직접 클래스 정의
class BlueMushroom(Mushroom):
    def __init__(self):
        super().__init__(name="파랑버섯", hp=100, attack_power=15, defense=5)

def main():
    # 1. 객체 생성
    player = Player("용사", hp=100, attack_power=20)
    monster = BlueMushroom()
    battle_manager = BattleManager()
    game = Game(player=player, monster=monster)
    
    # 2. 생성한 객체를 game에 주입
    game.player = player
    game.monster = monster
    game.battle_manager = battle_manager
    
    # 3. 게임 시작
    game.start()

if __name__ == "__main__":
    main()