class Solution {
public:
    // bool check(vector<int>& nums) {
    //     int n = nums.size();
    //     vector<int> temp;
    //     int i;
    //     for(i = 1; i < n; i++){
    //         if(nums[i] < nums[i-1]){
    //             break;
    //         }
    //     }
    //     int breakPoint = i;
    //     while(i < n) temp.push_back(nums[i++]);
    //     for(int i = 0; i < breakPoint; i++){
    //         temp.push_back(nums[i]);
    //     }
    //     bool ans = true;
    //     for(int i = 1; i < n; i++){
    //         if(temp[i-1] > temp[i]){
    //             ans = false;
    //         }
    //     }
    //     return ans;
    // }
    
    bool check(vector<int>& nums) {
        int n = nums.size();
        int break_point_count = 0;
        for(int i = 0; i < n; i++){
            if(nums[i] > nums[(i+1)%n]){
                break_point_count++;
            }
        }
        return break_point_count <= 1;
    }
};