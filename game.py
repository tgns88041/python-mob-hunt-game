import sys
from player import Player
from monster import Slime
from battle import BattleManager

class Game:
    def __init__(self, player=None, monster=None, battle_manager=None):
        # 1. 의존성 지연 로딩을 활용해 main.py에서 정의한 BlueMushroom 객체 등을 생성할 수 있도록 지원
        from player import Player
        from battle import BattleManager
        
        self.player = player if player is not None else Player()
        self.battle_manager = battle_manager if battle_manager is not None else BattleManager()
        
        if monster is not None:
            self.monster = monster
        else:
            try:
                # main.py에서 정의한 BlueMushroom을 동적으로 가져옵니다.
                from main import BlueMushroom
                self.monster = BlueMushroom()
            except ImportError:
                # 모듈 순환 참조나 누락 시 기본 슬라임 생성
                from monster import Slime
                self.monster = Slime("슬라임", hp=50, attack_power=10, defense=3)

    def show_menu(self):
        print("\n=== 메뉴 ===")
        print("1. 공격하기")
        print("2. 플레이어 정보 보기")
        print("3. 몬스터 정보 보기")
        print("4. 종료")

    def start(self):
        print("★ 몹 잡기 게임을 시작합니다! ★")
        while True:
            self.show_menu()
            choice = input("원하는 메뉴 번호를 입력하세요: ").strip()
            
            if choice == "1":
                # battle_manager의 player_attack 메서드를 이용하여 공격을 수행하고 상태를 출력
                self.battle_manager.player_attack(self.player, self.monster)
                if self.battle_manager.is_monster_dead(self.monster):
                    print("게임을 종료합니다.")
                    break
            elif choice == "2":
                self.player.info()
            elif choice == "3":
                self.monster.mob_info()
                if hasattr(self.monster, "slime_info"):
                    self.monster.slime_info()
            elif choice == "4":
                print("게임을 종료합니다.")
                sys.exit()
            else:
                print("잘못된 입력입니다. 1~4 사이의 번호를 입력해주세요.")

if __name__ == "__main__":
    game = Game()
    game.start()