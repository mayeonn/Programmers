func solution(_ n:Int64) -> [Int] {
    var arr = Array(String(n))
    arr.reverse()
    let result = arr.map{$0.hexDigitValue!}
    
    return result
}