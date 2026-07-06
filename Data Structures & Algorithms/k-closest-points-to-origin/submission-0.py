class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points: return []
        if k > len(points) : return points
        res = []
        for point_x, point_y in points:
            temp = point_x*point_x + point_y*point_y
            heapq.heappush_max(res, (temp, [point_x, point_y]))
            if len(res) > k:
                heapq.heappop_max(res)

        ans = []
        while len(res):
            _ , point = heapq.heappop_max(res)
            ans.append(point)
        return ans