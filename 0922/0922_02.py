class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
        print(f"학생 {name}의 정보가 등록 되었습니다")

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.name}의 성적 {grade}점이 추가 되었습니다")

    def get_averate(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0

    def __del__(self):  # 파일을 자동으로 삭제 객체가 메모리에서 삭제될 때 호출되는 메서드
        print(f"{self.name}의 정보가 삭제되었습니다")


student1 = Student("kim", 20, "1")

student1.add_grade(70)
student1.add_grade(80)
print(student1.get_averate())

student2 = Student("lee", 20, "2")
del student2


# 인스턴스 변수, 클래스 변수
# 인스턴스 : 각 객체마다 독립적으로 가지는 변수
# 클래스 : 모든 객체가 공유하는 변수

class BankAccount:
    bank_name = "파이썬 은행"
    total_accounts = 0
    intereset_rate = 0.02

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount.total_accounts+1

        BankAccount.total_accounts += 1
        # 클래스 변수 업데이트

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금 되었습니다")
        else:
            print("입금액은 0 보다 커야합니다")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}원이 출금 되었습니다. ")
        else:
            print("돈 부족")

    def apply_interest(self):
        interest = self.balance*BankAccount.intereset_rate
        self.balance += interest
        print(f"이자 {interest}원이 적용되었습니다. 잔액 {self.balance}원")

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.intereset_rate = new_rate
        print(f"이자률 {new_rate*100}%로 변경되었습니다")

    def __del__(self):
        print("계좌를 삭제했습니다")
        BankAccount.total_accounts -= 1
        print(f"{self.owner}의 계좌 삭제")


account1 = BankAccount("홍길동", 10000)
account2 = BankAccount("김철수", 15000)
print(f"은행이름: {BankAccount.bank_name}")
print(f"총 계좌 수: {BankAccount.total_accounts}")

account1.deposit(50000)
account2.apply_interest()

BankAccount.change_interest_rate(0.03)
account1.apply_interest()


class Calculator:

    calculation_count = 0

    def __init__(self, name):
        self.name = name
        self.history = []

    # 인스턴스 메서드
    def add_to_history(self, operation, result):  # 계산기록저장
        self.history.append(f"{operation}={result}")
        Calculator.calculation_count += 1

    # 클래스 메서드
    @classmethod
    def get_total_calcultions(cls):
        return cls.calculation_count

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def multiply(a, b):
        return a*b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    def calculate_and_save(self, a, b, operation):
        if operation == "add":
            result = self.add(a, b)
            self.add_to_history(f"{a}+{b}", result)
        elif operation == "multiply":
            result = self.multiply(a, b)
            self.add_to_history(f"{a}*{b}", result)

        return result


calc1 = Calculator("계산기1")
calc2 = Calculator("계산기2")

print(Calculator.add(5, 3))
print(Calculator.is_even(5))

result = calc1.calculate_and_save(10, 20, "add")
print(result)
print(f"총계산 횟수 : {Calculator.get_total_calcultions()}")
