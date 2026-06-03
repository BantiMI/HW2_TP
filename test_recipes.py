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

def test_Recipe():
    #Проверка инициализации атрибутов класса
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe = Recipe("recipe1", [Ingredient_1, Ingredient_2])
    assert recipe.title == "recipe1"
    assert recipe.ingredients == [Ingredient_1, Ingredient_2]

    #Добавление нового ингредиента
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    recipe = Recipe("recipe1", [Ingredient_1])
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe.add_ingredient(Ingredient_2)
    assert recipe.ingredients == [Ingredient_1, Ingredient_2]

    #Одинаковые ингредиенты складываются
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    recipe = Recipe("recipe1", [Ingredient_1])
    Ingredient_2 = Ingredient("Ingredient_1", 200, "kg")
    recipe.add_ingredient(Ingredient_2)
    assert recipe.ingredients == [Ingredient_1]
    assert recipe.ingredients[0].quantity == (100 + 200)

    #Проверка возврата объекта класса
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    recipe = Recipe("recipe1", [Ingredient_1])
    new_recipe = recipe.scale(ratio=20)
    assert (recipe is new_recipe) == False

    #Количество каждого ингредиента умножается
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe = Recipe("recipe1", [Ingredient_1, Ingredient_2])
    new_recipe = recipe.scale(ratio=20)
    assert new_recipe.ingredients[0].quantity == (100*20)
    assert new_recipe.ingredients[1].quantity == (200*20)

    #При передаче ratio <= 0 выбрасывается исключение
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe = Recipe("recipe1", [Ingredient_1, Ingredient_2])
    with pytest.raises(ValueError, match="Некорректный коэффициент"): #В лекциях не нашел, поэтому полез в интернет: https://habr.com/ru/companies/otus/articles/901858/
        recipe.scale(ratio=-94)

    #Проверка возврата количества уникальных ингреедиентов
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    Ingredient_3 = Ingredient("Ingredient_2", 300, "g")
    recipe = Recipe("recipe1", [Ingredient_1, Ingredient_2, Ingredient_3])
    assert len(recipe) == 2




if __name__ == "__main__":
    test_Ingredient()
    test_Recipe()