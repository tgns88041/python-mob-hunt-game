class BattleManager:
    def is_monster_dead(self, monster):
        """Checks if the monster is dead (HP <= 0)."""
        return monster.hp <= 0

    def player_attack(self, player, monster):
        """Player attacks the monster, updates state, and prints result."""
        player.attack(monster)
        if self.is_monster_dead(monster):
            print(f"{monster.name}을(를) 처치했습니다!")
        else:
            print(f"{monster.name}의 남은 HP: {monster.hp}")