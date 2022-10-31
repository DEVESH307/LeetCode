class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> remFreq;
        remFreq[0] = 1;
        int n = nums.size();
        int sum = 0;
        int rem;
        int ans = 0;
        for(auto num: nums){
            sum += num;
            rem = sum%k;
            if(rem < 0) rem += k;
            ans += remFreq[rem];
            remFreq[rem]++;
        }
        return ans;
    }
};