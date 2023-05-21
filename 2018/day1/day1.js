const fs = require("fs");
const path = require("path");

rawInput = fs.readFileSync(path.resolve(__dirname,"input.txt"),"utf8");
let parsedInput = rawInput
    .split("\n")
    .map(n => parseInt(n.replace("+","")))
    .filter(n => !isNaN(n));
    
let frequency = 0;
for (let n = 0; n < parsedInput.length; n++) {
    frequency += parsedInput[n];
}
console.log(`Part One Answer: ${frequency}`);

frequency = 0;
let count = 0;
uniqueFrequencies = [];
while(true) {
    let index = count % parsedInput.length;
    if (!uniqueFrequencies.includes(frequency)) {
        uniqueFrequencies.push(frequency);
        frequency += parsedInput[index];
        count++;
    } else {
        console.log(`Part Two Answer: ${frequency}`);
        break;
    }
}
