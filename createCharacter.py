import random
def generateHealth():
    return random.randint(300,900)

def generateAttack():
    return random.randint(20,60)

def generateDefence():
    return random.randint(0,15)

def generateSpeed():
    return random.randint(1,10)

def createCharacter():
    name = generateName().strip()
    health = generateHealth()
    attack = generateAttack()
    defence = generateDefence()
    speed = generateSpeed()
    character = (name, health, attack, defence, speed)
    return character

def generateName():
    f = open("names.data")
    rand = random.randint(1,159)
    readName = f.readlines()
    return readName[rand]

def main():
    for x in range(5):
        character = createCharacter()
        print(character)

    

if __name__ == '__main__':
    main()