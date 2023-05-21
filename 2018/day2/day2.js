const fs = require("fs");
const path = require("path");

const rawInput = fs.readFileSync(path.resolve(__dirname,"input.txt"),"utf8");
const parsedInput = rawInput
    .split("\n")
    .map(i => i.replace("\r",""));

// part one
let two = 0;
let three = 0;
for (let id of parsedInput) {
    let uniqueChars = new Set(id);
    let twoID = false;
    let threeID = false;
    for (let char of uniqueChars) {
        const regex = new RegExp(char, "g");
        const count = id.match(regex).length;
        if (count === 2 && twoID === false) {
            twoID = true;
            two++;
        }
        if (count === 3 && threeID === false) {
            threeID = true;
            three++;
        }
    }
}
console.log(`Part One Answer: ${two * three}`);

// part two
for (let i = 0; i < parsedInput.length; i++) {
    let idA = parsedInput[i];
    for (let j = i + 1; j < parsedInput.length; j++) {
        let idB = parsedInput[j];
        let missCount = 0;
        let commonChars = [];
        for (let q = 0; q < idA.length; q++) {
            if (idA[q] !== idB[q]) {
                missCount++;
            }
            if (idA[q] === idB[q]) {
                commonChars.push(idA[q]);
            }
            if (missCount > 1) {
                break;
            }
        }
        if (missCount === 1) {
            console.log(`Part Two Answer: ${commonChars.join("")}`);
            return;
        }
    }
}