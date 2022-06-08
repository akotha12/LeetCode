class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int low = prices[0];
        int maxProfit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < low) {
                low = prices[i];
            }
            if (prices[i] - low > maxProfit) {
                maxProfit = prices[i] - low;
            }
        }
        return maxProfit;
    }
};