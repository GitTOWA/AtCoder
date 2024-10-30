from collections import deque

# 幅優先探索（BFS）で最短経路を求める関数
def bfs(maze, start, goal):
    # 方向の定義（上、下、左、右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 迷路のサイズ
    rows, cols = len(maze), len(maze[0])
    
    # キューを初期化（スタート地点と経路を追加）
    queue = deque([(start, [start])])
    
    # 訪問済みのセットを初期化
    visited = set()
    visited.add(start)
    
    while queue:
        (current_row, current_col), path = queue.popleft()
        
        # ゴールに到達したら経路を返す
        if (current_row, current_col) == goal:
            return path
        
        # 現在の位置から次の位置を確認
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            # 迷路の範囲内で、まだ訪れていない道（0）の場合
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    # ゴールにたどり着けなかった場合
    return None

# 迷路を作成（0が道、1が壁）
maze = [
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]
]

# スタートとゴールの位置を指定
start = (0, 0)  # スタート地点
goal = (5, 5)   # ゴール地点

# 幅優先探索を実行して最短経路を取得
path = bfs(maze, start, goal)

# 結果を表示
if path:
    print("最短経路:", path)
else:
    print("ゴールまでの経路が見つかりませんでした。")
