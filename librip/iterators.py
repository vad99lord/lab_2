# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']
        self.items = items
        self.pos = -1

    def check_item(self):

        if self.ignore_case and self.items[self.pos - 1] != self.items[self.pos]:
            return True
        if not self.ignore_case and self.items[self.pos - 1].casefold() != self.items[self.pos].casefold():
            return True
        return False

    def __next__(self):
        # Нужно реализовать __next__
        self.pos += 1
        if self.pos == 0:
            return self.items[self.pos]
        while self.pos < len(self.items):
            if self.check_item():
                return self.items[self.pos]
            self.pos += 1
        raise StopIteration

    def __iter__(self):
        return self
