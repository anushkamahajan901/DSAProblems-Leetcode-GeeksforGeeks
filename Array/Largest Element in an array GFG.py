
from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        
        max= arr[0]; 
        n = len(arr);
        for i in range(1, n):
            if arr[i] > max:
                max = arr[i]
        return max
