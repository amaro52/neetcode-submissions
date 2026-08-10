class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {}

        for edge in edges:
            # arbitrary names (for visualization)
            parent = edge[0]
            child = edge[1]

            if parent not in edgeMap:   # parent is not in map
                if child in edgeMap:    # child is in map
                    for c in edgeMap[child]:
                        if c in edgeMap and parent in edgeMap[c]:
                            return False    # parent connects to a grandchild or something - BAD

                    edgeMap[child].append(parent)   # add the parent to the child's edge list
                else:
                    edgeMap[parent] = [child]   # create new entry
            else:
                for c in edgeMap[parent]:
                    if c in edgeMap and child in edgeMap[c]:
                        return False
                edgeMap[parent].append(child)   # add child to parent's edge list

        # DFS to check if all nodes are connected
        visited = set()  # stores all visited nodes
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)  # add node to the set of visited
            if i in edgeMap:    
                for j in edgeMap[i]:
                    if j != prev and not dfs(j, i):
                        return False
            return True

        return dfs(0, -1) and n == len(visited)  # seems to be a valid tree