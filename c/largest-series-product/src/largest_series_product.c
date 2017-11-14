#include "largest_series_product.h"
#include <stdio.h>

int largest_series_product(char * number, int range){
  int current = 1; int max = 0; int i = 0; int count = 0;
  if (range == 0) return 1;
  if (number == "") return -1;
  while (*(++number) != '\0') {
    count++;
    if ((*number - '0') > 9) return -1;
    if (*number - '0' == 0) { i = 0; current = 1; continue;}
    if (i >= range) {current /= *(number - range) -'0'; i--;}
    current *= *number - '0';
    if ((current > max) && (i >= range-1)) {max = current;}
    i++;
  }
  if (count < range) return -1;
  return max;
}
