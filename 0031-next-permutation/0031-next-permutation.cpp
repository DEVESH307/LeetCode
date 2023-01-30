class Solution {
public:
    // void nextPermutation(vector<int>& nums) {
    //     int n = nums.size();
    //     int i;
    //     for(i = n-1; i > 0 ; i--){
    //         if(nums[i-1] < nums[i]){
    //             break;
    //         }
    //     }
    //     if(i == 0){
    //         reverse(nums.begin(), nums.end());
    //     }
    //     else{
    //         int j;
    //         for(j = n-1; j > i; j--){
    //             if(nums[j] > nums[i-1]){
    //                 break;
    //             }
    //         }
    //         swap(nums[i-1], nums[j]);
    //         sort(nums.begin()+i, nums.end());
    //     }
    // }
    
    void nextPermutation(vector<int>& nums) {
        // code here
        int n = nums.size();
        int i;
        for(i = n-1; i > 0 ; i--){
            if(nums[i-1] < nums[i]){
                break;
            }
        }
        reverse(nums.begin()+i, nums.end());
        int left = i-1;
        int right = i;
        while(left >= 0 && right < n){
            if(nums[right] > nums[left]){
                swap(nums[left], nums[right]);
                break;
            }
            right++;
        }
    }
};