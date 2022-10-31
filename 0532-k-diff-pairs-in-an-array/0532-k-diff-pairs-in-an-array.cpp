class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int slow = 0;
        int fast = 1;
        int ans = 0;
        if (n == 0 || k < 0)   
            return 0;
        while(fast < n){
            if(nums[fast] - nums[slow] > k){
                slow++;
                if(fast - slow == 0){
                    fast++;
                }
            }
            else if(nums[fast] - nums[slow] < k){
                fast++;
            }
            else{
                ans++;
                slow++;
                fast++;
                while(fast < n && nums[fast] == nums[fast-1]){
                    fast++;
                }
            }
        }
        return ans;
    }
};