from typing import Union

class Water:
    def __init__(self, mineral:bool, pH:Union[float, int]):
        """
        Создание и подготовка к работе базового класса "вода"
        :param mineral: Минеральность
        :param pH: Уровень pH

        Примеры:
        >>> Water(True, 5.5)
        """
        self.mineral = mineral
        self.pH = pH

    def __str__(self) -> str:
        """
        Магический метод, возвращающий информацию об объекте класса

        Примеры:
        >>> Water(True, 5.5)
        >>> Water.__str__()
        Вода минеральная - True. Её уровень pH составляет 5.5.
        """
        return f"Вода минеральная - {self.mineral}. Её уровень pH составляет {self.pH}."

    def __repr__(self) -> str:
        """
        Магический метод, возвращающий инициализацию объекта класса

        Примеры:
        >>> Water(True, 5.5)
        >>> Water.__repr__()
        Water(True, 5.5)
        """
        return f"{self.__class__.__name__}({self.mineral}, {self.pH})"

    def check_drinkable(self) -> str:
        """
        Метод, проверяющий пригодность воды для питья
        :return: Пригодность для питья

        Примеры:
        >>> Water(True, 10)
        >>> Water.check_drinkable()
        Вода техническая, не пригодна для питья
        """
        ...

    def change_pH(self, new_pH:Union[float, int]):
        """"
        Метод, изменяющий уровень pH воды
        :param new_pH: Новый урвоень pH
        :return: Изменение уровня pH

        Примеры:
        >>> Water(True, 10)
        >>> Water.change_pH(8.5)
        Water.pH = 8.5
        """
        ...

class WaterDelivery(Water):
    def __init__(self,mineral:bool, pH:Union[float, int], bottle:int):
        """
        Создание и подготовка к работе дочернего класса "Доставка воды"
        Класс создан для формирования параметров заказа под доставку воды
        :param mineral: Минеральность
        :param pH: Уровень pH
        :param bottle: Количество 19 литровых бутылей в заказе

        Примеры:
        >>> WaterDelivery(True, 5.5, 2)
        """
        super().__init__(mineral, pH)
        self.bottle = bottle

    def __repr__(self) -> str:
        """
        Магический метод, возвращающий инициализацию объекта класса
        Перегрузка выполнена в связи с дополнительным аргументом
        Примеры:
        >>> WaterDelivery(True, 5.5, 2)
        >>> WaterDelivery.__repr__()
        WaterDelivery(True, 5.5, 2)
        """
        return f"{self.__class__.__name__}({self.mineral}, {self.pH}, {self.bottle})"

    def change_pH(self, new_pH:Union[float, int]) -> str:
        """
        Метода, изменяющий уровень pH воды
        Перегрузка выполнена в связи с введением предупреждения пользователя
        :param new_pH: Новый урвоень pH
        :return: Изменение уровня pH; возможное предупреждение

        Примеры:
        >>> WaterDelivery(True, 5.5, 2)
        >>> Water.change_pH(10)
        Water.pH = 10
        Внимание! При указанном уровне pH воду пить нельзя.
        """

class WaterFilter(Water):
    def __init__(self,mineral:bool, pH:Union[float, int], installation:bool):
        """
        Создание и подготовка к работе дочернего класса "Водяной фильтр"
        Класс создан для формирования параметров заказа под установку водяного фильтра
        :param mineral: Минеральность
        :param pH: Уровень pH
        :param installation: Монтаж фильтра

        Примеры:
        >>> WaterFilter(True, 5.5, True)
        """
        super().__init__(mineral, pH)
        self. installation =  installation

    def __repr__(self) -> str:
        """
        Магический метод, возвращающий инициализацию объекта класса
        Перегрузка выполнена в связи с дополнительным аргументом
        Примеры:
        >>> WaterFilter(True, 5.5, True)
        >>> WaterFilter.__repr__()
        WaterFilter(True, 5.5, True)
        """
        return f"{self.__class__.__name__}({self.mineral}, {self.pH}, {self.installation}"

    def check_drinkable(self) -> str:
        """
        Метод, проверяющий пригодность воды для питья
        Перегерузка
11:41


выполнена в связи с вводом дополнительной информации пользователю
        :return: Пригодность для питья

        Примеры:
        >>> WaterFilter(True, 10, True)
        >>> WaterFilter.check_drinkable()
        Вода техническая, не пригодна для питья, нет смысла устанавливать фильтр, будет поставлен только сифон
        для минерализации
        """
        ...

if __name__ == "__main__":
    # Write your solution here
    pass