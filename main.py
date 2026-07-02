from player import Player
from monster import Mushroom
from battle import BattleManager
from game import Game

# monster.py를 수정하지 않고 main.py에서 직접 클래스 정의
class BlueMushroom(Mushroom):
    def __init__(self):
        super().__init__(name="파랑버섯", hp=100, attack_power=15, defense=5)

def main():
    # 객체 생성
    player = Player()
    monster = BlueMushroom()
    battle_manager = BattleManager()
    game = Game()
    
    # 게임 시작1
    game.start()

if __name__ == "__main__":
    main()