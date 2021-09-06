'''idea
계산문제??

그리디 문제인가??

재귀적으로 풀어야 할 듯.

교환한 용기를 이용해, 다시 교환 가능하다.

크기순 정렬

진탐색트리 사용: 삽입, 삭제 빈번하다.

제일 큰 것(M)과 제일 작은것(m)

limit = X/2

M이 X 이상이면 통과

M+m이 limit 이상이면 

통과

M+m이 limit 이상이 아니면 
# 이렇게 하면 오래 걸린다.
# M+그 다음으로 작은것이 limit 이상인지 검사..
일단 새로 용기를 받고, 새로 받은 용기를 나중에 또 쓰일 수도 있게 한다.


총 용량: 12

반: 6

1 2 3 4 5 6
1, 2-> 9   
3, 4 ->12   
5, 6 -> 12
-> 작은 것끼리 합치면 안되는 경우가있다.


1 2 3 4

계속 최대, 최소 값을 꺼내야 한다.

이중우선순위 큐가 있으면 좋겠다...
할 줄 모르니까 이진탐색트리로 하자.


'''
import sys
import collections

read = sys.stdin.readline
out= sys.stdout.write


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        

class BST:
    def __init__(self, root):
        self.root = root
        self.parent= root
        self.current_node= root
        self.size = 1

    def insert(self, value):
        self.current_node = self.root
        self.size += 1
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def delete(self):
        # self.current_node = current_node
        # self.parent = parent
        # 삭제할 노드가 있는지 검사하고 없으면 False리턴
        # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
        # is_search = False
        # self.current_node = self.root
        # self.parent = self.root
        # while self.current_node:
        #     if self.current_node.value == value:
        #         is_search = True
        #         break
        #     elif value < self.current_node.value:
        #         self.parent = self.current_node
        #         self.current_node = self.current_node.left
        #     else:
        #         self.parent = self.current_node
        #         self.current_node = self.current_node.right
        # if is_search == False:
        #     return False

        value = self.current_node.value
        # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
        
        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        
        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right                

        # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
                
            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        self.size -= 1
        return True

    def pop_min(self):
        if self.root is None:
            
            return 
        self.current_node = self.root
        print(self.current_node.value)
        while True:
            print("내려가기")
            print(self.current_node.value)
            if self.current_node.left != None:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                break
        # while self.current_node.left != None:
        #     print("내려가기")
        #     self.parent = self.current_node
        #     self.current_node = self.current_node.left
        val = self.current_node.value
        print("delete 시작")
        self.delete()
        print("hello")
        # print(val)
        return val

    def pop_max(self):
        if self.root is None:
            return 
        self.current_node = self.root
        
        while self.current_node.right is not None:
            self.parent = self.current_node
            self.current_node = self.current_node.right
        val = self.current_node.value
        self.delete()
        return val



                
N, X = list(map(int, read().split()))
C = list(map(int, read().split()))


# 균형 잡아주기
C.sort()
center = N//2
bst = BST(Node(C[center]))

# bst 생성
for i in range(N):
    if i!=center:
        bst.insert(C[i])



half = X/2

result = 0

while bst.size>1:
    print(str(bst.size))
    maxC = bst.pop_max()
    print("pop max")
    # max가 이미 꽉 차있다면 개수 하나 추가
    if maxC >= X:
        result+= 1
        continue

    minC = bst.pop_min()
    print("pop pop_min")
    new = max(X, maxC+minC+half)

    print(f"M, m, n, size = {maxC}, {minC}, {new}, {bst.size}")
    # 새로 받은 용기가 꽉 차있으면
    if new >= X:
        
        result+= 1
        print(f"result++: {result}")
        continue
    # 새로 받은 용기가 꽉 안 차있으면
    else:
        print(f"insert ${new}")
        bst.insert(new)


print(result)
print("끝")