# 노드 클래스
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 연결 리스트 생성
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node3
node3.next = node2

head = node1

# 리스트 내용 출력
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")   # 1 -> 3 -> 2 -> None