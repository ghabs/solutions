#include "anagram.h"
#include <algorithm>
#include <iostream>

namespace anagram {
    anagram::anagram(std::string nsubject){
       std::transform(nsubject.begin(), nsubject.end(), nsubject.begin(), ::tolower);
       this->subject = nsubject;
    }
    std::vector<std::string> anagram::matches(std::vector<std::string> words) {
      std::vector<std::string> matched_words;

      for (size_t i = 0; i < words.size(); i++) {
        std::string testWord = words[i];
        std::transform(testWord.begin(), testWord.end(), testWord.begin(), ::tolower);
        if (isAnagram(testWord) && !sameWord(testWord)) {
          matched_words.push_back(words[i]);
        }
      }
      return matched_words;
    }
    bool anagram::isAnagram(std::string s) {
      std::string test = anagram::subject;
      std::sort(s.begin(), s.end());
      std::sort(test.begin(), test.end());
      return s==test;
    }
    bool anagram::sameWord(std::string s) {
      return s==anagram::subject;
    }
}; //namespace anagram
