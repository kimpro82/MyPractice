// Big Block Lettering
// 2023.05.28


import * as fs from 'fs';
import * as yaml from 'js-yaml';
import * as readline from 'readline';


// 입력을 받을 readline.Interface 생성
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// 알파벳 문자열 입력 받기
rl.question('알파벳 문자열을 입력하세요: ', (input: string) => {
    rl.close();

    // 입력받은 알파벳 문자를 대문자로 변환
    const upperCaseInput = input.toUpperCase();

    // alphabet.yml 파일 불러오기
    const alphabetData = yaml.load(fs.readFileSync('alphabet.yml', 'utf8'));    // not .safeLoad()

    // 출력용 배열 초기화
    const outputArray: string[] = [];

    // 알파벳 문자열을 출력용 배열에 누적하는 함수
    function accumulateAlphabetString(alphabet: string) {
        const alphabetDataString = alphabetData[alphabet];
        for (let i = 0; i < alphabetDataString.length; i++) {
            const char = alphabetDataString[i];
            if (outputArray[i]) {
                outputArray[i] += char;
            } else {
                outputArray[i] = char;
            }
        }
    }

    // 입력받은 알파벳 문자열을 출력용 배열에 누적
    for (let i = 0; i < upperCaseInput.length; i++) {
        const char = upperCaseInput[i];
        if (alphabetData.hasOwnProperty(char)) {
            accumulateAlphabetString(char);
        }
    }

    // 출력용 배열 출력
    if (outputArray.length > 0) {
        for (let i = 0; i < outputArray.length; i++) {
            console.log(outputArray[i]);
        }
    } else {
        console.log('입력한 알파벳 문자열에 해당하는 데이터가 없습니다.');
    }
});
