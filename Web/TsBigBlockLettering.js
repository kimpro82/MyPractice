"use strict";
// Big Block Lettering
// 2023.05.28
exports.__esModule = true;
var fs = require("fs");
var yaml = require("js-yaml");
var readline = require("readline");
// 입력을 받을 readline.Interface 생성
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// 알파벳 문자열 입력 받기
rl.question('알파벳 문자열을 입력하세요: ', function (input) {
    rl.close();
    // 입력받은 알파벳 문자를 대문자로 변환
    var upperCaseInput = input.toUpperCase();
    // alphabet.yml 파일 불러오기
    var alphabetData = yaml.load(fs.readFileSync('alphabet.yml', 'utf8')); // not .safeLoad()
    // 출력용 배열 초기화
    var outputArray = [];
    // 알파벳 문자열 출력 함수
    function printAlphabetString(alphabet) {
        var alphabetDataString = alphabetData[alphabet];
        for (var i = 0; i < alphabetDataString.length; i++) {
            var char = alphabetDataString[i];
            if (outputArray[i]) {
                outputArray[i] += char;
            }
            else {
                outputArray[i] = char;
            }
        }
    }
    // 입력받은 알파벳 문자열 출력
    for (var i = 0; i < upperCaseInput.length; i++) {
        var char = upperCaseInput[i];
        if (alphabetData.hasOwnProperty(char)) {
            printAlphabetString(char);
        }
    }
    // 출력용 배열 출력
    for (var i = 0; i < outputArray.length; i++) {
        console.log(outputArray[i]);
    }
});
