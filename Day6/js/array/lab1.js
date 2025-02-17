// Write a function that takes a string as input and returns the string reversed.
function reverseString(str) {
    return str.split("").reverse().join("");
}

// Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).
function isPalindrome(str) {
    return str.split("").reverse().join("") === str;
}
// console.log(isPalindrome("ollehello"));

// Write a function that converts a string into an array of words.
function convertToArrayOfWords(str) {
    return str.split(" ");
}
// console.log(convertToArrayOfWords("Hello World"));

// Write a function to count how many times a particular character appears in a string.
function characterCount(str, char) {
    const strarr = str.split("");
    filteredarr = strarr.filter((x) => x === char)
    return filteredarr.length;
}
// console.log(characterCount("Hello", "l"));

// Write a function that replaces all occurrences of a substring with a new string.
function replaceSubString(str, substr, newstr) {
    return str.replaceAll(substr, newstr);
}
// let mystr = "my people and my friends and my family";
// console.log(replaceSubString(mystr, "my", "your"));

// Write a function that removes all duplicate characters from a string.
function removeDuplicates(str) {
    let strarr = str.split("");
    return strarr.filter((x) => characterCount(str, x) === 1).join("");
    
    // let strarr = str.split("");
    // let newarr = [];
    // strarr.forEach((element) => {
    //     if(str.indexOf(element) == str.lastIndexOf(element)) {
    //         newarr.push(element);
    //     }
    // });
    // return newarr.join("");
}
// console.log(removeDuplicates("Hello World"));

// Write a function that converts a string to title case (each word starts with a capital letter).
function camelCaseWord(str) {
    let strarr = str.split("");

    //Convert first letter to uppercase
    const firstChar = strarr[0].toUpperCase();

    //Convert the rest of the word to lowercase
    strarr.shift()
    const restOfWord = strarr.join("").toLowerCase();
    return firstChar.concat(restOfWord);
    //Use CharAt and Splice....
}

function camelCaseString(str) {
    let strarr = convertToArrayOfWords(str);
    strarr[0] = camelCaseWord(strarr[0]);
    return strarr.reduce((acc, x) => acc.concat(` ${camelCaseWord(x)}`));
}
// console.log(camelCaseString("hello world, save the children"));

// Write a function to find the first non-repeated character in a string.
function nonRepeatedChar(str) {
    return removeDuplicates(str)[0];
}
// console.log(nonRepeatedChar("Hello World"));

// Write a function that removes whitespaces from the beginning and end of a string.
function removeWhiteSpace(str) {
    return str.trim();
}
// console.log(removeWhiteSpace(" Hello World "));

// Write a function that finds the length of the longest word in a string.
function longestWordLength(str) {
    strarr = convertToArrayOfWords(str);
    let longestLength = 0;
    strarr.forEach((element) => {
        longestLength = element.length > longestLength ? element.length : longestLength;
    });
    return longestLength;
}
// console.log(longestWordLength("Hello World, save the children"));

// Write a function that returns the index of the last occurrence of a given character in a string.
function lastIndexOf(str, char) {
    return str.lastIndexOf(char);
}


// Write a function that extracts a substring from a string based on given start and end indices.
function extractSubstring(str, start, end) {
    return str.substring(start, end);
}
// console.log(extractSubstring("Hello World", 0, 5));

// Write a function to pad a string with a specific character until it reaches a specified length
function padString(str, char, length) {
    return str.padStart(length, char);
}
console.log(padString("Hello World", "$", 20));