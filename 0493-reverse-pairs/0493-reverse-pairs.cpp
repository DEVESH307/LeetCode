class Solution {
public:
    int Merge(vector <int> &nums, int low, int mid, int high) {
        int total = 0;
        int j = mid+1;
        for (int i = low; i <= mid; i++) {
            while (j <= high && nums[i] > 2LL*nums[j]) {
                j++;
            }
            total += (j-(mid+1));
        }
        
        vector<int> temp;
        int left = low;
        int right = mid+1;
        while (left <= mid && right <= high) {
            if (nums[left] <= nums[right]){
                temp.push_back(nums[left++]);
            } 
            else{
                temp.push_back(nums[right++]);
            }
        }
        while (left <= mid) {
            temp.push_back(nums[left++]);
        }
        while (right <= high) {
            temp.push_back(nums[right++]);
        }
        for (int i = low; i <= high; i++) {
            nums[i] = temp[i-low];
        }
        return total;
    }
    int MergeSort(vector<int> & nums, int low, int high) {
        if (low >= high) return 0;
        int mid = (low + high)/2;
        int x = MergeSort(nums, low, mid);
        int y = MergeSort(nums, mid+1, high);
        int z = Merge(nums, low, mid, high);
        return x+y+z;
    }
    int reversePairs(vector<int>& nums) {
        return MergeSort(nums, 0, nums.size() - 1);   
    }
};