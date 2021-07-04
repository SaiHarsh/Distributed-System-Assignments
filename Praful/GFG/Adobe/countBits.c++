class Solution {
public:
    vector<int> countBits(int n) {
        
        int i, j, k;
        vector <int> a;
        for (k = 0; k <= n; k++)
        {
            j = k;
            for( i = 0; j; ++i )
            {
                j &= j - 1;
            }
            a.push_back(i);
        }
        return( a );
    }
};
