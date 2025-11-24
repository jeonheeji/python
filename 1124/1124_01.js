// JavaSript
// 웹페이지에 동적 기능을 추가하는 프로그래밍 언어

// let 재할당가능
let name="홍길동";
console.log(name);

// const 재할당 불가
const age = 25;
console.log(age);

// 구형 사용지양
var oldStyle='Es5  이전';

// 변수이름규칙 불가능
//const 1name='홍';
//const user-name='홍';
//const let = '홍';

// 데이터타입
// 숫자 (Number)
const age1 =25;
const price=19.99;
const negative=-16;

console.log(typeof age); // 데이터타입 볼 수 있음

// 문자열 (String)
const name1="홍길동";
const name2="김철수";
const name3='이영희';

console.log(typeof name3)

// 불리언(Boolean)
const isStudent1=true;
const isTeacher=false;

console.log(typeof isTeacher)

//null과 undefined
let empty=null; //의도적으로 널값 집어넣음
let notDefined; // 값이 할당되지않음

console.log(empty)
console.log(notDefined)

console.log(`제 이름은 ${name}, 나이는 ${age}입니다`);

const name4="홍길동";
const age4="25";
const isStudent=true;

console.log(`이름 : ${name4}`)
console.log(`나이 : ${age4}살`)
console.log(`학생 : ${isStudent}`)
console.log(`자기소개 :안녕하세요, 저는 ${age4}살 ${name4}입니다`)

// 삼항 연산자
// 조건 ? 참일떄 값 : 거짓일때값
let age2=20;
let result=age2>=18?"성인":"미성년자";
console.log(result);

function celsiusToFahrenheit(selsius){
    return selsius*9/5+32;
    
}
console.log(celsiusToFahrenheit(0));
console.log(celsiusToFahrenheit(100));

function average(numbers){
    let sum = 0;
    for (let n of numbers){
        sum+=n;
    }
return sum/numbers.length;
}

console.log(average([10,20,30]));