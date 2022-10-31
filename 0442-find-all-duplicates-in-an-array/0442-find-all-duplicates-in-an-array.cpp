// class Solution {
// public:
//     vector<int> findDuplicates(vector<int>& nums) {
//         vector<int> res;
//         sort(nums.begin(), nums.end());
//         int n = nums.size();
//         for(int i = 0; i < n-1; i++){
//             if(nums[i] == nums[i+1]){
//                 res.push_back(nums[i]);
//             }
//         }
//         return res;
//     }
// };

// class Solution {
// public:
//     vector<int> findDuplicates(vector<int>& nums) {
//         vector<int> res;
//         int n = nums.size();
//         unordered_set<int> st;
//         for(auto num: nums){
//             if(st.find(num) != st.end()){
//                 res.push_back(num);
//             }
//             else{
//                 st.insert(num);
//             }
//         }
//         return res;
//     }
// };

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            if(nums[abs(nums[i])-1] < 0)
                res.push_back(abs(nums[i]));
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1];
        }
        return res;
    }
};