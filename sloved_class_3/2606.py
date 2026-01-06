# 백준 2606: 바이러스 (DFS 풀이)

def dfs(graph, start, visited):
    visited[start] = True  # start 컴퓨터를 방문 처리(=감염 처리)

    # start 컴퓨터와 직접 연결된 모든 컴퓨터(이웃) 확인
    for neighbor in graph[start]:
        # 아직 방문(감염)하지 않은 컴퓨터라면
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)  # 그 컴퓨터로 이동해서 계속 DFS


def main():
    # 컴퓨터의 수 (1 ~ n)
    n = int(input())

    # 네트워크 상에서 연결된 컴퓨터 쌍(간선)의 수
    m = int(input())

    # 인접 리스트 형태로 그래프 초기화
    # 컴퓨터 번호를 1부터 쓰기 때문에 n+1 크기로 생성 (0번은 사용하지 않음)
    graph = [[] for _ in range(n + 1)]

    # m개의 연결 정보를 입력받아 그래프 구성
    for _ in range(m):
        a, b = map(int, input().split())
        # a와 b는 양방향 연결이므로 서로의 리스트에 추가
        graph[a].append(b)
        graph[b].append(a)

    # 방문(감염) 여부 체크 배열 (False로 초기화)
    visited = [False] * (n + 1)

    # 1번 컴퓨터에서 시작해 DFS로 연결된 모든 컴퓨터를 방문 처리
    dfs(graph, 1, visited)

    # visited에서 True의 개수 = 감염(방문)된 컴퓨터 수
    # 문제는 1번 컴퓨터는 제외하고 출력하라고 하므로 -1
    infected_count = sum(visited) - 1

    # 결과 출력
    print(infected_count)


# 이 파일이 직접 실행될 때만 main() 호출
if __name__ == "__main__":
    main()