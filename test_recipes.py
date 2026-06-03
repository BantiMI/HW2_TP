import pytest
from HW2 import *

def test_Ingredient():
    #Проверка инициализации атрибутов
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    assert Ingredient_1.name == "Ingredient_1"
    assert Ingredient_1.quantity == 100
    assert Ingredient_1.unit == "kg"

    #Проверка метода __str__
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    assert Ingredient_1.__str__() == "Ingredient_1: 100.0 kg"

    #Проверка метода __eq__
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_1", 200, "kg")
    assert (Ingredient_1 == Ingredient_2) == True

    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 100, "kg")
    assert (Ingredient_1 == Ingredient_2) == False

    Ingredient_1 = Ingredient("Ingredient_1", 100, "g")
    Ingredient_2 = Ingredient("Ingredient_1", 100, "kg")
    assert (Ingredient_1 == Ingredient_2) == False




if __name__ == "__main__":
    test_Ingredient()