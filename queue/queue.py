from collections import deque

queue = deque([1,2,3])
queue.append(4) # queue에 4를 쌓는다
queue.popleft() # queue에서 가장 앞의 데이터를 뺀다

print(list(queue)); # [2,3,4]