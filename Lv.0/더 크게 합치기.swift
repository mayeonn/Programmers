import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let x = max(Int(String("\(a)\(b)"))!, Int(String("\(b)\(a)"))!)
    return x
}