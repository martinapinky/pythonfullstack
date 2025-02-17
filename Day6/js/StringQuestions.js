// string reverse

function reverseString(str) {
    return str.split("").reverse().join("");
}
// console.log(reverseString("hello"));

// Check Palindrome
function isPalindrome(str) {
    return str.split("").reverse().join("") === str;
}
console.log(isPalindrome("ollehello"));