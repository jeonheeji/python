# 스택

# push(data) 스택의 맨 위에 요소 추가
# pop() 스택의 맨 위 요소 제거 및 반환
# peek()/top() 맨위 요소 확인 (제거하지 않음)
# is_empty() 스택이 비어있는지 확인
# size() 스택의 요소 개수 반환

# => 모든 시간 복잡도 0(1)

# 리스트로 스택구현

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"스택 : {stack}")
