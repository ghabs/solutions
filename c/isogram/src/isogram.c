
#include "isogram.h"
#include <stdlib.h>
#include <stdio.h>

bool is_isogram(char * s) {
  unsigned int bf = 0;
  char c;
  for (size_t i = 0; i < (sizeof(s) / sizeof(char)); i++) {
    if(s[0] == '\0') { return true; }
    c = s[i];
    //normalize upper and lower case;
    if (c >= 'A' && c <= 'Z'){ c -= 'A'; }
    else if (c >= 'a' && c <= 'z') { c -= 'a'; }
    else { continue; }
    //checks if the value already exists in the bitfield
    if ((bf & (1 << c)) > 0) { return false; }
    //if it doesn't exist set it as 1;
    bf |= (1 << c);
  }
  return true;
}
