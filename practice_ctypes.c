#include<stdio.h>

double add(int size, double *array, double *result){
    for(int i = 0; i < size; i++){
        result[0] = result[0] + array[i];
        //printf("%f", result[0]);
    }
}

/*
int main(){
    double *result = (double *) malloc(sizeof(double));
    int size = 100;
    double *array = (double *) malloc(size*sizeof(double));
    for(int i = 0; i < size; i++){
        array[i] = i;
    }

    printf("%f\n", add(size, array, result));

    return(0);
}
*/