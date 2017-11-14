#include "largest_series_product.h"
#include <stdio.h>

int largest_series_product(char* number, int places){
  //char arr[places];
  int current = (number[0] - '0'); int max = 0;
  int i = 1;

  for (; i < places; i++) {
    current *= (number[i]-'0');
  }
  if (current == 0) current = (number[i]-'0');
  while (number[++i] != '\0') {
    if (((number[i]-'0') == 0) || ((number[i-places]-'0') == 0)) current = 1;
    else {
    printf("%i\n", i);
    current *= (number[i]-'0');
    current /= (number[i-places]-'0');
    printf("%i\n", (number[i-places]-'0'));
    }
    if (current > max) max = current;

  }
  return max;
}
