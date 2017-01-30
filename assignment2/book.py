class Book:
    def __init__(self, title: str, author: str, length: int, completed: bool):
        self.title = title
        self.author = author
        self.length = length
        self.completed = completed

    def __str__(self):
        return ('{s.title} by {s.author}, {s.length} pages ({completed})'
                .format(s=self, completed=self.completed_str()))

    def completed_str(self):
        if self.completed:
            return 'completed'
        else:
            return 'required'

    def mark_completed(self):
        self.completed = True

    def is_long(self):
        return self.length >= 500
