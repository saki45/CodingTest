#include<stdlib.h>
#include<stdio.h>

inline void swapInt(int *p1, int *p2){

	int tmp = *p1;
	*p1 = *p2;
	*p2 = tmp;

}

void printArray(int *pArr, int nSize){

	int idx = 0;
	for(idx=0; idx<nSize; idx++)
		printf("%d", pArr[idx]);

	printf("\n");
}

void permutation(int *pArr, int *pCur, int nSize){

	if(pCur-pArr == nSize-1)
		printArray(pArr, nSize);
	else{
		int *pTmp = pCur;
		while(pTmp-pArr<nSize){
			swapInt(pTmp, pCur);
			permutation(pArr, pCur+1, nSize);
			swapInt(pTmp, pCur);
			pTmp++;
		}
	}
}

int compare(const void *a, const void *b){
	return *((int*)a) - *((int*)b);
}

int nextPermutation(int *pArr, int nSize){
	int idx = 0;
	for(idx=nSize-2; pArr[idx]>pArr[idx+1] && idx>=0; idx--)
		;

	// no next permutation
	if(idx<0)
		return 0;
	else{
		// switch with the 'ceil' element in the rightwards element
		int tIdx = nSize-1;
		while(tIdx>=idx && pArr[tIdx]<pArr[idx])
			tIdx--;
		swapInt(&pArr[idx], &pArr[tIdx]);

		if(idx<nSize-2)
			qsort(pArr+idx+1, nSize-idx-1, sizeof(int), compare);	
		return 1;
	}
}

void permutationOrder(int *pArr, int nSize){
	qsort(pArr, nSize, sizeof(int), compare);
	printArray(pArr, nSize);

	while(nextPermutation(pArr, nSize))
		printArray(pArr, nSize);
}

int main(){
	int pArr[4] = {1, 2, 3, 4};
	//permutation(pArr, pArr, 4);
	//printf("------------------------------\n");
	permutationOrder(pArr, 4);
}
