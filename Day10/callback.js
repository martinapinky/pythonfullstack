// functions as first class citizens
// higher order function can accept a function as an argument

function greet(callback) {
    console.log("hi");
    callback();
}

function greetnxt() {
    console.log("good morning");
}

greet(greetnxt);

const numbers = [4, 2, 1, -2, -1, 5];

const posNumbers = removeneg(numbers, (num) => num >= 0);

function removeneg(numbers, callback) {
    const arr = [];
    for (const num of numbers) {
        if (callback(num)) {
            arr.push(num);
        }
    }
    return arr;
}

console.log(posNumbers);

const double = numbers.map((num) => num * 2);
console.log(double);

console.log("Start");
setTimeout(() => {      //Asynchronous
    console.log("Timer completed")
}, 3000);
console.log("Timer Initiated");

// callback hell --> pyramid of doom

function task1(callback) {
    setTimeout(() => {
        console.log("Task 1 is completed");
        callback();
    }, 1000);
}

function task2(callback) {
    setTimeout(() => {
        console.log("Task 2 is completed");
        callback();
    }, 1000);
}

function task3(callback) {
    setTimeout(() => {
        console.log("Task 3 is completed");
        callback();
    }, 1000);
}

task1(() => {
    task2(() => {
        task3(() => {
            console.log("All tasks completed");
        });
    });
});


// Promises - ojbect

//3 states --> pending --> initial state, promise has neither been fulfilled or rejected
        // --> fullfilled --> The operation is successful and you are getting a resolve
        // --> rejected --> The operation has failed

let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let success = false;
        if (success) {
            resolve("Promise resolved");
        } else {
            reject("Promise rejected");
        }
    }, 3000)
});

promise
    .then((success) => {
        console.log(success);
    })
    .catch((error) => {
        console.log(error);
    });

    console.log("step : Start"); //Synchronous

////////////bunch of missing stuff