func solution(_ arr:[Int]) -> Double {
    return Double(arr.reduce(0, +))/Double(arr.count)
}

print(solution([1,2,3,4]))