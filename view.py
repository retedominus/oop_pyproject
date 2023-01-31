class View:

    @staticmethod
    def show_title(title: str):
        print(title)

    @staticmethod
    def show_result(value):
        if value is not None:
            print('Результат: ', value)

    @staticmethod
    def show_options(options: dict):
        for item in options:
            print('{} - {}'.format(item, options[item]))
