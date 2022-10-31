class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n-3; i++){
            for(int j = i+1; j < n-2; j++){
                int left_ptr = j+1;
                int right_ptr = n-1;
                while(left_ptr < right_ptr){
                    // int new_target = target - (nums[i] + nums[j]);
                    // int curr_sum = nums[left_ptr] + nums[right_ptr]; 
                    long long curr_sum = 1LL*nums[i] + 1LL*nums[j] + 1LL*nums[left_ptr] + 1LL*nums[right_ptr]; 
                    if(curr_sum > target)
                        --right_ptr;
                    else if(curr_sum < target)
                        ++left_ptr;
                    else{
                        res.push_back({nums[i], nums[j], nums[left_ptr], nums[right_ptr]});
                        ++left_ptr;
                        --right_ptr;
                        while (left_ptr < right_ptr && nums[left_ptr] == nums[left_ptr-1]) ++left_ptr;
                        while (left_ptr < right_ptr && nums[right_ptr] == nums[right_ptr+1]) --right_ptr;
                    }
                }
                while(j + 1 < n && nums[j] == nums[j+1]) ++j;
            }
            while(i + 1 < n && nums[i] == nums[i+1]) ++i;
        }
        return res;
    }
};