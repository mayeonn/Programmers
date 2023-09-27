import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
        let x = max(2*a*b, Int(String("\(a)\(b)"))!)
    return x
}