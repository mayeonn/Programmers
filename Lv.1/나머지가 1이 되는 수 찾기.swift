import Foundation

func solution(_ n:Int) -> Int {
    var x = 1
    while(x<n) {
        if n%x == 1{
            break
        }
        x+=1
    }
    return x
}

print(solution(12))