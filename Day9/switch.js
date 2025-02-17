// switch
// switch(expression) {
//     case value1:
//         //cose to execute if expression === value1
//         break;
//     case value2:
//         //cose to execute if expression === value1
//         break;
//     default:
//         //code to execute if none of the cases match
// }

let day = 3;
switch (day) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    default:
        console.log("Some other day");
}

let fruit = "apple";

switch(fruit) {
    case "apple":
        console.log("This is pome fruit");
        break;
    case "orange":
        console.log("This is citrus fruit");
        break;
    default:
        console.log("Unknown fruit");
}

// Calculator
 let a = 5, b = 3, operation = "+";

 switch(a, b, operation) {
    case "+":
        console.log(`${a} + ${b} = ${a + b}`);
        break;
    case "-":
        console.log(`${a} - ${b} = ${a - b}`);
        break;
    case "*":
        console.log(`${a} * ${b} = ${a * b}`);
        break;
    case "/":
        console.log(`${a} / ${b} = ${a / b}`);
        break;
    default:
        console.log("Unknown operator. Please use + - * / signs");
 }

 