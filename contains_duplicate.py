class Solution(object):
    def containsDuplicate(self, nums):
        self.list_check = nums
        for item in self.list_check:
            if self.list_check.count(item) > 1:
                print(True) # return True
                break
        else:
            print(False) # return false

SolutionObj = Solution()
    
user_list = list(input("Enter list: "))
SolutionObj.containsDuplicate(user_list)



    
    