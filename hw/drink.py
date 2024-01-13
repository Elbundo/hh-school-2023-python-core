class Drink:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f'{{title: {self.title}, production_date: {self.production_date}}}'
