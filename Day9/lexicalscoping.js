// lexical scoping - the function scope is determined by its positionn in the source code. 

function outer() {
    let outervar = "I am the outer var";
    function inner() {
        console.log(outervar);
    }
    inner();
}
outer();

function createCounter() {
    let count = 0;
    return {
        increment() {
            count++;
            console.log(count);
        },
        decrement() {
            count--;
            console.log(count);
        }
    };
}

const counter1 = createCounter();
counter1.increment();
counter1.decrement();

const counter2 = createCounter(); //separate closure
counter2.increment();

// Hoisting --- function declarations and variable declarations are moved to the top during run time.
// Arrow functions and function expressions don't support hoisting
greet();
function greet() {
    console.log("Hello");
}

//variable - only the variable declaration is hoisted, not the initialization
// console.log(x);  
// var x = 1;

// console.log(x);  //Reference error 
// let x = 1;
// //let and const --> Accessing the variable before declaration throws a reference errors

// function greet(name) {
//     console.log(`This is ${this.name}`);
// }
// greet("Anna"); // this returns undefined

// const person = {name: "Anna"};

// const new1 = greet.bind(person); //function binding
// console.log(new1);
// new1();

//arrow functions do not have their own this. they inherit from the surrounding lexical scope.

const person = {
    name: "John",
    age: 21,
    greet: function() {
        console.log(this.name);
    }
}

function outer() {
    const self = this;
    self.name = "John";
    const greet = () => {
        console.log(this.name)
    };
    greet();
}

outer();

const p1 = {
    name: "John;",
    greet: function() {
        const innergreet = () => {
            console.log(this.name);
        };
        innergreet();
    }
}

p1.greet();