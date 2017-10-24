#ifndef ETL_H
#define ETL_H
#include <string>
#include <map>
#include <vector>

namespace etl {
  const std::map<char, int>  transform (std::map<int, std::vector<char>> m);
  void dump_map(const std::map<char, int>&);
} //namespace etl

#endif
