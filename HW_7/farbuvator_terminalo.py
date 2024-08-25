class ColorizerMeta(type):
    def __getattr__(cls, color):
        return cls(color)

class colorizer(metaclass=ColorizerMeta):
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }

    def __init__(self, color):
        self.color = self.COLORS.get(color, self.COLORS['reset'])
        self.color_name = color

    def __enter__(self):
        print(self.color, end='')
        print(f'Ви змінили колір на {self.color_name}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.COLORS['reset'], end='')
new_color = colorizer('red')
new_color.__enter__()
###
with colorizer.green:
    print('Цей текст зелений')
print('Цей текст у стандартному кольорі')
