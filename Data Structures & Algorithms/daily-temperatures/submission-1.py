class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temps_and_pos = []

        for i, temp in enumerate(temperatures):
            while temps_and_pos and temp > temps_and_pos[-1][0]:
                old_temp_and_pos = temps_and_pos.pop()
                res[old_temp_and_pos[1]] = i - old_temp_and_pos[1]
            temps_and_pos.append((temp, i))
        return res


                    