class Solution {
public:
    const int mod = 1e9+7;
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        int maxHorzontalDistance = max(horizontalCuts[0], h-horizontalCuts.back());
        int maxverticalDistance = max(verticalCuts[0], w-verticalCuts.back());
        for(int i = 0; i < horizontalCuts.size()-1; i++)
            maxHorzontalDistance = max(maxHorzontalDistance, horizontalCuts[i+1]-horizontalCuts[i]);
        for(int j = 0; j < verticalCuts.size()-1; j++)
            maxverticalDistance = max(maxverticalDistance, verticalCuts[j+1]-verticalCuts[j]);
        return (maxHorzontalDistance*1LL*maxverticalDistance)%mod;

    }
};