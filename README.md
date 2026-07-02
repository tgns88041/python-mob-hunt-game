# 🎮 Python Mob Hunt Game

Python의 **클래스 상속(Class Inheritance)**과 **협업 워크플로우**를 학습하고 실습하기 위해 제작된 간단한 콘솔 기반 몹 잡기(몬스터 사냥) 게임 프로젝트입니다.

이 프로젝트는 다수의 개발자가 Git Branch를 나누어 플레이어 구현, 전투 시스템 기획, 게임 매니저 제어 등의 역할을 분담하여 협업하고 연동하는 실습 과정을 거쳐 완성되었습니다.

---

## 🚀 주요 기능

1. **사냥(전투) 시스템:** 플레이어와 몬스터의 능력치(공격력, 방어력)를 계산하여 데미지를 입히는 턴제 사냥 시스템을 지원합니다.
2. **다양한 몬스터 타입:** 기본 몹(`Mob`) 클래스를 상속받은 버섯(`Mushroom`), 분열 능력을 갖춘 슬라임(`Slime`), 그리고 네임드 몹인 파랑버섯(`BlueMushroom`)이 등장합니다.
3. **상태 보기:** 플레이어와 몬스터의 실시간 체력(HP) 및 능력치 정보를 상시 조회할 수 있습니다.
4. **데미지 보정 로직:** 방어력이 매우 높은 몬스터를 공격하더라도 최소 1의 고정 데미지를 입히도록 설계되어 있습니다.

---

## 📁 디렉토리 구조 및 파일 역할

```text
c:\Users\richc\python_project\python-mob-hunt-game\
│
├── main.py          # 게임의 진입점(Entry Point)이자 전체 객체 연동 담당
├── game.py          # 콘솔 메뉴 출력 및 게임의 메인 루프 제어
├── player.py        # 플레이어(Player) 클래스의 속성 및 공격/정보 메서드 정의
├── monster.py       # 몬스터(Mob, Mushroom, Slime)의 기본 클래스 및 상속 클래스들
├── battle.py        # 전투 매개체 역할 및 HP 검증(처치 판정)
└── README.md        # 프로젝트 설명서
```

### 상세 설명
* **[main.py](file:///c:/Users/richc/python_project/python-mob-hunt-game/main.py):** `Player`, `BlueMushroom`, `BattleManager` 객체를 생성하고, 이들을 `Game` 인스턴스에 안전하게 주입(Injection)하여 게임을 작동시킵니다.
* **[game.py](file:///c:/Users/richc/python_project/python-mob-hunt-game/game.py):** 사용자로부터 메뉴 입력을 받아 사냥을 진행하거나 정보를 조회하는 등의 루프 시스템을 처리합니다.
* **[player.py](file:///c:/Users/richc/python_project/python-mob-hunt-game/player.py):** 플레이어의 이름, 체력, 공격력을 보관합니다. 공격 시 `플레이어 공격력 - 몬스터 방어력`으로 작동하며, 데미지가 1 미만인 경우 최소 1 데미지를 보장합니다.
* **[monster.py](file:///c:/Users/richc/python_project/python-mob-hunt-game/monster.py):** 다양한 몬스터들의 기초 체력을 정의하고 슬라임의 분열(`split`), 버섯의 달리기/점프(`run`/`jump`) 등 특수 스킬을 보관합니다.
* **[battle.py](file:///c:/Users/richc/python_project/python-mob-hunt-game/battle.py):** 플레이어의 타격을 중개하고 몬스터가 사망했는지(HP가 0 이하인지)를 모니터링합니다.

---

## 💻 실행 방법

로컬 터미널에서 프로젝트의 루트 디렉토리로 이동한 뒤, 아래 파이썬 명령어를 입력하여 게임을 바로 실행할 수 있습니다.

```bash
python main.py
```

### 실행 예시 (콘솔 화면)
```text
★ 몹 잡기 게임을 시작합니다! ★

=== 메뉴 ===
1. 공격하기
2. 플레이어 정보 보기
3. 몬스터 정보 보기
4. 종료
원하는 메뉴 번호를 입력하세요: 
```

---

## 🛠️ 개발 기술 스택 및 협업 방식

* **Language:** Python 3
* **Version Control:** Git, GitHub
* **Collaboration Tools:** GitHub Issues, Branching Strategy (`feature/` branches), Pull Requests (PR) & Review Process