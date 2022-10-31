class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // int ME = nums[0];
        // int meCnt = 1;
        // for(int i = 1; i < nums.size(); i++){
        //     if(nums[i] == ME){
        //         meCnt++;
        //     }
        //     else{
        //         meCnt--;
        //         if(meCnt == 0){
        //             ME = nums[i];
        //             meCnt = 1;
        //         }
        //     }
        // }
        // return ME;
        int majorityIndex = 0;
        int count = 1;
        for(int index = 1; index < nums.size(); index++){
            count = nums[majorityIndex] == nums[index] ? ++count : --count;
            if(count == 0){
                majorityIndex = index;
                count = 1;
            }
        }
        return nums[majorityIndex];
    }
};