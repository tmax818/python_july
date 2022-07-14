/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  function encodeStr(str) {
    const freqTable = {}
    let newstr = ""
    for(let i = 0; i < str.length; i++){
        if(freqTable[str[i]]){
            freqTable[str[i]] += 1
        } else {
            freqTable[str[i]] = 1
        }
    }
    console.log(freqTable)
    for(let i = 0; i < str.length; i++){
        if(str[i] !== str[i + 1] && freqTable[str[i]])
        newstr += `${str[i]}${freqTable[str[i]]}`
    }

    return newstr.length >= str.length ? str : newstr
  }

  console.log(encodeStr(str1))
  console.log(encodeStr(str2))
  console.log(encodeStr(str3))
  console.log(encodeStr(str4))