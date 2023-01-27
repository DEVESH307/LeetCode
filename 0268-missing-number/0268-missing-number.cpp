class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int missNum = 0;
        for(int i = 1; i <= nums.size(); i++){
            missNum = missNum^nums[i-1]^i;
        }
        return missNum;
    }
};