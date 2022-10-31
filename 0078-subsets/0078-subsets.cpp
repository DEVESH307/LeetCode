class Solution {
public:
    void subsetsHelper(vector<int>& nums, int index, vector<vector<int>> &res, vector<int> &temp){
        if(index == nums.size()){
            res.push_back(temp);
            return;
        }
        temp.push_back(nums[index]);
        subsetsHelper(nums, index+1, res, temp);
        temp.pop_back();
        subsetsHelper(nums, index+1, res, temp);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        // sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> temp;
        subsetsHelper(nums, 0, res, temp);
        // sort(res.begin(), res.end());
        return res;
    }
};