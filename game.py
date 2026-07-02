import sys
from player import Player
from monster import Mushroom, Slime

class Game:
    def __init__(self):
        # 몬스터와 플레이어 생성
        self.player = Player("용사", hp=100, attack_power=20, defense=5)
        # 기본 몬스터로 Mushroom 객체 생성 (기호에 맞춰 다른 몬스터도 가능)
        self.monster = Slime("슬라임", hp=50, attack_power=10, defense=3)
        self.battle_manager = None  # battle.py의 시스템이나 매니저에 해당하는 부분 (미사용 및 요구 사항 충족용)

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
                self.player.attack(self.monster)
                if self.monster.hp <= 0:
                    print(f"\n축하합니다! [{self.monster.name}]을(를) 물리쳤습니다!")
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