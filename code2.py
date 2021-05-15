# Definition for singly-linked list.

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


# Definition for singly-linked list.
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


class Solution:
    # 判断列表的长度
    def len(self,li):
        length = 0
        for i in li:
            length += 1
        return length

    def list_to_link(self, li):

        sl = SingleLink()

        for i in li:
            sl.append2(i)

        return sl

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):

        list1 = []
        list2 = []
        list3 = []

        # 遍历链表并生成列表
        l1cur = l1._head
        while l1cur != None:
            list1.append(l1cur.val)
            l1cur = l1cur.next

        l2cur = l2._head
        while l2cur != None:
            list2.append(l2cur.val)
            l2cur = l2cur.next

        for i in range(len(list1)):
            list3.append(list1[i] + list2[i])
        print(list3)

        sl3 = SingleLink()

        for i in list3:
            sl3.add(i)

        sl3.tranvel()


if __name__ == "__main__":

    l1 = [0]
    l2 = [0]

    s1 = Solution()
    sl1 = s1.list_to_link(l1)

    s2 = Solution()
    sl2 = s2.list_to_link(l2)

    sl3 = Solution()
    sl3.addTwoNumbers(sl1, sl2)



