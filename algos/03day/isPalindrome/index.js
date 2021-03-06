/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  const str1 = "a x a";
  const expected1 = true;
  
  const str2 = "racecar";
  const expected2 = true;
  
  const str3 = "Dud";
  const expected3 = false;
  
  const str4 = "oho!";
  const expected4 = false;
  
  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
  function isPalindrome(str) {
    for(let i = 0; i < Math.floor(str.length/2); i++){
        if(str[i] !== str[str.length - 1 - i]){
            return false
        }
    }
    return true
  }

  function isPalindrome2(str){
    let reversedStr = str.split("").reverse().join("")
    console.log(reversedStr)
    if(reversedStr === str){
        return true
    }
    else{
        return false
    }
  }

//   console.log(isPalindrome(str1))
//   console.log(isPalindrome(str2))
//   console.log(isPalindrome(str3))
//   console.log(isPalindrome(str4))
  console.log(isPalindrome2(str1))
  console.log(isPalindrome2(str2))
  console.log(isPalindrome2(str3))
  console.log(isPalindrome2(str4))