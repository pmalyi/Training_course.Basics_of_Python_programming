"""
Модуль містить клас Player.

Клас Player представляє одного гравця в грі "Морський бій" (Battleship)
і зберігає його ім'я та статистику виграних/програних ігор.
"""


class Player:
    """
    Клас Player представляє гравця гри Battleship.

    Об'єкти цього класу зберігають:
      - ім'я гравця;
      - кількість виграних ігор;
      - кількість програних ігор.
    """

    def __init__(self, player_name: str):
        """
        Конструктор класу Player.

        :param player_name: ім'я гравця.

        Атрибут _player_name ініціалізується значенням параметра
        player_name. Атрибути _games_won та _games_lost
        ініціалізуються нулями.
        """
        self._player_name: str = player_name
        self._games_won: int = 0
        self._games_lost: int = 0

    def get_games_won(self) -> int:
        """
        Повертає кількість ігор, виграних цим гравцем.

        :return: кількість виграних ігор.
        """
        # TODO: реалізувати
        raise NotImplementedError

    def get_games_lost(self) -> int:
        """
        Повертає кількість ігор, програних цим гравцем.

        :return: кількість програних ігор.
        """
        # TODO: реалізувати
        raise NotImplementedError

    def get_games_played(self) -> int:
        """
        Повертає загальну кількість зіграних ігор
        (сума виграних та програних).

        :return: загальна кількість зіграних ігор.
        """
        # TODO: реалізувати
        raise NotImplementedError

    def add_game_won(self) -> None:
        """
        Збільшує кількість виграних ігор на 1.
        """
        # TODO: реалізувати
        raise NotImplementedError

    def add_game_lost(self) -> None:
        """
        Збільшує кількість програних ігор на 1.
        """
        # TODO: реалізувати
        raise NotImplementedError

    def get_name(self) -> str:
        """
        Повертає ім'я гравця.

        :return: ім'я гравця.
        """
        # TODO: реалізувати
        raise NotImplementedError
