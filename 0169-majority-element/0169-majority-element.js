/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
    let majorityElement = nums[0];

    let voteCount = 1;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === majorityElement) {
            voteCount += 1;
        } else {
            voteCount -= 1
        }

        if (voteCount === 0) {
            majorityElement = nums[i];
            voteCount = 1;
        }
    }

    return majorityElement;


};