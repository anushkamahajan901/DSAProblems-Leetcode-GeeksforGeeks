
class Solution:
    def print2largest(self, arr):
        # Code Here
        largest=second_largest=-1;

        for i in arr:
            if i > largest:
                second_largest = largest;
                largest = i;

                
            elif i > second_largest and i!= largest:
                second_largest = i;
                
        return second_largest
                
