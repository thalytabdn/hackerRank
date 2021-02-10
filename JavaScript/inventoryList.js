'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function() {
  inputString = inputString.split('\n');

  main();
});

function readLine() {
    return inputString[currentLine++];
}
function inventoryList() {
  // write your code here
    items: {},
    add: function(name){
        this.items[name] = name;
    },
    remove: function(name){
        this.items[name] = null;
    },
    getList: function(){
        return this.items;
    }
    
};

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    
    const obj = inventoryList();
    const operationCount = parseInt(readLine().trim());
    
    for(let i = 1; i <= operationCount; i++) {
        const operationInfo = readLine().trim().split(' ');
        if (operationInfo[0] === 'add') {
            obj.add(operationInfo[1]);
        } else if (operationInfo[0] === 'remove') {
            obj.remove(operationInfo[1]);
        } else if (operationInfo[0] === 'getList') {
            const res = obj.getList();
            if (res.length === 0) {
                ws.write('No Items\n');
            } else {
                ws.write(`${res.join(',')}\n`);
            }
        }
    }
    ws.end();
}