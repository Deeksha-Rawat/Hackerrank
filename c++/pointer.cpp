#include <stdio.h>
#include<math.h>

void update(int *a,int *b) {
    int na,nb;
    na=*a+*b;
    nb=abs(*a-*b);
    *a=na;
    *b=nb;

    // Complete this function
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

