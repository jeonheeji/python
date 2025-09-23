from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다")


card = CardPayment()
card.pay(10000)
money = CashPayment()
money.pay(20000)
