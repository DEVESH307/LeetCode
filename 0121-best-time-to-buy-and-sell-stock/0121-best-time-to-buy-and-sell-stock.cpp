class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSoFar = prices[0];
        int maxProfit = INT_MIN;
        for(auto price: prices){
            minSoFar = min(minSoFar, price);
            maxProfit = max(maxProfit, price-minSoFar);
        }
        return maxProfit;
    }
};