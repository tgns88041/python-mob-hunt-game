# 플레이어 클래스 정의
class Player:
    def __init__(self, name="용사", hp=100, attack_power=20):
        """
        Player 초기화 메서드
        :param name: 플레이어 이름 (str)
        :param hp: 체력 (int)
        :param attack_power: 공격력 (int)
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, monster):
        """
        몬스터를 공격하여 체력을 감소시키는 메서드
        :param monster: 공격 대상 몬스터 객체
        """
        # 데미지 계산: 플레이어 공격력 - 몬스터 방어력
        damage = self.attack_power - monster.defense
        
        # 데미지가 1보다 작으면 최소 1로 처리
        if damage < 1:
            damage = 1
            
        monster.hp -= damage
        print(f"[{self.name}]이(가) [{monster.name}]을(를) 공격하여 {damage}의 데미지를 입혔습니다!")
        
        if monster.hp < 0:
            monster.hp = 0

    def info(self):
        """
        플레이어의 현재 상태를 출력하는 메서드
        """
        print(f"--- 플레이어 상태 ---")
        print(f"이름   : {self.name}")
        print(f"체력   : {self.hp}")
        print(f"공격력 : {self.attack_power}")
        print(f"---------------------")


# 간단한 동작 확인을 위한 테스트 코드
if __name__ == "__main__":
    # 임시 몬스터 클래스 정의 (monster.py를 수정하지 않기 위해 테스트용으로 사용)
    class MockMonster:
        def __init__(self, name, hp, defense):
            self.name = name
            self.hp = hp
            self.defense = defense

    # 플레이어 생성
    player = Player("용사", hp=100, attack_power=20)
    
    # 몬스터 생성
    slime = MockMonster("슬라임", hp=30, defense=5)
    golem = MockMonster("골렘", hp=50, defense=25) # 플레이어 공격력보다 방어력이 높음 (최소 데미지 테스트용)

    print("=== 테스트 시작 ===")
    player.info()
    
    print(f"\n* 공격 전 슬라임 HP: {slime.hp}")
    player.attack(slime)
    print(f"* 공격 후 슬라임 HP: {slime.hp} (예상: 15)\n")
    
    print(f"* 공격 전 골렘 HP: {golem.hp}")
    player.attack(golem)
    print(f"* 공격 후 골렘 HP: {golem.hp} (예상: 49, 최소 데미지 1 적용)\n")
    
    player.info()
    print("=== 테스트 종료 ===")