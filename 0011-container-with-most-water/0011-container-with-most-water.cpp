// class Solution {
// public:
//     int maxArea(vector<int>& height) {
//         int res = INT_MIN;
//         int left = 0;
//         int right = height.size()-1;
//         while(left <= right){
//             if(height[left] < height[right]){
//                 res = max(res, height[left]*(right-left));
//                 left++;
//             }
//             else if(height[left] > height[right]){
//                 res = max(res, height[right]*(right-left));
//                 right--;
//             }
//             else{
//                 res = max(res, height[left]*(right-left));
//                 left++;
//                 right--; 
//             }
//         }
//         return res;
//     }
// };

class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = INT_MIN;
        int left = 0;
        int right = height.size()-1;
        while(left <= right){
            res = max(res, min(height[left], height[right])*(right-left));
            if(height[left] < height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return res;
    }
};