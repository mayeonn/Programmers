import Foundation

func solution(_ s:String) -> Bool
{
    let S = s.uppercased()
    let P = S.components(separatedBy: "P").count - 1
    let Y = S.components(separatedBy: "Y").count - 1

    if P==Y{
        return true
    }
    return false
}