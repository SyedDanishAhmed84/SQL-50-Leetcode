class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        area=0

        while left<right:
            width=right-left
            current_height=min(height[left],height[right])
            current_area=width*current_height

            area=max(area,current_area)
            
            if height[left] < height[right]:
                left=left+1
            else:
                right=right-1

        return area

a=[1,8,6,2,5,4,8,3,7]
sol=Solution()
sol.maxArea(a)
print(a)
        