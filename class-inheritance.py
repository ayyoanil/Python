class Enemy:

    def __init__(self, val):
        self.life = val

    def __repr__(self):
        return str(self.life)

    def attack(self):
        print('Killed!!')
        self.life -= 1
        print(self.life, 'life left.')


enemy1 = Enemy(5)
print(enemy1)
enemy1.attack()
