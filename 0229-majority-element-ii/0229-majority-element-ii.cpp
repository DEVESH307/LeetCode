class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        int required_count = n/3;
        unordered_map<int, int> mp;
        for(auto num: nums){
            mp[num]++;
        }
        for(auto itr: mp){
            if(itr.second > required_count){
                res.push_back(itr.first);
            }
        }
        return res;
    }
};