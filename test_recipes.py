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


def test_ShoppingList():
    # Проверка выбрасывания исключения при порции <= 0
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe = Recipe("recipe1", [Ingredient_1, Ingredient_2])
    lis = ShoppingList()
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        lis.add_recipe(recipe, 0)

    # Проверка добавления рецента в список
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe = Recipe("recipe1", [Ingredient_1, Ingredient_2])
    lis = ShoppingList()
    lis.add_recipe(recipe, 1)
    assert lis._items == [(Ingredient_1, "recipe1"), (Ingredient_2, "recipe1")]

    # Проверка удаление всех ингредиентов по рецепту
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_2", 200, "g")
    recipe_1 = Recipe("recipe1", [Ingredient_1])
    recipe_2 = Recipe("recipe2", [Ingredient_2])
    lis = ShoppingList()
    lis.add_recipe(recipe_1, 1)
    lis.add_recipe(recipe_2, 2)
    lis.remove_recipe("recipe1")
    assert lis._items == [(Ingredient_2, "recipe2")]

    # Если такого рецепта нет - ничего не меняется
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    recipe_1 = Recipe("recipe1", [Ingredient_1])
    lis = ShoppingList()
    lis.add_recipe(recipe_1, 1)
    lis.remove_recipe("recipe2")
    assert lis._items == [(Ingredient_1, "recipe1")]

    # Одинаковые ингредиенты из разных рецептов суммируются
    Ingredient_1 = Ingredient("Ingredient_1", 100, "kg")
    Ingredient_2 = Ingredient("Ingredient_1", 200, "kg")
    recipe_1 = Recipe("recipe1", [Ingredient_1])
    recipe_2 = Recipe("recipe2", [Ingredient_2])
    lis = ShoppingList()
    lis.add_recipe(recipe_1, 1)
    lis.add_recipe(recipe_2, 2)
    assert lis.get_list() == [Ingredient("Ingredient_1", 500.0, "kg")]

    # Возвращаемый список отсортирован по названию
    Ingredient_1 = Ingredient("Ааа", 100, "kg")
    Ingredient_2 = Ingredient("Ббб", 200, "kg")
    recipe_1 = Recipe("recipe1", [Ingredient_1])
    recipe_2 = Recipe("recipe2", [Ingredient_2])
    lis = ShoppingList()
    lis.add_recipe(recipe_1, 1)
    lis.add_recipe(recipe_2, 2)
    assert lis.get_list() == [Ingredient("Ааа", 100.0, "kg"), Ingredient("Ббб", 400.0, "kg")]

    # Два списка корректно объединяются
    Ingredient_1 = Ingredient("Ааа", 100, "kg")
    Ingredient_2 = Ingredient("Ббб", 200, "kg")
    recipe_1 = Recipe("recipe1", [Ingredient_1])
    recipe_2 = Recipe("recipe2", [Ingredient_2])
    lis_1 = ShoppingList()
    lis_2 = ShoppingList()
    lis_1.add_recipe(recipe_1, 1)
    lis_2.add_recipe(recipe_2, 2)
    lis = lis_1 + lis_2
    assert lis.get_list() == [Ingredient("Ааа", 100.0, "kg"), Ingredient("Ббб", 400.0, "kg")]

    # Исходные списки не изменяются
    redient_2 = Ingredient("Ббб", 200, "kg")
    recipe_1 = Recipe("recipe1", [Ingredient_1])
    recipe_2 = Recipe("recipe2", [Ingredient_2])
    lis_1 = ShoppingList()
    lis_2 = ShoppingList()
    lis_1.add_recipe(recipe_1, 1)
    lis_2.add_recipe(recipe_2, 2)
    lis = lis_1 + lis_2
    assert lis_1.get_list() == [Ingredient("Ааа", 100.0, "kg")]
    assert lis_2.get_list() == [Ingredient("Ббб", 400.0, "kg")]



if __name__ == "__main__":
    test_Ingredient()
    test_Recipe()
    test_ShoppingList()