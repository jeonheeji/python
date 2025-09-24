# que

# enqueue(data) 맨 위에 요소 추가
# dequeue()  요소 제거 및 반환
# front()/peek() 맨 앞 요소 확인 (제거하지 않음)
# is_empty() 스택이 비어있는지 확인
# size() 스택의 요소 개수 반환

# => 모든 시간 복잡도 0(1)

class ListQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):  # 시간복잡도 증가 0(n)
        if not self.is_empty():
            return self.items.pop(0)
        else:
            IndexError("Queue empty")

    def fornt(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empyt")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


que = ListQueue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(f"que : {que}")
