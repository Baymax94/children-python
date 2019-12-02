class Bird():
    def __init__(self, color):
        self.color = color

    def say(self):
        print('一只%s的小鸟在叽叽喳喳地叫' % self.color)

b = Bird('蓝色')
b.say()
