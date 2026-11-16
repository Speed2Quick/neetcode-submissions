class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # store the current max area
        # get the min height between two points
        # get the distance between the two points

        # calulate the area
        # while r_height_idx is greater than l_height_idx
        # calulate the current area
        # if the current area is greater than the res
        # assign result to current area
        # move the index of the smaller height

        l, r = 0, len(heights) - 1

        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res