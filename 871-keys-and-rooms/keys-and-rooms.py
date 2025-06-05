class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs_recursive(graph, node, visited):
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in graph[node]:
                    dfs_recursive(graph, neighbor, visited)
        visited = set()
        c = list(range(0, len(rooms), 1))
        res = {key: value for key, value in zip(c, rooms)}
        dfs_recursive(res, 0, visited)
        d = list(set(c) - set(visited))
       
        
        if d == []:
            return True
        else:
            return False


        
        