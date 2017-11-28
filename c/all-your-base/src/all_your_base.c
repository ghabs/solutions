#include "all_your_base.h"
#include <math.h>
#include <stdlib.h>
#define MAX_SIZE 100


size_t rebase(int8_t * digits, int16_t inputbase, int16_t outputbase, size_t inputlength){
    size_t sum = 0;
    int8_t ds[MAX_SIZE];
    size_t dc = 0; int dig = 0; int rc = 0; int id = 0;
    if ((inputbase < 0) || (outputbase <= 1) || (digits[0]==0)) {digits[0] = 0; return dc;}
    for (int i = (inputlength-1); i >= 0; i--) {
        if ((digits[i] < 0) || (digits[i] >= inputbase)) { digits [0] = 0; return dc;}
        sum += digits[dig] * pow(inputbase, i);
        dig++;
    }
    while (sum > 0) {
        ds[dc] = sum % outputbase;
        sum /= outputbase;
        dc++;
    };
    rc = dc;
    while (rc-- >= 0) {
        digits[id] = ds[rc];
        id++;
    }
    return dc;
}
