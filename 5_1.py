class StringVar:
 
    def __init__(self, text):
        self.text = text

    def set(self, text):
        self.text = text     

    def get(self):
        return self.text
 
a = StringVar(input('Введите текст: '))

print(a.get())