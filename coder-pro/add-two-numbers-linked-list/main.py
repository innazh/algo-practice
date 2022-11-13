class Node(object):
    def __init__(self, x):
        self.val = int(x)
        self.next = None

#O(n) Time & Space
class Solution(object):
    def addTwoNums(self, lOne, lTwo):
        iOne = lOne
        iTwo = lTwo
        sum = curr = None

        carryOver = 0
        while iOne or iTwo:
            s = iOne.val + iTwo.val + carryOver
            carryOver= s / 10

            if not curr:
                sum = curr = Node(s % 10)
            else:
                curr.next = Node(s % 10)
                curr = curr.next

            if iOne.next or iTwo.next:
                if not iOne.next:
                    iOne.next = Node(0)
                if not iTwo.next:
                    iTwo.next = Node(0)
            iOne = iOne.next
            iTwo = iTwo.next

        if carryOver!=0:
            curr.next = Node(carryOver)
        # print(sum.val, sum.next.val, sum.next.next.val,sum.next.next.next.val)
        return sum

# 953
# 109
# ---
# 0621
listOne = Node(9)
listOne.next = Node(5)
listOne.next.next = Node(3)
listTwo = Node(1)
listTwo.next = Node(0)
listTwo.next.next = Node(9)

Solution().addTwoNums(listOne, listTwo) #1062