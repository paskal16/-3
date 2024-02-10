import doctest


class Telephone():
    def __init__(self, brand: str, battery: int, year_of_release: int):
        """
            Создание и подготовка к работе объекта "телефон"

            :param brand: Производитель телефона (Sony, Nokia, Samsung)
            :param battery: Состояние аккумулятора (от 0 до 100)
            :param year_of_release: Год выхода (c 1876 до 2024)

            Примеры:
            >>> telephone = Telephone('Samsung', 100, 2023)  # инициализация экземпляра класса
        """
        self._brand = brand #производитель не меняется
        self.battery = battery
        self.year_of_release = year_of_release #дата релиза не может быть изменена

    @property
    def brand(self):
        return self._brand

    @property
    def year_of_release(self):
        return self._year_of_release

    @year_of_release.setter
    def year_of_release(self, year_of_release: int):
        if not isinstance(year_of_release, int):
            raise TypeError
        if year_of_release > 2024 or year_of_release < 1876:
            raise ValueError
        self._year_of_release = year_of_release

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, battery: int):
        if not isinstance(battery, int):
            raise TypeError
        if battery > 100 or battery < 0:
            raise ValueError
        self._battery = battery

    def __str__(self):
        return f"Производитель {self._brand}, аккумулятор {self.battery}, год выпуска {self._year_of_release}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self._brand!r}, battery={self.battery!r}, year_of_release={self._year_of_release!r}"



    def charge(self)-> str:
        """
                Функция которая заряжает телефон

                :return: произошла ли зарядка телефона или он был заряжен

                Примеры:
                >>> telephone = Telephone('samsung', 89, 2010)
                >>> telephone.charge()
                'You have charged your device'

        """
        if self.battery < 100:
            self.battery = 100
            return 'You have charged your device'
        return 'No charging required'

    def play_music(self, duration = 2):
        """
                       Функция которая воспроизводит музыку

                       :return: можно ли включить песню. ограничения - 2 минуты из за памяти телефона

                       Примеры:
                       >>> telephone = Telephone('samsung', 89, 2010)
                       >>> telephone.play_music(1)
                       'music is playing'

        """

        self.duration = duration
        if self.duration> 2:
            return "you can't listen this song. Only 2 minutes"
        return 'music is playing'




class Smartphone(Telephone):
    def __init__(self, brand: str, battery: int, year_of_release: int, os='Android'):
        """
        Создание и подготовка к работе объекта "смарттфон"

        :param brand: Производитель телефона (Sony, Nokia, Samsung)
        :param battery: Состояние аккумулятора (от 0 до 100)
        :param year_of_release: Год выхода (c 1876 до 2024)
        :param os: Операционная система (Android, IOS)

        Примеры:
        >>> smartphone = Smartphone('Samsung', 100, 2023)  # инициализация экземпляра класса
        """
        super().__init__(brand, battery, year_of_release)
        self.os = os

    def __str__(self):
        return f"Производитель {self.brand}, аккумулятор {self.battery}, год выпуска {self.year_of_release}, ОС {self.os!r}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, battery={self.battery!r}," \
               f" year_of_release={self.year_of_release!r}, os={self.os!r}"

    def play_music(self, duration = 2):
        """
                       Функция которая воспроизводит музыку

                       :return: можно ли включить песню.

                       Примеры:
                       >>> telephone = Smartphone('samsung', 89, 2010)
                       >>> telephone.play_music(10)
                       'music is playing. You also can watch video clip for this song '

        """

        self.duration = duration
        return 'music is playing. You also can watch video clip for this song '
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
