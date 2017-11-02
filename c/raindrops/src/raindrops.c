#include "raindrops.h"
#include <stdio.h>
#include <string.h>
#include <math.h>

void convert(char* result, int drop){
  int i = 0;
  char pling[] = "Pling";
  char plang[] = "Plang";
  char plong[] = "Plong";
  if (drop % 3 == 0){
    strcat(result, pling);
    i += 5;
  }
  if (drop % 5 == 0){
    strcat(result, plang);
    i += 5;
  }
  if (drop % 7 == 0){
    strcat(result, plong);
    i += 5;
  }
  if (i == 0){
    printf("%i\n", drop);
    //Get the length of the int
    int d = (drop == 0 ? 1 : (int)(log10(drop)+1));
    //Add an additional 1 because of \n
    snprintf(result, d + 1, "%i", drop);
  }

}
