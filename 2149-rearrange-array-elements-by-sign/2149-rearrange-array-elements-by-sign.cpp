class Solution {
public:
    // vector<int> rearrangeArray(vector<int>& nums) {
    //     // code here
    //     int n = nums.size();
    // vector<int> pos;
    // vector<int> neg;
    // for(int i = 0; i < n; i++){
    // if(nums [i] >= 0){
    // pos.push_back(nums [i]);
    // }
    // else{
    // neg.push_back(nums [i]);
    // }
    // }
    // int i, index;
    // index = 0;
    // for(i = 0; i < min(pos.size(), neg.size()); i++){
    // nums [index++] = pos[i];
    // nums [index++] = neg[i];
    // }
    // while(i < pos.size()){
    // nums [index++] = pos[i++];
    // }
    // while(i < neg.size()){
    // nums [index++] = neg[i++];
    // }
    //     return nums;
    // }
    
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,0);
        int indexpos = 0, indexneg = 1;
        for(auto num: nums){
            if(num > 0){
                ans[indexpos] = num;
                indexpos += 2;
            }
            if(num<0){
                ans[indexneg] = num;
                indexneg += 2;
            }
        }
        return ans;
    }
};