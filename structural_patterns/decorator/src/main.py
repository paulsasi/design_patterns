import person

if __name__ == '__main__':

    print("Stage 0")

    paul = person.Primitive(name="paul", age=25)
    paul = person.Industry(paul)
    paul = person.Teacher(paul)
    print(paul.describe())

    isma = person.Primitive(name="isma", age=25)
    isma = person.Teacher(isma)
    isma = person.Industry(isma)
    print(isma.describe())

    mario = person.Primitive(name="mario", age=25)
    print(mario.describe())

    print("Types")
    print(type(paul))
    print(type(isma))
    print(type(mario))