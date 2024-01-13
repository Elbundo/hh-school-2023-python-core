from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
wines = [Wine(f'Wine{i}', i) for i in range(10)]
beers = [Beer(f'Beer{i}', i) for i in range(10)]

market = Market(wines, beers)

print(market.has_drink_with_title('Wine2'))
print(market.has_drink_with_title('Beer-1'))

print(market.get_drinks_sorted_by_title())

print(market.get_drinks_by_production_date(3, 6))
