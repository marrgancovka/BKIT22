from faker import Faker
from lab_python_oop.Rectandle import Rectangle
from lab_python_oop.Curcle import Curcle
from lab_python_oop.Quadrate import Quadrate

def main():

    rect = Rectangle("синего", 1, 1)
    curc = Curcle("зеленого", 1)
    quadr = Quadrate("красного", 1)
    print(rect)
    print(curc)
    print(quadr)

    fake = Faker()
    print(fake.sentence())


if __name__ == "__main__":
    main()