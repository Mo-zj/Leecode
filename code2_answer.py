# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLink(object):
    def __init__(self,node=None):
        self._head = node

    # 头插法
    def add(self,item):
        listnode = ListNode(item)

        listnode.next = self._head
        self._head = listnode

    # 把列表转换为链的数据结构,尾插法
    def append2(self,item):

        listnode = ListNode(item)

        if self._head == None:
            self._head = listnode
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = listnode

    # 遍历链表
    def tranvel(self):
        cur = self._head
        while cur != None:
            print(cur.val,end=" ")
            cur = cur.next

    def list_to_link(self, li):

        sl = SingleLink()

        for i in li:
            sl.append2(i)

        return sl


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先建立一个头节点
        head = point = ListNode(0)
        carry = 0 # 进位

        while l1 or l2:
            new_point = ListNode(0)

            if not l1:
                sum_ = l2.val + carry
                new_point.val = sum_%10
                carry = sum_ // 10
                l2 = l2.next
            elif not l2:
                sum_ = l1.val + carry
                new_point.val = sum_%10
                carry = sum_//10
                l1 = l1.next
            else:
                sum_=(l1.val + l2.val + carry)

                new_point.val = sum_%10

                carry = sum_ // 10

                l1 = l1.next
                l2 = l2.next

            point.next = new_point
            point = point.next

"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry
            curr.next = ListNode(sum % 10)
            ## bug 修复：视频中忘了移动 curr 指针了
            urr = curr.next
            carry = sum // 10

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: curr.next = ListNode(carry)
        return dummy.next

"""


if __name__ == "__main__":

    list1 = [1,2,3,4]
    list2 = [5,6.7,8]

    s1 = SingleLink()
    sl1 = s1.list_to_link(list1)

    s2 = SingleLink()
    sl2 = s2.list_to_link(list2)

    so = Solution()
    res = so.addTwoNumbers(sl1,sl2)






