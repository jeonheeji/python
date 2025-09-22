class Student:
    def __init__(self, score):
        self.__score = score

    @property
    def set_score(self):
        return self.__score

    @set_score.setter
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError
        self.__set_score = score


sc = Student(80)
print(sc.set_score)
sc.set_score = 120
print(sc.set_score)
