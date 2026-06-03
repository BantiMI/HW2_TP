class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name: str = name
        self.quantity = quantity
        self.unit: str = unit

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity: float = float(quantity)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if self.name == other.name and self.unit == other.unit: return True
        return False

class Recipe:
    def __init__(self, title, ingredients):
        self.title: str = title
        self.ingredients: list[Ingredient] = []
        for ingr in ingredients:
            self.add_ingredient(ingr)
    def add_ingredient(self, ingredient: Ingredient):
        for ingr in self.ingredients:
            if ingr == ingredient:
                ingr.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)) and ratio > 0: return True
        return False

    def scale(self, ratio: float):
        if Recipe.is_valid_ratio(ratio):
            new_ingredients = []
            for i in self.ingredients:
                new_ingredients.append(Ingredient(i.name, i.quantity*ratio, i.unit))
            new = Recipe(self.title, new_ingredients)
            return new
        raise ValueError("Некорректный коэффициент")
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        v = "\n".join(str(i) for i in self.ingredients)
        return f"{self.title}:\n{v}"


class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portion: float):
        if portion <= 0:
            raise ValueError ("Количество порций должно быть положительным")
        else:
            recipe = recipe.scale(portion)
            for ingr in recipe.ingredients:
                self._items.append((ingr, recipe.title))

    def remove_recipe(self, title: str):
        new_items = []
        for ingr, tit in self._items:
            if tit != title:
                new_items.append((ingr, tit))
        self._items = new_items

    def get_list(self):
        dic = {}
        for ingr, title in self._items:
            if (ingr.name, ingr.unit) in dic:
                dic[(ingr.name, ingr.unit)] += ingr.quantity
            else:
                dic[(ingr.name, ingr.unit)] = ingr.quantity
        itog = []
        for k, v in dic.items():
            itog.append(Ingredient(k[0], v, k[1]))
        return sorted(itog, key=lambda i: i.name)

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list[Ingredient] = None):
        if ingredients is None: ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio: float):
        new_recipe = super().scale(ratio)
        new = DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)
        return new
    def __str__(self):
        v = super().__str__()
        return f"[{self.diet_type}] {v}"
