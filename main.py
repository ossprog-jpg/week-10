import random

fileHeroes = "heroes.txt"
fileVillains = "villains.txt"
fileWeapons = "weapons.txt"

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
    return random.choice(data).strip()

randomHero = load_data(fileHeroes)
randomVillain = load_data(fileVillains)

randomHeroWeapon = load_data(fileWeapons)
randomVillainWeapon = load_data(fileWeapons)

while randomHeroWeapon == randomVillainWeapon:
    randomVillainWeapon = load_data(fileWeapons)

heroHealth = 100
villainHealth = 100

print("Hero:", randomHero, "-", randomHeroWeapon)
print("Villain:", randomVillain, "-", randomVillainWeapon)
print()

while heroHealth > 0 and villainHealth > 0:

    damage = len(randomHeroWeapon)
    villainHealth -= damage

    print(randomHero, "attacks", randomVillain, "with", randomHeroWeapon)
    print("Damage:", damage)
    print("Villain health:", villainHealth)
    print()

    if villainHealth <= 0:
        print(randomHero, "wins!")
        break

    damage = len(randomVillainWeapon)
    heroHealth -= damage

    print(randomVillain, "attacks", randomHero, "with", randomVillainWeapon)
    print("Damage:", damage)
    print("Hero health:", heroHealth)
    print()

    if heroHealth <= 0:
        print(randomVillain, "wins!")