#include <stdio.h>

int main(void) {
	// your code goes here
	int x;
	float y,r;
	scanf("%d %f",&x,&y);
    if(x%5==0&&y>x+.5){
        r=(y-x)-.5;
        
        printf("%.2f",r);
    }
    else{
        printf("%.2f",y);
    }
	return 0;
}

