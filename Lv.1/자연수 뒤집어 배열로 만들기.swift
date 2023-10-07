func solution(_ n:Int64) -> [Int] {
    // shorter code
    // compactMap -> 1D array에서 nil 제거 & Optional 바인딩
    return "\(n)".compactMap{$0.hexDigitValue}.reversed()
}
