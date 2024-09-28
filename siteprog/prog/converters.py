class FourDigitYearConverter:
    """Класс конвертор для маршрута в формате: int[0-9].int[0-9].int[0-9].int[0-9]"""
    regex = "[0-9]{4}"

    def to_python(self, value):  # преобразование в int для views функции представления
        return int(value)

    def to_url(self, value):  # преобразование в str для urls
        return "%04d" % value
