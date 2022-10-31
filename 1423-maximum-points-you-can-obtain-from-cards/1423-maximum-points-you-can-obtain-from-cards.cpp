class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int currSum = 0;
        int maxSum;
        for(int i = 0; i < k; i++){
            currSum += cardPoints[i];
        }
        maxSum = currSum;
        for(int i = k-1; i >= 0; i--){
            currSum -= cardPoints[i];
            currSum += cardPoints[n-k+i];
            maxSum = max(maxSum, currSum);
        }
        return maxSum;
    }
};

// class Solution {
// public:
//     int maxScore(vector<int>& cardPoints, int k) {
//         int n = cardPoints.size();
//         long long totalSum = 0;
//         long long minSumOfUnpickedCard;
//         long long currSumOfUnpickedCard = 0;
//         for(auto points: cardPoints){
//             totalSum += points;
//         }
//         // cout<<totalSum<<endl;
//         for(int i = 0; i < n-k; i++){
//             currSumOfUnpickedCard += cardPoints[i];
//         }
//         // cout<<currSumOfUnpickedCard<<endl;
//         minSumOfUnpickedCard = currSumOfUnpickedCard;
//         // cout<<minSumOfUnpickedCard<<endl;
//         for(int i = n-k; i < n; i++){
//             currSumOfUnpickedCard -= cardPoints[i-(n-k)];
//             currSumOfUnpickedCard += cardPoints[i];
//             minSumOfUnpickedCard = min(minSumOfUnpickedCard, currSumOfUnpickedCard);
//             // cout<<minSumOfUnpickedCard<<endl;
//         }
//         return (int) (totalSum - minSumOfUnpickedCard);
//     }
// };