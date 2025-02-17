// console.log("Hello World");

// const example = () => {
//     if (true) {
//         let a = 2;
//         console.log(a);
//     }
// }
// example();

// let a = {};
// console.log(typeof(a));

// let a = "Hello, John said \"Hello\"";
// console.log(a);

// let a = `This is Multi line
// multi line
// `
// console.log(a);

// console.log("6"/"2");

// let str = "123";
// console.log(Number(str));
// console.log(typeof(str));

// let str2 = "123n";
// console.log(Number(str2));

// console.log(Boolean(1));
// console.log(Boolean(0));
// console.log(Boolean("hello"));
// console.log(Boolean(""));
// console.log(Boolean("0"));
// console.log(Boolean(" "));

// console.log("6"+ 5 - 2);
// console.log("6"+ 5 * 2);

// Function Expression - when working with callbacks
// const greet = function greet(name) {
//     console.log(`Hello ${name}`);
// }

// greet("Alice");

// Arrow function - don't have this context and inherit from surrounding context
const greet = (name) => {
    console.log(`Hello ${name}`);
}
greet("Alice");

