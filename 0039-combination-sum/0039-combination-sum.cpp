class Solution {
public:
    vector<vector<int>> res;
    void combinationSumHelper(vector<int>& candidates, int index, int target, vector<int> &sol){
        if(index == candidates.size() || target < 0)
            return;
        if(target == 0){
            res.push_back(sol);
            return;
        }
        combinationSumHelper(candidates, index+1, target, sol);
        sol.push_back(candidates[index]);
        if(target-candidates[index] >= 0)
            combinationSumHelper(candidates, index, target-candidates[index], sol);
        sol.pop_back();

    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> sol;
        combinationSumHelper(candidates, 0, target, sol);
        return res;
    }
};