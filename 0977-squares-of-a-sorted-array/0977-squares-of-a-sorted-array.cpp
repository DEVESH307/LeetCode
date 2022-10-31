class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // int n = nums.size();
        // for(int i = 0; i < n; i++){
        //     if(nums[i] < 0){
        //         nums[i] = -1*nums[i];
        //     }
        // }
        // sort(nums.begin(), nums.end());
        // for(int i = 0; i < n; i++){
        //     nums[i] = nums[i]*nums[i];
        // }
        // return nums;
        int n = nums.size();
        vector<int> res(n);
        int l = 0;
        int r = n-1;
        for(int i = n-1; i >= 0; i--){
            if(abs(nums[l]) > abs(nums[r])){
                res[i] = nums[l]*nums[l];
                l++;
            }
            else{
                res[i] = nums[r]*nums[r];
                r--;
            }
        }
        return res;
    }
};