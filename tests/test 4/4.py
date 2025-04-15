class ParentTypeError(TypeError):
    pass


class ParentRecursionError(RecursionError):
    pass


class Comment:
    def __init__(self, name, date, summary):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(summary, str):
            raise TypeError("Summary must be a string")

        try:
            date_part, time_part = date.split()
            day, month, year = map(int, date_part.split('-'))
            hours, minutes = map(int, time_part.split(':'))

            if not (1 <= month <= 12 and 1 <= day <= 31 and 0 <= hours <= 23 and 0 <= minutes <= 59):
                raise ValueError("Invalid date values")
        except ValueError:
            raise ValueError("Invalid date format, expected 'DD-MM-YYYY HH:MM'")

        self.name = name
        self.date = date
        self.summary = summary
        self.approved = 0
        self.edited = 0
        self.sub_comments = []
        self.parent = None

    def _validate_string(self, value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")

    def _validate_date(self, date_str):
        try:
            date_part, time_part = date_str.split()
            day, month, year = map(int, date_part.split('-'))
            hours, minutes = map(int, time_part.split(':'))

            if not (1 <= month <= 12 and 1 <= day <= 31 and 0 <= hours <= 23 and 0 <= minutes <= 59):
                raise ValueError
        except (ValueError, AttributeError):
            raise ValueError("Invalid date format or impossible date")

    def get_author(self):
        return f"{self.name}"

    def get_date(self):
        return f"{self.date.split()[0]}"

    def get_time(self):
        return f"{self.date.split()[-1]}"

    def get_text(self):
        return f"{self.summary}"

    def approve(self):
        self.approved = 1

    def is_approved(self):
        return self.approved == 1

    def set_text(self, text):
        self._validate_string(text, "Text")
        self.summary = text
        self.edited = 1
        self.approved = 0

    def is_edited(self):
        return self.edited == 1

    def get_sub_comments(self):
        return list(self.sub_comments)

    def __iadd__(self, sub_comment):
        if isinstance(sub_comment, SubComment):
            sub_comment.set_parent(self)
        return self

    def __lt__(self, other):
        if isinstance(other, SubComment):
            return other.is_child_of(self)
        return False

    def __gt__(self, other):
        if isinstance(other, Comment):
            return self.is_child_of(other)
        return False

    def is_child_of(self, potential_parent):
        return False

    def __repr__(self):
        return f"Comment({self.name}, {self.get_date()}, {self.get_time()})"

    def print_tree(self, level=0):
        indent = "    " * level
        print(f"{indent}{repr(self)}")
        for sub in sorted(self.sub_comments, key=lambda x: x.get_time()):
            sub.print_tree(level + 1)


class SubComment(Comment):
    def __init__(self, name, date, summary, parent=None):
        super().__init__(name, date, summary)
        if parent is not None:
            self.set_parent(parent)

    def set_parent(self, parent):
        if not (isinstance(parent, (Comment, SubComment)) or parent is None):
            raise ParentTypeError("Parent must be Comment, SubComment or None")

        if parent is not None and parent.is_child_of(self):
            raise ParentRecursionError("Parent cannot be a child of this comment")

        if self.parent is parent:
            return

        if self.parent is not None:
            self.parent.sub_comments.remove(self)

        self.parent = parent

        if parent is not None:
            parent.sub_comments.append(self)

    def is_child_of(self, potential_parent):
        if self.parent is potential_parent:
            return True
        if isinstance(self.parent, SubComment):
            return self.parent.is_child_of(potential_parent)
        return False

    def __repr__(self):
        parent_repr = repr(self.parent) if self.parent is not None else "None"
        return f"SubComment({self.name}, {self.get_date()}, {self.get_time()}, {parent_repr})"
