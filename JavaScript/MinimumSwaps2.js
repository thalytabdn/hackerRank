'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the minimumSwaps function below.
function minimumSwaps(arr) {
    let swaps = 0
    for (let i = 0; i < arr.length; i++) {
        while (arr[i] !== i + 1) {
            arr[i] = [arr[arr[i]-1], arr[arr[i]-1] = arr[i]][0]
            if (!arr[i]) break
            swaps++
        }
    }

    return swaps
}

let arr = [4,3,1,2]
console.log(minimumSwaps(arr))

// function main() {
//     const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

//     const n = parseInt(readLine(), 10);

//     const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

//     const res = minimumSwaps(arr);

//     ws.write(res + '\n');

//     ws.end();
// }
