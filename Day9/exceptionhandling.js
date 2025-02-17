//exception handling --> errors are handled gracefully

//common javascript errors
// 1. Syntax Error
// 2. Type Error e.g null.toString()
// 3. Reference Error - accessing a variable which is not defined
// 4. Range Error - number outside the valid ramge
// 5. URL Error - issue with encode URL and decode URL

try {
    let result = x / 0;
}
catch(error) {
    console.log(error.name);
    console.log(error.message);
}
finally {
    console.log("Execution has completed");
}


try {
    data = JSON.parse("invalidjson");
} 
catch(error){
    console.log(error.name);
    console.log(error.message);
} 
finally {
    console.log("Execution has completed");
}

function checkAge(age) {
    if (age < 18) {
        throw new Error("Age must be 18 years or older");
    }
    console.log("Access Granted");
}

try {
    checkAge(16);
} 
catch(error){
    console.log(error.name);
    console.log(error.message);
} 
finally {
    console.log("Execution has completed");
}

//nullish coalescing (??)
height = height ?? 0;

console.log(Math.trunc(1.83));
if (!Math.trunc) {
    Math.trunc = function(number) {
        //
    }
}

// core.js - polyfill

// Babel - transpiler