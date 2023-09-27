import Foundation

func solution(_ n:Int) -> Int {
    if n.isMultiple(of: 2){
        return stride(from: 2, through: n, by: 2).reduce(0){$0 + $1*$1}
    }
    else{
        return stride(from: 1, through: n, by: 2).reduce(0, +)
    }
}
