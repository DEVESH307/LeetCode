class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        // int N = nums.length;
        // int[] res = new int[N];
        // int sum = 0;
        // for(int i = 0; i < N; i++){
        //     sum += nums[i];
        //     res[i] = sum;
        // }
        // return res;
        for(int i = 1; i < nums.size(); i++){
            nums[i] += nums[i-1];
        }
        return nums;
    }
};