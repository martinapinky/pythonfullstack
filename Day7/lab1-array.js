// Create and Access Array Elements
// Create an array fruits with the elements ['apple', 'banana', 'cherry']. Log the second element of the array.
let arr1 = ['apple', 'banana', 'cherry'];
let [var1, var2, var3] = arr1;
console.log(var2);

// Add Elements to an Array
// Add the element 'orange' to the end of the fruits array. Log the updated array.
arr1.push('orange');
console.log(arr1);

// Remove Elements from an Array
// Remove the first element from the fruits array and log the updated array.
arr1.shift();
console.log(arr1);

// Find the Length of an Array
// Find and log the length of the fruits array.
console.log(arr1.length);

// Check if an Element Exists in an Array
// Check if the element 'banana' exists in the fruits array. Log a message indicating whether the element is present or not.
let found = arr1.find((x) => x === 'banana');
console.log((found ? "banana Exists in the array" : "banana Doesn't exist in the array"));

// Array Iteration Using forEach
// Use the forEach() method to log each fruit in the fruits array.
arr1.forEach((element) => {
    console.log(element);
});

// Filter Elements in an Array
// Use the filter() method to create a new array that only contains fruits that have more than 5 characters. Log the new array.
const filteredarr = arr1.filter((x) => x.length > 5);
console.log(filteredarr);

// Map Over an Array
// Use the map() method to create a new array where each fruit in the fruits array is converted to uppercase. Log the new array.
let uppercaseArr = arr1.map((x) => x.toUpperCase());
console.log(uppercaseArr);

// Find an Element in an Array
// Use the find() method to find the first fruit in the fruits array that has more than 5 characters. Log the result.
let fruit = arr1.find((x) => x.length > 5);
console.log(fruit);

// Reduce an Array
// Use the reduce() method to concatenate all the fruits in the fruits array into a single string with spaces in between. Log the result.
let string1 = arr1.reduce((str, element) => str.concat(` ${element}`));
console.log(string1);

const items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'];
const count = items.reduce((accumulator, currentValue) => {
  accumulator[currentValue] = (accumulator[currentValue] || 0) + 1;
  return accumulator;
}, {});
console.log(count)

// Sort an Array
// Sort the fruits array alphabetically and log the sorted array.
console.log(arr1.sort());

// Combine Two Arrays
// Combine the fruits array with another array ['grape', 'melon'] and log the new array.
arr2 = ['grape', 'melon'];
console.log(arr1.concat(arr2));

// Check if an Array Contains an Element
// Use the includes() method to check if the fruits array contains the element 'cherry'. Log the result.
console.log(arr1.includes('cherry'));

// Find the Index of an Element
// Use the indexOf() method to find the index of the element 'banana' in the fruits array. Log the result.
console.log(arr1.indexOf('banana'));

// Splice Elements in an Array
// Use the splice() method to remove the second element from the fruits array and add the element 'pear' in its place. Log the updated array.
arr1.splice(1, 1, 'pear');
console.log(arr1);

// Create an Array of Objects
// Create an array of objects representing books with properties: title, author, and year. Log the array.
let books = [
    { title: 'To Kill a Mockingbird', author: 'Harper Lee', year: 1960 },
    { title: '1984', author: 'George Orwell', year: 1949 },
    { title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', year: 1925 }
];
console.log(books);

// Access Nested Array Elements
// Given the array const library = [['Book1', 'Author1'], ['Book2', 'Author2']], access and log the author of the second book.
const library = [['Book1', 'Author1'], ['Book2', 'Author2']];
let [book1, book2] = library;
console.log(book2[1]);

// Flatten an Array
// Flatten a nested array const nestedArray = [[1, 2], [3, 4], [5, 6]] into a single array and log the result.
const nestedArray = [[1, 2], [3, 4], [5, 6]];
let flatArr = nestedArray.flat();
console.log(flatArr);

// Remove Duplicate Elements from an Array
// Remove duplicate elements from an array const numbers = [1, 2, 3, 2, 1, 4, 5] and log the result.
const numbers = [1, 2, 3, 2, 1, 4, 5];
let noDuplicatesArr = numbers.filter((x) => numbers.indexOf(x) === numbers.lastIndexOf(x));
console.log(noDuplicatesArr);

// Check if an Array is Empty
// Write a function to check if an array is empty and log the result for the array const arr = [].
function isEmpty(array1) {
    return array1.length === 0;
}
const arr = [];
console.log(isEmpty(arr));