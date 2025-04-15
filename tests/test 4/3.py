class Comment:
    def __init__(self, name, date, summary):
        self.name = name
        self.date = date
        self.summary = summary
        self.approved = 0
        self.edited = 0
        self._sub_comments = []

    def get_author(self):
        return self.name

    def get_date(self):
        return self.date.split()[0]

    def get_time(self):
        return self.date.split()[-1]

    def get_text(self):
        return self.summary

    def approve(self):
        self.approved = 1

    def is_approved(self):
        return self.approved == 1

    def set_text(self, text):
        self.summary = text
        self.edited = 1
        self.approved = 0

    def is_edited(self):
        return self.edited == 1

    def __repr__(self):
        return f"{self.summary}\n[{self.name} ({self.date})]\n"

    def get_sub_comments(self):
        return self._sub_comments.copy()

    def __iadd__(self, sub_comment):
        sub_comment.set_parent(self)
        return self

    def __lt__(self, other):
        return self._is_nested_in(other, self)

    def __gt__(self, other):
        return self._is_nested_in(self, other)

    def _is_nested_in(self, parent, child):
        if child in parent._sub_comments:
            return True
        for sub in parent._sub_comments:
            if self._is_nested_in(sub, child):
                return True
        return False


class SubComment(Comment):
    def __init__(self, name, date, summary, parent=None):
        super().__init__(name, date, summary)
        self._parent = parent
        if parent is not None:
            parent._sub_comments.append(self)

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        if self._parent is not None:
            self._parent._sub_comments.remove(self)
        self._parent = parent
        if parent is not None:
            parent._sub_comments.append(self)

    def __repr__(self):
        if self._parent is None:
            return f"SubComment({self.name}, {self.get_date()}, {self.get_time()}, None)"
        else:
            parent_repr = repr(self._parent).split('\n')[0]  # Берем только первую строку родителя
            return f"SubComment({self.name}, {self.get_date()}, {self.get_time()}, {parent_repr})"


a = Comment('Вася', '23-02-2023 12:43', 'первый')
print(repr(a))
b = SubComment('Миша', '23-02-2023 12:44', 'второй', parent=a)
print(a.get_sub_comments())
print(a < b, a > b, b < a, b > a)
c = SubComment('Петя', '23-02-2023 12:54', 'третий')
print(repr(c))
b += c
print(a < b, a < c, b < c, c > a)
print(repr(c))
c.set_parent(a)
print(a < b, a < c, b < c, c > a)
print(*map(repr, a.get_sub_comments()), sep='\n')
