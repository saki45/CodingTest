# include <stdio.h>
# include <stdlib.h>
# include <string.h>

// This problem checks whether one string is the rotation of the other
// Example:
// ABCDE/CDEAB   -- True

int stringRotationCheck(char *pStr1, char *pStr2){

	// Check NULL pointer
	if(pStr1 == NULL || pStr2 == NULL){
		printf("NULL input string\n");
		return 0;
	}

	printf("%s\n", pStr1);
	printf("%s\n", pStr2);

	int nLength1 = strlen(pStr1);
	int nLength2 = strlen(pStr2);

	// Check whether one string is of length 0
	if(nLength1 == 0 || nLength2 == 0){
		printf("Input string with length 0.\n");
		return 0;
	}
	
	// Check if the length of two strings are the same
	if(nLength1 != nLength2){
		printf("The length of two strings is not the same.\n");
		return 0;
	}

	// Duplicate the first string
	char *pStr1Dup = (char*)malloc(nLength1*2*sizeof(char) + 1);
	pStr1Dup[0] = '\0';
	strcat(pStr1Dup,pStr1);
	strcat(pStr1Dup,pStr1);

	// check whether pStr2 is a substring of pStr1Dup
	if(strstr(pStr1Dup, pStr2) != NULL){
		printf("\"%s\" is a rotation of \"%s\".\n", pStr2, pStr1);
		return 1;
	}
	else{
		printf("\"%s\" is not a rotation of \"%s\".\n", pStr2, pStr1);
		return 0;
	}

	free(pStr1Dup);
}

int main(){
   	char *str1 = "ABCD";
    	char *str2 = "1234";
	int a = stringRotationCheck(str1, str2);

	
	stringRotationCheck("ABCD","DABC");
	stringRotationCheck("","");
	stringRotationCheck("A","A");
	stringRotationCheck("ABC","ACB");
	stringRotationCheck("ABCD","DAB");
	

	return 0;	
}
