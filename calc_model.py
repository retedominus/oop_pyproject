class CalcModel:
    def __init__(self, arg1, arg2):
        self._x = arg1
        self._y = arg2

    def result(self):
        pass


class DivModel(CalcModel):

    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def result(self):
        return self._x / self._y


class SubModel(CalcModel):

    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def result(self):
        return self._x - self._y


class SumModel(CalcModel):

    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def result(self):
        return self._x + self._y


class MultModel(CalcModel):

    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def result(self):
        return self._x * self._y
