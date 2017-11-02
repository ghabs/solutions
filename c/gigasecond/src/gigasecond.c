#include "gigasecond.h"
#include <stdio.h>

time_t gigasecond_after(time_t birth){
  return (1000000000 + birth);
}
