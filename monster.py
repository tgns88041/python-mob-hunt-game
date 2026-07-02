class Mob:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def attack(self):
        print(f"[{self.name}]이(가) 공격스킬을 출력했습니다.")
        print(f"{self.attack_power}의 데미지로 공격했습니다.")

    def mob_info(self):
        print(f'이름: {self.name}')
        print(f'hp: {self.hp}')
        print(f'공격력: {self.attack_power}')
        print(f'방어력: {self.defense}')

class Mushroom(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense)

    def run(self):
        print(f"{self.name}(이)가 달리기 시작했습니다.")

    def jump(self):
        print(f"{self.name}(이)가 점프합니다.")


class Slime(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense)
        self.count = 1

    def split(self):
        self.count *= 2
        print(f"{self.name}이 분열했습니다!")

    def slime_info(self):
        print(f"현재 슬라임의 개수  {self.count}마리")