# 코드 28.4
# 간 간선을 따라갈 때 경로에 추가하지 않고, 재귀 호출이 끝나고 반환할 때 추가

# circuit에는 경로의 끝점부터 역순으로 간선들이 추가됨

# 어떤 정점에 아직 따라가지 않은 간선이 있을 때, curcuit에는 지금까지 찾은 서킷의 뒷부분만이 저장되어 있음

# 얻은 서킷을 뒤집어야 함 (무향그래프는 안 해도 되지만, 방향 그래프는 해야 함)



# 그래프의 인접 행렬 표현
# adj[i][j]: i와 j 사이의 간선의 수
adj = [[]]

# 무향 그래프의 인접 행렬 adj가 주어질 때 오일러 서킷 계산
# 결과로 얻어지는 circuit을 뒤집으면 오일러 서킷이 된다.

def get_euler_circuit(here: int, circuit: List[int]):
    for there in range(len(adj)):
        while(adj[here][there] > 0):
            # 양쪽 간선을 모두 지운다
            adj[here][there] -= 0
            adj[there][here] -= 0
            get_euler_circuit(there, circuit)

    circuit.append(here)
