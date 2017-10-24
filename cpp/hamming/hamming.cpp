#include "hamming.h"
#include <stdexcept>

using namespace std;

namespace hamming {
  uint compute(std::string a, std::string b) {
    if (a.size() != b.size()) {
      throw std::domain_error("strings are of unequal length");
    }
    uint count = 0;
    for (uint i = 0; i <= a.size(); ++i) {
      if (a[i] != b[i]) {
        count++;
      };
    }
    return count;
  }

} // namespace hamming
