// looping mechanism
//1. for loop

//for(initialization ; condition ; increment/decrement)

for(let i = 0; i < 5; i++) {
    console.log(i);
}

//while
let i = 0;
while(i < 5) {
    console.log(i);
    i++;
}

//do ..while  //executes atleast once
let j = 5;
do {
    console.log(j);
    j++;
} while (j < 5);

//for ..of loop
const array = ['a', 'b', 'c'];
for(const value of array) {
    console.log(value);
}

//for ..in
const obj = {a:1, b:2, c:3};
for (key in obj) {
    console.log(key, obj[key]);
}

const array1 = ['a', 'b', 'c'];
for(const index in array1) {
    console.log(index);
}

//forEach ==> Array
//callback functions

const arr = [1, 2, 3];
arr.forEach((item, index) => {
    console.log(item,index)
});

// continue statement --> skips the current iteration and moves to the next one
for (i = 0; i < 10; i++) {
    if(i == 5)
        continue;
    console.log(i);
}

// break statement --> break the loop when condition is met
for (i = 0; i < 10; i++) {
    if(i == 5)
        break;
    console.log(i);
}

// factorial n * (n - 1) * (n - 2) * (n - 3) * ...1
function factorial(n) {
    if(n===0)
        return 1;
    return n * factorial(n - 1);
}
console.log(factorial(5));

//fibonaci --> 0 1 1 2 3 5 8 13 21...
const n = 10;
let a = 0, b = 1;
console.log(a);
console.log(b);
for(let i = 2; i < n; i++) {
    const c = a + b;
    console.log(c);
    a = b;
    b = c;
}