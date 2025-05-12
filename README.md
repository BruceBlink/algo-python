LeetCode 系统刷题计划。这份计划旨在帮助您覆盖核心知识点，并通过经典题目掌握解题方法。

请注意，难度评级是相对的，您的实际感受可能不同。您可以根据自己的情况调整每个阶段的时间和重点。

**第一阶段：基础入门与核心数据结构**

* **目标：** 熟悉平台，掌握数组、字符串、链表、栈、队列、哈希表这些基础数据结构及其操作，理解二分查找。主要集中在 Easy 和 Medium 难度题目。

1.  **数组 (Arrays) & 字符串 (Strings)**
    * **概念：** 了解数组的基本特性（连续存储）、字符串的不可变性（在某些语言中），掌握遍历、查找、修改（对于数组）等操作。
    * **技巧：** 双指针、模拟。
    * **题目：**
        * [1. Two Sum (两数之和)](https://leetcode.cn/problems/two-sum/)
            * 描述：在一个整数数组中找到两个数，它们的和等于一个特定的目标值。
        * [283. Move Zeroes (移动零)](https://leetcode.cn/problems/move-zeroes/)
            * 描述：将数组中的所有 0 移动到数组末尾，同时保持非零元素的相对顺序。
        * [125. Valid Palindrome (验证回文串)](https://leetcode.cn/problems/valid-palindrome/)
            * 描述：判断一个字符串是否是回文串，只考虑字母和数字，忽略大小写。
        * [344. Reverse String (反转字符串)](https://leetcode.cn/problems/reverse-string/)
            * 描述：将一个字符串原地反转。
        * [11. Container With Most Water (盛最多水的容器)](https://leetcode.cn/problems/container-with-most-water/)
            * 描述：给定 n 条直线，找出其中的两条直线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        * [15. 3Sum (三数之和)](https://leetcode.cn/problems/3sum/)
            * 描述：在一个整数数组中找到所有和为 0 的三元组。
2.  **链表 (Linked Lists)**
    * **概念：** 理解链表的节点结构和通过指针连接的特点，与数组的对比。
    * **技巧：** 遍历、节点增删改、反转、快慢指针。
    * **题目：**
        * [206. Reverse Linked List (反转链表)](https://leetcode.cn/problems/reverse-linked-list/)
            * 描述：反转一个单链表。
        * [21. Merge Two Sorted Lists (合并两个有序链表)](https://leetcode.cn/problems/merge-two-sorted-lists/)
            * 描述：将两个升序链表合并为一个新的升序链表。
        * [23. Merge-K-Sorted-Lists (合并K个升序链表)](https://leetcode.cn/problems/merge-k-sorted-lists/)
            * 描述：将若干个升序链表合并为一个新的升序链表。
        * [141. Linked List Cycle (环形链表)](https://leetcode.cn/problems/linked-list-cycle/)
            * 描述：判断一个链表是否包含环。
        * [142. Linked-List-Cycle-II (环形链表II)](https://leetcode.cn/problems/linked-list-cycle-ii/)
            * 描述：判断一个链表是否包含环，如果有环返回入环的起点。
        * [19. Remove Nth Node From End of List (删除链表的倒数第 N 个结点)](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
            * 描述：删除链表的倒数第 N 个节点。
        * [160. Intersection-Of-Two-Linked-Lists(相交链表)](https://leetcode.cn/problems/intersection-of-two-linked-lists/)
            * 描述：找到并返回两个单链表相交的起始节点。
3.  **栈 (Stacks) & 队列 (Queues)**
    * **概念：** 理解栈的 LIFO (后进先出) 和队列的 FIFO (先进先出) 原则。
    * **技巧：** 利用它们的特性解决问题。
    * **题目：**
        * [20. Valid Parentheses (有效的括号)](https://leetcode.cn/problems/valid-parentheses/)
            * 描述：判断一个只包含括号的字符串是否有效。
        * [155. Min Stack (最小栈)](https://leetcode.cn/problems/min-stack/)
            * 描述：实现一个支持 O(1) 时间获取最小元素的栈。
        * [232. Implement Queue using Stacks (用栈实现队列)](https://leetcode.cn/problems/implement-queue-using-stacks/)
            * 描述：使用两个栈实现一个队列。
        * [225. Implement Stack using Queues (用队列实现栈)](https://leetcode.cn/problems/implement-stack-using-queues/)
            * 描述：使用一个或多个队列实现一个栈。
4.  **哈希表 (Hash Tables)**
    * **概念：** 理解哈希表的键值对存储和 O(1) 平均时间复杂度的存取特性。
    * **技巧：** 用于快速查找、计数、去重、存储映射关系。
    * **题目：**
        * [1. Two Sum (两数之和)](https://leetcode.cn/problems/two-sum/) - 使用哈希表优化到 O(n)。
        * [242. Valid Anagram (有效的字母异位词)](https://leetcode.cn/problems/valid-anagram/)
            * 描述：判断两个字符串是否是字母异位词（组成字母和数量相同）。
        * [350. Intersection of Two Arrays II (两个数组的交集 II)](https://leetcode.cn/problems/intersection-of-two-arrays-ii/)
            * 描述：计算两个数组的交集，结果中每个元素出现的次数应与两个数组中该元素的出现次数一致。
5.  **二分查找 (Binary Search)**
    * **概念：** 理解在**有序**数据中快速查找的原理。
    * **技巧：** 递归或迭代实现，处理边界条件（左闭右闭，左闭右开等）。
    * **题目：**
        * [704. Binary Search (二分查找)](https://leetcode.cn/problems/binary-search/)
            * 描述：在一个有序数组中查找一个目标值。
        * [35. Search Insert Position (搜索插入位置)](https://leetcode.cn/problems/search-insert-position/)
            * 描述：在有序数组中找到目标值或其应该插入的位置。
        * [34. Find First and Last Position of Element in Sorted Array (在排序数组中查找元素的第一个和最后一个位置)](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)
            * 描述：在一个有序数组中查找目标值的起始和结束位置。

**第二阶段：进阶数据结构与算法思想**

* **目标：** 掌握树和图的基础算法，理解递归、回溯、动态规划、贪心等核心思想。主要集中在 Medium 难度题目，少量 Easy/Hard。

1.  **树 (Trees)**
    * **概念：** 理解树（特别是二叉树）的递归定义，掌握各种遍历方式的原理和实现。
    * **技巧：** 递归、迭代（栈、队列）、分治。
    * **题目：**
        * [101. Symmetric Tree (对称二叉树)](https://leetcode.cn/problems/symmetric-tree/)
            * 描述：验证对称二叉树。
        * [102. Binary Tree Level Order Traversal (二叉树的层序遍历)](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
            * 描述：进行二叉树的广度优先遍历。
        * [94. Binary Tree Inorder Traversal (二叉树中序遍历)](https://leetcode.cn/problems/binary-tree-inorder-traversal/)
            * 描述：实现二叉树的中序遍历（递归和迭代）。
        * [111. Minimum Depth of Binary Tree (二叉树的最小深度)](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)
            * 描述：计算二叉树的最小深度。
        * [104. Maximum Depth of Binary Tree (二叉树的最大深度)](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)
            * 描述：计算二叉树的最大深度。
        * [226. Invert Binary Tree (翻转二叉树)](https://leetcode.cn/problems/invert-binary-tree/)
            * 描述：翻转二叉树的左右子树。
        * [98. Validate Binary Search Tree (验证二叉搜索树)](https://leetcode.cn/problems/validate-binary-search-tree/)
            * 描述：判断一个二叉树是否是一个有效的二叉搜索树。
        * [235. Lowest Common Ancestor of a Binary Search Tree (二叉搜索树的最近公共祖先)](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)
            * 描述：找到给定两个节点的最近公共祖先。
        * [236. Lowest Common Ancestor of a Binary Tree (二叉树的最近公共祖先)](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)
            * 描述：找到给定两个节点的最近公共祖先。
        * [543. Diameter Of Binary Tree (二叉树的直径)](https://leetcode.cn/problems/diameter-of-binary-tree/)
            * 描述：找到树中任意两个节点之间最长路径的长度。
        * [114. Flatten Binary Tree To Linked List(二叉树展开为链表)](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)
            * 描述：给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
        * [116. Populating Next Right Pointers In Each Node(填充每个节点的下一个右侧节点指针)](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)
            * 描述：给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
        * [654. Maximum Binary Tree(最大二叉树)](https://leetcode.cn/problems/maximum-binary-tree/)
            * 描述：给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
        * [105. Construct Binary Tree From Preorder And Inorder Traversal(从前序与中序遍历序列构造二叉树)](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
            * 描述：根据二叉树的前序、中序遍历结果构造二叉树。
        * [106. Construct Binary Tree From Inorder And Postorder Traversal(从中序与后序遍历序列构造二叉树)](https://leetcode.cn/problems/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
            * 描述：根据二叉树的中序、后续遍历结果构造二叉树。
2.  **图 (Graphs) - 基础**
    * **概念：** 理解图的表示方法（邻接矩阵、邻接表），掌握 BFS 和 DFS 在图上的应用。
    * **技巧：** BFS (队列), DFS (递归或栈), 访问标记。
    * **题目：**
        * [200. Number of Islands (岛屿数量)](https://leetcode.cn/problems/number-of-islands/)
            * 描述：在二维网格中计算连通的 '1' 的数量（视为岛屿）。
        * [133. Clone Graph (克隆图)](https://leetcode.cn/problems/clone-graph/)
            * 描述：深拷贝一个图。
        * [733. Flood Fill (图像渲染)](https://leetcode.cn/problems/flood-fill/)
            * 描述：从起始像素开始，将其周围颜色相同的像素填充为新颜色。

3.  **递归 (Recursion) 与回溯 (Backtracking)**
    * **概念：** 理解递归函数的定义和调用过程，理解回溯法是试探性的解决问题（通常用于搜索所有可能的解）。
    * **技巧：** 递归基线条件、状态恢复（回溯）。
    * **题目：**
        * [46. Permutations (全排列)](https://leetcode.cn/problems/permutations/)
            * 描述：生成一个列表的所有可能排列。
        * [78. Subsets (子集)](https://leetcode.cn/problems/subsets/)
            * 描述：生成一个列表的所有可能子集。
        * [39. Combination Sum (组合总和)](https://leetcode.cn/problems/combination-sum/)
            * 描述：找到数组中相加等于目标值的所有组合（元素可以重复使用）。
        * [17. Letter Combinations of a Phone Number (电话号码的字母组合)](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)
            * 描述：根据电话号码的数字生成所有可能的字母组合。

4.  **动态规划 (Dynamic Programming - DP)**
    * **概念：** 理解 DP 的两个关键特征（重叠子问题、最优子结构），理解状态和状态转移方程，会使用 DP table (通常是数组)。从简单问题开始。
    * **技巧：** 定义状态、推导转移方程、确定 base case、填充 DP table。
    * **题目：**
        * [70. Climbing Stairs (爬楼梯)](https://leetcode.cn/problems/climbing-stairs/)
            * 描述：计算爬到楼顶的不同方法数。
        * [53. Maximum Subarray (最大子数组和)](https://leetcode.cn/problems/maximum-subarray/)
            * 描述：找到和最大的连续子数组。
        * [198. House Robber (打家劫舍)](https://leetcode.cn/problems/house-robber/)
            * 描述：计算在不惊动小偷的情况下能偷到的最高总金额（不能偷相邻的房屋）。
        * [322. Coin Change (零钱兑换)](https://leetcode.cn/problems/coin-change/)
            * 描述：计算凑成总金额所需的最少硬币个数。

5.  **贪心算法 (Greedy Algorithm)**
    * **概念：** 在每一步选择中都采取在当前状态下最好或最优（即最利于达到全局最优）的选择。
    * **技巧：** 识别问题的贪心性质，证明（或理解为什么）局部最优能导致全局最优。
    * **题目：**
        * [121. Best Time to Buy and Sell Stock (买卖股票的最佳时机)](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
            * 描述：计算一次交易能获得的最大利润。
        * [55. Jump Game (跳跃游戏)](https://leetcode.cn/problems/jump-game/)
            * 描述：判断是否能到达数组的最后一个索引。

6.  **堆 (Heap) / 优先队列 (Priority Queue)**
    * **概念：** 理解堆是一种特殊的树形数据结构，能快速找到最大/最小元素，用于实现优先队列。
    * **技巧：** 使用语言内置的优先队列（如 Python 的 `heapq`）。
    * **题目：**
        * [347. Top K Frequent Elements (前 K 个高频元素)](https://leetcode.cn/problems/top-k-frequent-elements/)
            * 描述：找到列表中出现频率最高的 K 个元素。

**第三阶段：高级算法与混合应用**

* **目标：** 挑战更复杂的 DP、图算法，掌握单调栈/队列等特定模式，学习一些不常用但重要的算法。主要集中在 Medium 和 Hard 难度题目。

1.  **单调栈 (Monotonic Stack) & 单调队列 (Monotonic Queue)**
    * **概念：** 利用栈/队列维护元素的单调性，高效处理“找左右第一个更/小元素”或滑动窗口问题。
    * **题目：**
        * [739. Daily Temperatures (每日温度)](https://leetcode.cn/problems/daily-temperatures/) (单调栈)
            * 描述：对于每天的温度，计算需要等待多少天才能遇到更高的温度。
        * [42. Trapping Rain Water (接雨水)](https://leetcode.cn/problems/trapping-rain-water/) (双指针、DP、栈解法)
            * 描述：计算给定高度图能接多少雨水。
        * [84. Largest Rectangle in Histogram (柱状图中最大的矩形)](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (单调栈)
            * 描述：计算柱状图中能围成的最大矩形面积。
        * [239. Sliding Window Maximum (滑动窗口最大值)](https://leetcode.cn/problems/sliding-window-maximum/) (单调队列/双端队列)
            * 描述：计算滑动窗口中每个位置的最大值。
        * [907. Sum of Subarray Minimums (子数组的最小值之和)](https://leetcode.cn/problems/sum-of-subarray-minimums/) (单调栈 + 贡献法)
            * 描述：计算所有连续子数组的最小值之和。

2.  **高级 DP**
    * **概念：** 涉及到二维 DP、字符串 DP、背包问题变种等。
    * **题目：**
        * [1143. Longest Common Subsequence (最长公共子序列)](https://leetcode.cn/problems/longest-common-subsequence/)
            * 描述：计算两个字符串的最长公共子序列的长度。
        * [64. Minimum Path Sum (最小路径和)](https://leetcode.cn/problems/minimum-path-sum/)
            * 描述：计算网格中从左上角到右下角的最小路径和（只能向下或向右）。
        * [300. Longest Increasing Subsequence (最长递增子序列)](https://leetcode.cn/problems/longest-increasing-subsequence/)
            * 描述：计算数组的最长严格递增子序列的长度。

3.  **图的高级算法 (概念理解与应用)**
    * **概念：** 拓扑排序、最短路径（Dijkstra, Floyd-Warshall 了解）、最小生成树（Prim, Kruskal 了解）。
    * **题目：**
        * [207. Course Schedule (课程表)](https://leetcode.cn/problems/course-schedule/)
            * 描述：判断是否可以完成所有课程（涉及到有向图的拓扑排序）。
        * [547. Number of Provinces (省份数量)](https://leetcode.cn/problems/number-of-provinces/) (并查集 或 DFS/BFS)
            * 描述：计算连通分量的数量。

4.  **Trie (前缀树)**
    * **概念：** 用于高效存储和查找字符串集合中具有相同前缀的字符串。
    * **题目：**
        * [208. Implement Trie (Prefix Tree) (实现 Trie (前缀树))](https://leetcode.cn/problems/implement-trie-prefix-tree/)
            * 描述：实现 Trie 的插入、查找、前缀查找功能。

5.  **并查集 (Union Find)**
    * **概念：** 高效处理元素分组和查询元素所属组的问题。
    * **题目：**
        * [547. Number of Provinces (省份数量)](https://leetcode.cn/problems/number-of-provinces/) (见上，并查集是另一种解法)
        * [1202. Smallest String With Swaps (交换字符串中的元素)](https://leetcode.cn/problems/smallest-string-with-swaps/)
            * 描述：给定一系列可以交换的索引对，求字典序最小的可能字符串。

**第四阶段：模拟面试与查漏补缺**

* **目标：** 将掌握的知识灵活运用，提高速度和准确率，适应面试环境。

1.  **参加 LeetCode 周赛/双周赛：** 在规定时间内独立完成题目，检验自己的水平。
2.  **随机刷题：** 使用 LeetCode 题库的随机功能，或者按照公司标签刷题，模拟面试的随机性。
3.  **模拟面试：** 与他人进行模拟面试，练习在压力下清晰地表达思路、写代码、调试。
4.  **回顾总结：**
    * 整理错题本，定期复习。
    * 总结常见算法模式的识别方法和解题框架。
    * 对每个知识点，能够不看代码白板写出其核心实现。

**如何使用这份列表：**

* **按部就班：** 建议大致按照阶段和主题的顺序进行。
* **注重理解：** 每道题都要理解其考察的知识点、为什么这种算法适用、以及代码的每一步。
* **自己先尝试：** 不要轻易看题解，先独立思考和尝试。
* **多解法比较：** 理解一种解法后，去看看是否有其他解法，对比它们的优劣。
* **反复练习：** 对于重要的经典题目，过一段时间再做一遍，检查是否真正掌握。

祝您刷题顺利，不断进步！