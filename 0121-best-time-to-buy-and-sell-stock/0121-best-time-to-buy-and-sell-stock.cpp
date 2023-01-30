class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSoFar = prices[0];
        int maxProfit = INT_MIN;
        int profit;
        for(auto price: prices){
            minSoFar = min(minSoFar, price);
            profit = price-minSoFar;
            maxProfit = max(maxProfit, profit);
        }
        return maxProfit;
    }
};