class Studant:
    def __init__(self, registration, school_grades):
        self.registration = registration
        self._school_grades = school_grades
        
    @property
    def school_grades(self):
        return self._school_grades
    
    
    @school_grades.setter
    def school_grades(self, value):
        self._school_grades = value
        