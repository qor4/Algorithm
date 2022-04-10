function gcd(num1, num2){
    while(num2){
        let temp = num1 % num2
        num1 = num2
        num2 = temp
    }
    return num1
}

function lcm(num1, num2){
    return (num1 * num2 / gcd(num1, num2))
}
function solution(arr) {
    var answer = 0;
    let num = arr[0]
    arr.sort((a, b)=> a - b)
    for(let i = 1; i < arr.length; i++){
        num = lcm(num, arr[i])
    }
    return num;
}
