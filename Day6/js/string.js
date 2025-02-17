const str = "Hello World";
console.log(str.charAt(0));
console.log(str.charCodeAt(2));

const str2 = "World";
// concat
console.log(str.concat(',', str2));
// includes
console.log(str.includes("world")); // Case sensitive!!  false
// endsWith
console.log(str.endsWith("World"));
console.log(str.endsWith("Hello", 5));
// indexOf
console.log(str.indexOf("w")); // Case sensitive!!  -1
console.log(str.indexOf("l"));
// lastIndexOf
console.log(str.lastIndexOf("l"));
// padStart
console.log(str.padStart(20, "*#"));
// repeat (count)
console.log(str.repeat(3));
// replace (oldvalue, newvalue)
console.log(str.replace("l", "0"));
// replaceAll (oldvalue, newvalue)
console.log(str.replaceAll("l", "0"));
// slice (start, end)
console.log(str.slice(0, 5));
// split (separator, limit)
console.log(str.split(" ", "5"));
console.log(str.split(""));
// toLowerCase
console.log(str.toLowerCase());
// trim
console.log(str.trim());
// trimStart
console.log(str.trimStart());
// trimEnd
console.log(str.trimEnd());
// length
console.log(str.length);