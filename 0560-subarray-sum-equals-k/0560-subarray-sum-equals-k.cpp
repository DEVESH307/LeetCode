// class Solution {
// public:
//     int subarraySum(vector<int>& nums, int k) {
//         int count = 0;
//         int n = nums.size();
//         for(int l = 0; l < n; l++){
//             int sum = 0;
//             for(int h = l; h < n; h++){
//                 sum += nums[h];
//                 if(sum==k){
//                     count++;
//                 }
//             }
//         }
//         return count;
//     }
// };
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ans = 0;
        int sum = 0;
        unordered_map<int, int> mp;
        mp[sum] = 1;
        for(auto num: nums){
            sum += num;
            int find = sum-k;
            if(mp.find(find) != mp.end()){
                ans += mp[find];
            }
            mp[sum]++;
        }
        return ans;
    }
};