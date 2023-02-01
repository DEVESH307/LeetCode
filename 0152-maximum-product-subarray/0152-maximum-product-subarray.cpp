class Solution {
public:
    int maxProduct(vector<int>& nums) {
        long long maxProd = *max_element(nums.begin(), nums.end());
	    long long currMax = 1;
	    long long currMin = 1;
	    for(auto a: nums){
	        if(a == 0){
	            currMax = 1;
    	        currMin = 1;
	        }
	        else{
	            long long currMaxTemp = currMax;
	            long long currMinTemp = currMin;
	            currMax = max({a*currMaxTemp, a*currMinTemp, (long long)a});
	            currMin = min({a*currMaxTemp, a*currMinTemp, (long long)a});
	            maxProd = max(maxProd, currMax);
	        }
	    }
	    return maxProd;
    }
};