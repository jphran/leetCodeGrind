
class CityPlanner:
    @staticmethod
    def level_buildings(heights: list[int]) -> int:
        """

        :param heights: building heights
        :return: Number of floors removed
        """
        heights.sort()  # O(n)

        n = len(heights)
        removal_cost = [0] * n
        leveling_cost = [0] * n

        for i in range(1, n):
            removal_cost[i] += removal_cost[i - 1] + heights[i - 1]
            leveling_cost[-i - 1] = leveling_cost[-i] + (heights[-i] - heights[-i-1]) * i

        total_cost = [x + y for x, y in zip(removal_cost, leveling_cost)]

        return min(total_cost)


if __name__ == "__main__":
    heights = [1, 1, 1, 7, 1, 1, 1, 1]
    print(CityPlanner.level_buildings(heights))