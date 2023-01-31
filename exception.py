class Except:
    @classmethod
    def check_number(cls, value: str):
        if value.replace('-', '').isdigit():
            return int(value)
        elif value.replace('-', '').replace('.', '').isdigit():
            return float(value)
        else:
            return None
