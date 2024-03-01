class Gun:
    def __init__(self, recoil, fire_speed):
        self.recoil = recoil
        self.fire_speed = fire_speed

    def bullet_fired(self):
        print('firing from Gun')
        return self.recoil + self.fire_speed


class MachineGun:
    def __init__(self, recoil, fire_speed):
        self.recoil = recoil
        self.fire_speed = fire_speed

    def bullet_fired(self):
        print('firing from machine gun')
        return self.recoil.bullet_fired() * self.fire_speed


class LMG:
    def __init__(self, recoil, fire_speed):
        self.recoil = recoil
        self.fire_speed = fire_speed

    def bullet_fired(self):
        print('firing from LMG gun')
        return self.recoil.bullet_fired() ** self.fire_speed


base_gun = Gun(2, 2)

lmg_gun = LMG(base_gun,10)
print(lmg_gun.bullet_fired())
