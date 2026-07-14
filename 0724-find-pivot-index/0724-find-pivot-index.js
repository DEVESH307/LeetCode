/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    const n = nums.length;
    const prefixSum = Array(n).fill(0);
    const suffixSum = Array(n).fill(0);

    for(let i = 1; i < n; i++){
        prefixSum[i] = prefixSum[i-1] + nums[i-1] 
    }

    for(let i = n - 2; i >= 0; i--){
        suffixSum[i] = suffixSum[i+1] + nums[i+1] 
    }

    for(let i = 0; i < n; i++){
        if(prefixSum[i]=== suffixSum[i]){
            return i;
        } 
    }

    return -1;



    
};