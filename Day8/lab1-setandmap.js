/////////////// Exercises on Set
// Remove Duplicates from an Array
// Write a function that removes all duplicates from an array using a Set.
function removeDuplicate(array) {
    return [...new Set(array)];
}

const numbers = [1, 2, 3, 4, 4, 5, 2];
console.log(removeDuplicate(numbers));

// Intersection of Two Arrays
// Find the common elements between two arrays using a Set.
const numbers1 = [1, 2, 3, 5, 6, 6, 8];

function commonElements(arr1, arr2) {
    const arrset = new Set(arr1);
    let commonElements = [];
    arr2.forEach(element => {
        if (arrset.has(element)) {
            commonElements.push(element)
        }
    });
    return commonElements;
}
console.log(commonElements(numbers, numbers1));

// Unique Characters in a String
// Write a function that checks if a string contains all unique characters.
function hasAllUniqueChars(str) {
    return str.length === [...new Set(str.split(""))].length;
}
console.log(hasAllUniqueChars("Hello World"));

// Count Unique Elements
// Write a function that counts the number of unique elements in an array using a Set.
function countUnique(arr) {
    return [... new Set(arr)].length;
}
console.log(countUnique(numbers));


/////////////////// Exercises on Map
// Count Frequency of Elements
// Write a function that counts the frequency of each element in an array using a Map.
function countFrequency(array){
    const countMap = new Map();
    array.forEach(item => {
    countMap.set(item, (countMap.get(item) || 0 ) + 1);
    });
    return countMap;
}
console.log(countFrequency(numbers));    

// Group by Property
// Given an array of objects, group the objects by a specified property using a Map.
const people = [
    { name: "Alice", age: 25},
    { name: "Bob", age: 25},
    { name: "Charlie", age: 30}
  ];
// console.log(Object.entries(people));
// console.log([...Object.values(people)]);
// console.log(people[0]["age"]); 
function groupObjectsByProperty(arr, property) {
    const propertyMap = new Map();
    arr.forEach((obj) => {
        value = propertyMap.get(obj[property]) || [];
        value.push(obj);
        propertyMap.set(obj[property], value);
    });
    return propertyMap;
}

console.log(groupObjectsByProperty(people, "age"));

// Remove Duplicate Keys
// Write a function that removes duplicate keys from an array of key-value pairs using a Map.
const array3 = [["name", "Alice"], ["name", "John"], ["age", "25"]];
function removeDuplicateKeys(arr) {
    const newMap = new Map();
    arr.forEach((element) => {
        newMap.set(element[0], newMap.get(element[0]) || element[1]);
    });
    return [...newMap];
}
console.log(removeDuplicateKeys(array3));

// Convert Map to Object
// Write a function to convert a Map into a plain JavaScript object.
const myMap1 = new Map();
myMap1.set('name', 'John');
myMap1.set('age', '25');
// console.log([...myMap1]);
function convertToObject(myMap) {
    return Object.fromEntries([...myMap]);
}
console.log(convertToObject(myMap1));

// Reverse a Map
// Write a function to reverse the keys and values of a Map.
function reverseKeyValues(myMap) {
    return new Map([...myMap].map((value) => value.reverse()));
}
console.log(reverseKeyValues(myMap1));