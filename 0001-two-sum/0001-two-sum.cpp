class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hm;
        int n = nums.size();
        vector<int> res(2);
        for (int i = 0; i < n; i++) {
           if(hm.find(target - nums[i]) != hm.end()){
               res[0] = hm[target - nums[i]];               
               res[1] = i;

           }
            else{
                hm[nums[i]] = i;
            }
        }
        return res;
    }
};