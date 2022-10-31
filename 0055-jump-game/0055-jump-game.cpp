class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goalPost = nums.size()-1;
        for(int i = nums.size()-2; i >= 0; i--){
            if(i + nums[i] >= goalPost)
                goalPost = i;
        }
        return goalPost == 0;
    }
};