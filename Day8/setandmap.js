// set is a collection of unique values
// values can be primitive or object
// maintains the insertion order

const set = new Set();

console.log(set);

//methods of set
set.add(1);
set.add(2);
set.add(1);

console.log(set);

// delete method
set.delete(2);
console.log(set);

// has
console.log(set.has(2));

// clear
console.log(set.clear());
set.delete(2);
console.log(set);

// size
console.log(set.size);

// Iteration methods
set.add(1);
set.add(2);
set.add(3);
console.log(set.values());
console.log(set.keys());

// spread operator
console.log([...set]);

// maps
// Collection of key Value pait
// keys can be of any 
// maintaines the insertion order

const myMap = new Map();

// set method --> updates or adds a key value pair

myMap.set('name', 'John');
myMap.set('age', '25');
console.log(myMap);

// get(key)
// Retrieves the value associated with the specified key
console.log(myMap.get('name'));

// has --> to check if a particular key exists or not
console.log(myMap.has('name'));

// clear and size

//Iteration Methods
console.log(myMap.keys());

//1. keys
console.log([...myMap.keys()]);

//2. Values
console.log([...myMap.values()]);

//3. entries() --> key and value pair
console.log([...myMap.entries()]);

// Remove Duplicates from Array

function removeDuplicate(array) {
    return [...new Set(array)];
}

const numbers = [1, 2, 3, 4, 4, 5, 2];
console.log(removeDuplicate(numbers));


// An array of objects, filter out the objects with duplicate properties
const array4 = [{id:1, name:"Anna"}, {id:2, name:"John"}, {id:2, name:"John"}];
function filterDuplicates(arr) {
    const seen = new Set();
    return arr.filter(obj =>
        {
            const ele = JSON.stringify(obj);
            if(seen.has(ele)) {
                return false;
            } else {
                seen.add(ele);
                return true;
            }
        }
    )
}
console.log(filterDuplicates(array4));