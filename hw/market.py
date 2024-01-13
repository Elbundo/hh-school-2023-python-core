class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.drinks = {drink.title: drink for drink in (wines + beers)}

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drinks

    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(self.drinks.values(), key=lambda d: d.title)

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return [self.drinks[title] for title in self.drinks if (self.drinks[title].production_date >= from_date) and (self.drinks[title].production_date <= to_date)]
