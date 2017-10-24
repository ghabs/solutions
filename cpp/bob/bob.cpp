#include "bob.h"
#include <cctype>

namespace bob {
  const std::string whiteSpaces( " \f\n\r\t\v" );


  void trimRight( std::string& str,
        const std::string& trimChars = whiteSpaces )
  {
     std::string::size_type pos = str.find_last_not_of( trimChars );
     str.erase( pos + 1 );
  }

  std::string hey(std::string convo){
    //strip trailing whitespace
    //if str size is 0 return "Fine. Be that way!"
    //if all chars are caps, respond with "Whoa, chill out!"
    //if last char is a ? then respond "Sure."
    //else return Whatever.
    bob::trimRight(convo);
    uint convo_size = convo.size();
    if (convo_size == 0) {
      return "Fine. Be that way!";
    }
    bool check = true;
    bool one_letter = false;
    int i = 0;
    while (i <= convo_size && check) {
      ++i;
      if(islower(convo[i])){ check = false; }
      if(isalpha(convo[i])){ one_letter = true; }
      if (i == convo_size && one_letter){
        return "Whoa, chill out!";
      }
    }
    if ((convo[convo_size  - 1]) == '?') {
      return "Sure.";
    }
    return "Whatever.";
  }
} // namespace bob
