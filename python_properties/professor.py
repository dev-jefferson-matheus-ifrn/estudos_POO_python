class Professor:
    def __init__(self, salary):
        self.salary = salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0 or isinstance(value, str):
            self._salary = 0
        else:
            self._salary = value