from typing import List


class RiverSizes:
    def getRiverSizes(self, map: List[List[int]]) -> List[int]:
        sizes = []
        visited = [[False for value in row] for row in map]
        for i in range(len(map)):
            for j in range(len(map[i])):
                self.explore(i, j, map, visited, sizes)
        return sizes

    def explore(self,
                i: int,
                j: int,
                map: List[List[int]],
                visited: List[List[bool]],
                sizes: List[int]):
