//arrays - special type of object used to store values

//creating
let arr = [1, 2, 3, 4, "5"];
console.log(arr);
//array constructor
let array = new Array(3);
console.log(array);
//array.of
// let arr1 = Array.of(3);
// console.log(arr1);
console.log(arr.length);
// indexOf
// lastIndexOf

// modifying array
arr.push(3);  //Add element to the end of the array
console.log(arr);

arr.pop();  //Remove last element of the array
console.log(arr);

arr.unshift(1); //Add element to the beginning of the array
console.log(arr);

arr.shift();  //Removes first element from the array
console.log(arr);

let arr1 = [1, 2, 3, 51];
let arr2 = [2, 3, 51];
console.log(arr1.concat(arr2));
let arr3 = [1, 2, 3, 5, 5];
arr3.splice(1, 2, 4, 8) //removed element from any position
console.log(arr3)

// forEach
arr3.forEach((element) => console.log(element));  //creates a new array
// map
const newarr = arr3.map((x) => x*2);
console.log(newarr);
console.log(arr3)
//filter
const filteredarr = arr3.filter((x) => x > 4);
console.log(filteredarr);
//reducer
// let sum = arr3.reduce((arr, x) > acc + x, 0);
// console.log(sum);

//some 
//every
//find
console.log(arr3);
let found = arr3.find((x) => x === 5);
console.log(found);
