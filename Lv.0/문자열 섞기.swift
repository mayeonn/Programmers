import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var str = ""
    for i in str1.indices{
        str.append("\(str1[i])\(str2[i])")
    }
    return str
}