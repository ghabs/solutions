#ifndef ANAGRAM_H
#define ANAGRAM_H
#include <string>
#include <vector>

namespace anagram {
  class anagram {
  private:
    std::string subject;
  public:
    anagram(std::string input);
    std::vector<std::string> matches( std::vector<std::string> words );
    void set_subject(std::string);
    bool isAnagram(std::string s);
    bool sameWord(std::string s);
  };
} //namespace anagram


#endif
