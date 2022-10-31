class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i;
        for(i = n-1; i > 0 ; i--){
            if(nums[i-1] < nums[i]){
                break;
            }
        }
        if(i == 0){
            reverse(nums.begin(), nums.end());
        }
        else{
            int j;
            for(j = n-1; j > i; j--){
                if(nums[j] > nums[i-1]){
                    break;
                }
            }
            swap(nums[i-1], nums[j]);
            sort(nums.begin()+i, nums.end());
        }
    }
};