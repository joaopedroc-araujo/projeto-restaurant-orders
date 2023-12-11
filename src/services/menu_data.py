import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        self.source_path = source_path
        self.dishes = set()
        self._read_csv()

    def _read_csv(self):
        dishes_dict = {}
        with open(self.source_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                quantity = int(row["recipe_amount"])

                if dish_name not in dishes_dict:
                    dishes_dict[dish_name] = Dish(dish_name, price)

                ingredient = Ingredient(ingredient_name)

                dishes_dict[dish_name].add_ingredient_dependency(
                    ingredient, quantity
                )

        for dish in dishes_dict.values():
            self.dishes.add(dish)
