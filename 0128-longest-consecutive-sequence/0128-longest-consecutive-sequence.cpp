class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;
        unordered_set<int> set;
        for(auto num: nums){
            set.insert(num);
        }
        for(auto num: nums){
            if(set.find(num-1) == set.end()){
                int curr_len = 0;
                int curr_num = num;
                while(set.find(curr_num) != set.end()){
                    curr_num++;
                    curr_len++;
                }
                ans = max(ans, curr_len);
            }
        }
        return ans;
    }
};