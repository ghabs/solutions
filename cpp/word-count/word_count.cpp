#include "word_count.h"
#include <boost/algorithm/string.hpp>
#include <iostream>

namespace word_count {
  std::map<std::string, int> words(std::string field) {
    std::map<std::string, int> output;
    std::vector<std::string> vec;
    boost::split(vec, field, boost::is_space() || boost::is_any_of(".,:;"));
    for (std::string i : vec){
      boost::trim_if(i, boost::is_punct());
      boost::to_lower(i);
      if (i.length() == 0) continue;
      if (output.find(i) != output.end() ){
          //does this pass by value or reference?

          output[i]++;
      }
      else {
        output[i] = 1;
      }
    }
    return output;
  }
}
