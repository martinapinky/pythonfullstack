// for Loop
// Write a for loop to generate a Fibonacci sequence of a given length n.
// const n = 10;
// let a = 0, b = 1;
// console.log(a);
// console.log(b);
// for(let i = 2; i < n; i++) {
//     const c = a + b;
//     console.log(c);
//     a = b;
//     b = c;
// }

// Write a for loop to find all prime numbers between 1 and 50.
// for (let i = 2; i < 50; i++) {
//     let isPrime = true;    
//     for (let j = 2; j < i; j++) {
//         if (i % j === 0) {
//             isPrime = false;
//             break;
//         } 
//     }
//     if (isPrime) {
//         console.log(i);
//     }
// }

// 2. while Loop
// Use a while loop to print all numbers in reverse order from 100 to 1.
// i = 100;
// while(i > 0) {
//     console.log(i);
//     i--;
// }

// Write a while loop to repeatedly divide a number by 2 until it becomes less than 1. Count the number of divisions.
// n = 100;
// count = 0;
// console.log(n);
// while(n >= 1) {
//     count++;
//     n = n / 2;
//     console.log(n);
// }
// console.log("Number of divisions: ", count);

// 3. do...while Loop
// Use a do...while loop to prompt the user to enter a number greater than 10. 
// Continue prompting until the condition is met.
// let number;
// do {
//     number = parseInt(prompt("Enter number greater than 10:"));
// } while (number < 10);

// Write a do...while loop to find the sum of digits of a number.
// let num = 256;
// let numArray = num.toString().split("");
// let i = 0;
// sum = 0;
// do {
//     sum += parseInt(numArray[i]);
//     i++;
// } while (i < numArray.length);
// console.log(sum);

// 4. for...of Loop
// Use a for...of loop to filter out all odd numbers from an array.
// const array = [1, 2, 3, 4, 5, 6];
// const filteredArray = [];
// for (const value of array) {
//     if (value % 2 === 0) {
//         filteredArray.push(value);
//     }
// }
// console.log(filteredArray);

// Write a for...of loop to concatenate all strings in an array into a single string.
// array1 = ["I", "am", "in", "India"];
// singleString = "";
// for (str of array1) {
//     singleString = singleString + "str";
// }
// console.log(singleString);

// 5. for...in Loop
// Write a for...in loop to calculate the total of all numeric values in an object.
// const obj = {a:1, b:2, c:3};
// let sum = 0;
// for (key in obj) {
//     if (typeof(obj[key]) === "number") {
//         sum += obj[key];
//     }
// }
// console.log(sum);

// Write a for...in loop to create a string of all the keys in an object, separated by commas.
// let string = "";
// for (const key in obj) {
//     string = string + ", " + key;
// }
// console.log(string.slice(2));

// 6. Array.prototype.forEach()
// Use forEach to calculate the product of all numbers in an array.
// const array1 = [1, 2, 3, 4, 5];
// let product = 1;
// array1.forEach((element) => {
//     product = product * element;
// });

// console.log(product);

// product = array1.reduce((acc, n) => acc * n);

// Write a program using forEach to count the occurrences of each character in a string.

// 7. Array.prototype.map()
// Use map to create a new array where each element is the square of the original array.
// const array2 = [1, 2, 3, 4, 5];
// const newArray2 = array2.map(element => element * element);
// console.log(newArray2);

// Write a program using map to capitalize the first letter of each word in an array.
// const array3 = ["i", "am", "in", "india"];
// const newArray3 = array3.map(element => element.charAt(0).toUpperCase() + element.slice(1));
// console.log(newArray3);

// 8. Array.prototype.filter()
// Use filter to create a new array containing only the numbers greater than 10 from the original array.
// const array4 = [1, 2, 3, 4, 5, 10, 20, 30, 40];
// const newArray4 = array4.filter((x) => x > 10);
// console.log(newArray4);

// Write a program using filter to extract all words that start with the letter "a" from an array.
// const array5 = ["alinda", "martina", "pinky"];
// const newArray5 = array5.filter((x) => x.startsWith("a"));
// console.log(newArray5);

// 9. Array.prototype.reduce()
// Use reduce to find the maximum number in an array.
// const array4 = [1, 2, 3, 4, 5, 10, 20, 30, 40];
// maxNumber = array4.reduce((acc, n) => n > acc ? n : acc);
// console.log(maxNumber);

// Write a program using reduce to concatenate all elements of an array into a single string.
// const array3 = ["i", "am", "in", "india"];
// string = array3.reduce((acc, element) => acc.concat(element));
// console.log(string);

// 10. Recursion
// Write a recursive function to calculate the sum of all numbers from 1 to n.
// function calculateSum (n) {
//     if(n===1)
//         return 1;
//     return n + calculateSum(n - 1);
// }
// console.log(calculateSum(3));

// Write a recursive function to reverse a string. 
function reverseString(str) {
    if (str === "") {
        return "";
    }
    return str.charAt(str.length - 1) + reverseString(str.substring(0, str.length - 1));
}
console.log(reverseString("hello"));