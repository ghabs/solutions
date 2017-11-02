#include "hamming.h"

int compute(const char * a, const char * b){
  int i = 0; int count = 0;
  if (!a || !b) { return -1; }
  for (;;i++) {
    if (a[i] != b[i]) { count++; }
    if (a[i] == '\0' || b[i] == '\0') { break; }
  }
  if (a[i] != b[i]) {return -1; }
  return count;
}
