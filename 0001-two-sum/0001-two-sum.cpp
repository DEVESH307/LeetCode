class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp ;
        int n = nums.size();
        vector<int> res(2);
        for (int i = 0; i < n; i++) {
            int find = target - nums[i];
           if(mp.find(find) != mp.end()){
               res[0] = mp[find];               
               res[1] = i;
           }
            else{
                mp[nums[i]] = i;
            }
        }
        return res;
    }
};