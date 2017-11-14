#include "pangram.h"


int is_pangram(const char* word) {
    int bf = 0; char c; int i = 0;
    if (word == 0) return 0;
    while ((c = word[i]) != '\0'){
        if (c >= 'A' && c <= 'Z') {c -= 'A'; bf |= (1 << c);}
        else if (c >= 'a' && c <= 'z') {c-= 'a'; bf |= (1 << c);}
        i++;
    }
    if (bf == 67108863) { return 1; }
    return 0;
}