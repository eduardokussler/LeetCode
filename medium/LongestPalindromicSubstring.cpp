#include <string>
#include <set>
#include <list>
#include <sstream>
#include <iostream>

int main() {
    // std::string input = "babad";
    std::string input = "cbbd";
    // std::string input = "a";
    // std::string input = "bb";
    int palindromeStartIndex = 0;
    int palindromeEndIndex = 0;

    int currentPalindromeLength = palindromeEndIndex - palindromeStartIndex;

    for (int index = 0; index < input.length(); index++) {
         // odd length palindrome
        int leftPosition = index;
        int rightPosition = index;
        while (leftPosition >= 0 && rightPosition < input.length() && input[leftPosition] == input[rightPosition]) {
            int candidatePalindromeLength = rightPosition - leftPosition + 1; // + 1 because the end position is exclusive ( ]
            if (candidatePalindromeLength > currentPalindromeLength) {
                palindromeStartIndex = leftPosition;
                palindromeEndIndex = rightPosition + 1; // + 1 because the end position is exclusive ( ]
                currentPalindromeLength = candidatePalindromeLength;
            }
            leftPosition--;
            rightPosition++;
        }
        // even length palindrome
        leftPosition = index;
        rightPosition = index + 1;
        while (leftPosition >= 0 && rightPosition < input.length() && input[leftPosition] == input[rightPosition]) {
            int candidatePalindromeLength = rightPosition - leftPosition + 1; // + 1 because the end position is exclusive ( ]
            if (candidatePalindromeLength > currentPalindromeLength) {
                palindromeStartIndex = leftPosition;
                palindromeEndIndex = rightPosition + 1; // + 1 because the end position is exclusive ( ]
                currentPalindromeLength = candidatePalindromeLength;
            }
            leftPosition--;
            rightPosition++;
        }
    }

    std::cout << "Longest palindrome is " << input.substr(palindromeStartIndex, currentPalindromeLength) << std::endl;
    
    return 0;
}