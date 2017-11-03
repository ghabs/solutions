#include "bob.h"

const char* hey_bob(const char* msg){
  const char* i = msg; int lower = 0; char lc = '\0'; int caps = 0;
  while (*i != '\0') {
    if (*i >= 97 && *i <= 122) lower++;
    if (*i >= 65 && *i <= 90) caps++;
    i++;
    if (*i != ' ' && *i != '\0') lc = *i;
  }
  if (lc == '\0') return "Fine. Be that way!";
  if (!lower && caps) return "Whoa, chill out!";
  if (lc == '?') return "Sure.";
  if (msg) return "Whatever.";
  return "Fine. Be that way!";
}
