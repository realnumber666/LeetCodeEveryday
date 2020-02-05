class Solution:
    def findOrder(self, n: int, edge: List[List[int]]) -> List[int]:
        conn = {i: [] for i in range(n)}
        indgree = [0] * n

        for item in edge:
            conn[item[1]].append(item[0])
            indgree[item[0]] += 1

        zero_indgree = []

        for i in range(n):
            if indgree[i] == 0:
                zero_indgree.append(i)

        i = 0
        while i < len(zero_indgree):
            for node in conn[zero_indgree[i]]:
                indgree[node] -= 1
                if indgree[node] == 0:
                    zero_indgree.append(node)
            i += 1

        if len(zero_indgree) == n:
            return zero_indgree
        else:
            return []