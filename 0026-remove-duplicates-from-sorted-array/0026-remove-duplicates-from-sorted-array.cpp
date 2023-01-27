class Solution {
public:
    // int removeDuplicates(vector<int>& nums) {
    //     set<int> set;
    //     for(int i = 0; i < nums.size(); i++){
    //         set.insert(nums[i]);
    //     }
    //     int k = 0;
    //     for(auto num: set){
    //         nums[k++] = num;
    //     }
    //     return set.size();
    // }
    
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int k = 1;
        for(int i = 1; i < n; i++){
            if(nums[i-1] != nums[i]){
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};