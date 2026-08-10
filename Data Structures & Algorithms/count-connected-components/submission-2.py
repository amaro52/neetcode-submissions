class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        maps = {}

        # make mappings for all the nodes
        for e in edges:
            node1 = e[0]
            node2 = e[1]

            if node1 not in maps:
                maps[node1] = {node2}
            else:
                maps[node1].add(node2)

            if node2 not in maps:
                maps[node2] = {node1}
            else:
                maps[node2].add(node1)

        # go through connected component
        visited = set()
        def dfs(node):
            if node in maps:
                for c in maps[node]:
                    if c not in visited:
                        visited.add(c)
                        dfs(c)

        # count number of components
        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
             

        return components






















