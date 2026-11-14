"""
LeetCode 122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

-------------------------------------------------------------------------------
Intuition
In this problem, you can buy and sell multiple times, so you do not need to wait for one global minimum and maximum. Any time price goes up from one day to the next, that increase can be safely taken as profit. If we collect all such positive increases, we effectively capture every profitable part of every upward trend. This greedy idea gives the same result as buying at local minima and selling at local maxima, but with much simpler code.

Approach
Initialize profit = 0.
Iterate from day 1 to n - 1.
If prices[i] > prices[i - 1], add prices[i] - prices[i - 1] to profit.
Return profit.
Why this works:

Suppose prices go 1 -> 3 -> 5.
Taking (3 - 1) + (5 - 3) equals (5 - 1).
So summing small gains is equivalent to one big optimal trade on each rising segment.
Complexity
Time complexity: O(n) — single pass through prices.
Space complexity: O(1) — only one accumulator variable.

Code in C++:

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b = prices[0];
        int sum =0;
        for(int i = 0;i < prices.size();i++)
        {
            if(prices[i] > b)
            {
                sum = sum + (prices[i] - b);

            }
            b = prices[i];
        }

        return sum;
        
    }
};
Code in Python:
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b = prices[0]
        sum =0;
        for i in range(len(prices)):
            if(b < prices[i]):
                sum = sum + (prices[i] - b)
            b = prices[i]
        return sum

