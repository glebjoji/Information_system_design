class StudentSummary:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name
    
    def __str__(self):
        initials = f"{self._first_name[0]}.{self._middle_name[0]}."
        return f"{self._last_name} {initials}"