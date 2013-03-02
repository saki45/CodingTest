#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_OF_ELEMENT 20
#define MAX_VALUE 30

void printResult(int *pArr, int *pSub, int nRange){

	int idx = 0;
	for(idx=0; idx<=nRange; ++idx){
		if(pSub[idx])
			printf("%d ", pArr[idx]);
	}
	printf("\n");

}

void findSubSetSum(int *pArr, int *pSub, int nSize, int nIndex, int curSum, int nSum){

	if(curSum+pArr[nIndex] > nSum)
		return;

	if(curSum+pArr[nIndex] == nSum){
		pSub[nIndex] = 1;
		printResult(pArr, pSub, nIndex);
		pSub[nIndex] = 0;
		return;
	}

	if(nIndex < nSize-1){
		pSub[nIndex] = 1;
		findSubSetSum(pArr, pSub, nSize, nIndex+1, curSum+pArr[nIndex], nSum);
		pSub[nIndex] = 0;
		findSubSetSum(pArr, pSub, nSize, nIndex+1, curSum, nSum);
	}	
}	

int main() {
	int *pArr = (int*)malloc(NUM_OF_ELEMENT*sizeof(int));
	int *pSub = (int*)calloc(NUM_OF_ELEMENT, sizeof(int));

	srand(time(NULL));
	int idx = 0;

	for(idx=0; idx<NUM_OF_ELEMENT; ++idx)
		pArr[idx] = rand()%MAX_VALUE + 1;

	for(idx=0; idx<NUM_OF_ELEMENT; ++idx)
		printf("%d ", pArr[idx]);
	printf("\n");

	findSubSetSum(pArr, pSub, NUM_OF_ELEMENT, 0, 0, 2*MAX_VALUE);

	free(pArr);
	free(pSub);

	return 0;
}

