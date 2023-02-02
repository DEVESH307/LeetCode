// class Solution {
//   public:
//     int searchHelper(int nums[], int low, int high, int target) {
//         // code here
//         if(low > high) return -1;
        
//         int mid = (low+high)/2;
//         if(nums[mid] == target) 
//             return mid;
//         else if(nums[mid] < target)
//             return searchHelper(nums, mid+1, high, target);
//         else
//             return searchHelper(nums, low, mid-1, target);
        
//     }
//     int search(int nums[], int n, int target) {
//         // code here
//         return searchHelper(nums, 0, n-1, target);
//     }
// };

// Iteration Method

class Solution {
    public:
    int search(vector<int>& nums, int target) {
        // code here
        int n = nums.size();
        int low = 0;
        int high = n-1;
        
        while(low <= high){
            int mid = (low+high)/2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                low = mid+1;
            else
                high = mid-1;
        }
        return -1;
    }
};