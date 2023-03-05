class Solution(object):
    def containsDuplicate(self, nums):
        checker = 0
        self.list_check = nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        for x in range(len(self.list_check)):
            if checker == 0:
                checker = self.list_check[x]
                print(checker + " 1")
                continue
            if checker != self.list_check[x]:
                checker = self.list_check[x]
                print(checker + " 2")
                
            if checker == self.list_check[x]:
                print(checker + " 3")
                print(True)
                break
            
        else:
            print(False)

SolutionObj = Solution()
    
user_list = list(input("Enter list: "))
SolutionObj.containsDuplicate(user_list)



    
    