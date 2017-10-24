#include "etl.h"
#include <iostream>
#include <cctype>

namespace etl {
  void dump_map(std::map<char, int>& map) {
    for ( std::map<char,int>::const_iterator it = map.begin(); it != map.end(); it++) {
      std::cout << "Key: " << it->first << std::endl;
      std::cout << "Values " << it->second << std::endl;
    }
  }
    const std::map<char, int> transform(std::map<int, std::vector<char>> m){
      std::map<char, int> output = {};
      for (auto const &ent1 : m) {
        auto const &inner_vector = ent1.second;
        for (auto i : inner_vector) {
          i = std::tolower(i);
          output[i] = ent1.first;
        }
      }
      //dump_map(output);
      return output;
    }

} //etl
