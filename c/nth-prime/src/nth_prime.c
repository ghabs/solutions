#include "nth_prime.h"
#include <stdio.h>

int nth(int n){
    int primes[n];
    primes[n] = 0; int k = 2; int j = 1; int p;
    if(n == 0) return 0;
    while(primes[n] == 0){
        for (p = 2; p < k; p++){
            if (k % p == 0){
                break;      
            }
        }
        if (p == k){
            primes[j] = k;
            j++;
        }
        k++;
    }
    return primes[n];
}