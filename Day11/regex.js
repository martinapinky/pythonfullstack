// Regular Expressions in JavaScript
// Regular Expressions (regex) are patterns used to match character combinations in strings. In JavaScript, regular expressions provide a powerful way to search, validate, and manipulate text by defining patterns that can match specific string sequences.
// Syntax of Regular Expressions:
// A regular expression is usually written between two forward slashes (/), like this: /pattern/. The pattern can be any sequence of characters and special symbols that defines what you're looking for in the string.
// For example:
// /abc/ matches the exact sequence "abc".
// /\d/ matches any digit.
// Basic Components of Regular Expressions
// Literals:
// Normal characters are treated as literals (e.g., /hello/ will match the exact string "hello").
// Case sensitivity: /hello/ will match "hello" but not "Hello" or "HELLO".
// Metacharacters: These characters have special meaning:
// . (dot): Matches any character except newlines.
// Example: /h.llo/ will match "hello", "hxllo", etc.
// ^: Anchors the regex to the start of the string.
// Example: /^hello/ matches "hello" only if it appears at the beginning.
// $: Anchors the regex to the end of the string.
// Example: /world$/ matches "world" only if it appears at the end.
// []: Defines a character class, matching any one of the characters inside the brackets.
// Example: /[aeiou]/ matches any vowel (a, e, i, o, u).
// |: Logical OR; matches either the pattern on the left or the right.
// Example: /cat|dog/ matches either "cat" or "dog".
// () (parentheses): Grouping constructs to apply operators to a sub-pattern.
// Example: /(abc)+/ matches one or more occurrences of "abc".
// Quantifiers:
// *: Matches 0 or more of the preceding element.
// Example: /a*/ matches "aaa", "aa", or an empty string.
// +: Matches 1 or more of the preceding element.
// Example: /a+/ matches "a", "aa", "aaa", etc.
// ?: Matches 0 or 1 of the preceding element.
// Example: /a?/ matches an empty string or "a".
// {n}: Matches exactly n occurrences of the preceding element.
// Example: /a{3}/ matches exactly "aaa".
// {n,}: Matches n or more occurrences.
// Example: /a{2,}/ matches "aa", "aaa", "aaaa", etc.
// {n,m}: Matches between n and m occurrences.
// Example: /a{2,4}/ matches "aa", "aaa", or "aaaa".
// Character Classes:
// \d: Matches any digit (equivalent to [0-9]).
// \D: Matches any non-digit.
// \w: Matches any word character (letters, digits, and underscores, equivalent to [A-Za-z0-9_]).
// \W: Matches any non-word character.
// \s: Matches any whitespace character (spaces, tabs, line breaks).
// \S: Matches any non-whitespace character.
// Escape Sequences:
// If you need to use a special character as a literal, you need to escape it with a backslash (\).
// Example: /\./ will match a literal period (.), not any character.
// Creating a Regular Expression:
// You can create a regular expression in two ways in JavaScript:
// Using a Regular Expression Literal: This is the most common and straightforward way to define a regular expression.

//  const regex = /hello/;
// Using the RegExp Constructor: This method is useful if you want to create a regular expression dynamically (e.g., with variables).

//  const regex = new RegExp("hello");


// const digitsRegex = /^\d+$/;

// console.log(digitsRegex.test("12345"));  // true
// console.log(digitsRegex.test("12a45"));  // false

const regex = /hello/;
const digitsRegex = /^\d+$/;

// console.log(regex.test("hello"));
// console.log(digitsRegex.test("12a45"));


const phoneRegex = /^[6789]\d{9}$/;
console.log(phoneRegex.test("9876543210")); // true
console.log(phoneRegex.test("1234567890")); // false

const optional = /colou?r/; 
console.log(optional.test("color"));  // true
console.log(optional.test("colour")); // true
console.log(optional.test("coloor")); // false

const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
console.log(passwordRegex.test("Strongpass1"));
console.log(passwordRegex.test("weakpass"));
console.log(passwordRegex.test("MyPassword"));
console.log(passwordRegex.test("12MyPassword"));
console.log(passwordRegex.test("12mypassword"));