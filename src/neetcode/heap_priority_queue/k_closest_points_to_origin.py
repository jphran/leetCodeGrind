"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
"""
import heapq
import math


class Solution:
    def _euclidean_distance_from_origin(self, point: list[int]) -> float:
        return math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_max_heap: list[tuple[float, int]] = []

        for idx, point in enumerate(points):
            distance = self._euclidean_distance_from_origin(point)

            if len(distance_max_heap) >= k:
                if -distance > distance_max_heap[0][0]:
                    heapq.heappushpop(distance_max_heap, (-distance, idx))
            else:
                heapq.heappush(distance_max_heap, (-distance, idx))

        closest_points = [points[tup[1]] for tup in distance_max_heap]

        return closest_points
