// class Solution {
// public:
//     vector<vector<int>> threeSum(vector<int>& nums) {
//         sort(nums.begin() , nums.end());
//         if(nums.size() < 3){
//             return {};
//         }
//         if(nums[0] > 0){
//             return {};
//         }
//         unordered_map<int , int> hashMap;
//         for(int i = 0 ; i < nums.size() ; ++i){
//             hashMap[nums[i]] = i;
//         }
//         vector<vector<int>> answer;
//         for(int i = 0 ; i < nums.size() - 2 ; ++i){
//             if(nums[i] > 0){
//                 break;
//             }
//             for(int j = i + 1 ; j < nums.size() - 1 ; ++j){
//                 int required = -1*(nums[i] + nums[j]);
//                 if(hashMap.count(required) && hashMap.find(required)->second > j){
//                     answer.push_back({nums[i] , nums[j] , required});
//                 }
//                 j = hashMap.find(nums[j])->second;
//             }
//             i = hashMap.find(nums[i])->second;
//         }
//         return answer;
//     }
// };
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int n = nums.size();
        if(n < 3){
            return {};
        }
        if(nums[0] > 0){
            return {};
        }
        for(int i = 0; i < n; i++){
            if(nums[i] > 0){
                break;
            }
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int low = i+1;
            int high = n-1;
            int sum = 0;
            while(low < high){
                sum = nums[i]+nums[low]+nums[high];
                if(sum > 0){
                    high--;
                }
                else if(sum < 0){
                    low++;
                }
                else{
                    res.push_back({nums[i], nums[low], nums[high]});
                    int last_occr_low = nums[low];                    
                    int last_occr_high = nums[high];
                    while(low < high && last_occr_low == nums[low]){
                        low++;
                    }
                    while(low < high && last_occr_high == nums[high]){
                        high--;
                    }
                }
            }
        }
        return res;
    }
};