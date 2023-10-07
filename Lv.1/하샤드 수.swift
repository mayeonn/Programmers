func solution(_ x:Int) -> Bool {
    let arr = "\(x)".compactMap{$0.hexDigitValue}
    return x % arr.reduce(0){$0+$1} == 0
}

print(solution(10))