#include "acronym.h"
#include <ctype.h>
#include <stdlib.h>

char* abbreviate(char* msg){
  char* buf;
  buf = (char *)malloc(1024);
  size_t i = 0; size_t ii = 0;
  if (!msg) return NULL;
  while (msg[i] != '\0') {
    if (i == 0) {
      buf[i] = toupper(msg[i]);
      ii++; i++;
    }
    else if (isspace(msg[i]) || (msg[i] == '-')){
      buf[ii] = toupper(msg[i+1]);
      ii++ ; i+= 2;
    }
    else { i++; }
  }
  if (i == 0) { return NULL; }
  void* p = realloc(buf, ii);
  return (char *) p;
}
