class Solution {
public:
    // int findMaxConsecutiveOnes(vector<int>& nums) {
    //     int max_one = 0;
    //     int  n = nums.size();
    //     for(int i = 0; i < n; i++){
    //         int count1 = 0;
    //         int x = nums[i];
    //         if(x == 1){
    //             while(i < n && nums[i] == 1){
    //                 count1++;
    //                 i++;
    //             }
    //         } 
    //         else{
    //             continue;
    //         }
    //         max_one = max(max_one, count1);
    //     }
    //     return max_one;
    // }
    
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max1 = 0;
        int count1 = 0;
        int  n = nums.size();
        for(int i = 0; i < n; i++){
            if(nums[i] == 1){
                count1++;
                max1 = max(max1, count1);
            }
            else{
                count1 = 0;
            }
        }
        return max1;
    }
};