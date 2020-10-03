# include<bits/stdc++.h>

using namespace std;

int main(void){
	int n;
	scanf("%d", &n);

	int heights[n+1];
	for(int i=1; i<=n; i++) scanf("%d", &heights[i]);

	//Step-1
	int height_i_2, height_i_1, ans;

	//Step-2
	height_i_2 = 0;
	height_i_1 = abs(heights[1] - heights[2]);
	ans = height_i_1;
	//Step-3

	int oneStep, twoStep;
	for(int i=3; i<=n; i++){
		oneStep = height_i_1 + abs(heights[i] - heights[i-1]);
		twoStep = height_i_2 + abs(heights[i] - heights[i-2]);
		ans = min(oneStep, twoStep);

		// Swap
		height_i_2 = height_i_1;
		height_i_1 = ans;
	}
	printf("%d\n", ans);
	return 0;
}