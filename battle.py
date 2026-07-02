class BattleManager:
    def is_monster_dead(self, monster):
        """몬스터가 처치되었는지 확인합니다 (HP <= 0)."""
        return monster.hp <= 0

    def player_attack(self, player, monster):
        """플레이어가 몬스터를 공격하고 결과를 출력합니다."""
        player.attack(monster)
        if self.is_monster_dead(monster):
            print(f"{monster.name}을(를) 처치했습니다!")
        else:
            print(f"{monster.name}의 남은 HP: {monster.hp}")