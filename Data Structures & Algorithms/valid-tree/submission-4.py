class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_map = {}

        # add edges in a way such that there are no duplicate edges
        for e in edges:
            parent = e[0]
            child = e[1]

            if parent not in edge_map:
                if child in edge_map:
                    # if parent not in edge_map[child]:
                    edge_map[child].add(parent)
                else:
                    edge_map[parent] = {child}
            else:
                if child in edge_map:
                    # if parent not in edge_map[child]:
                    edge_map[child].add(parent)
                else:
                    edge_map[parent].add(child)

        # check if valid tree (check for no cycles)
        visited = set()
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            if node in edge_map:
                for i in edge_map[node]:
                    if not dfs(i):
                        return False

            return True

        return dfs(0) and n == len(visited)