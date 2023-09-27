import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    let idx1 = my_string.index(my_string.startIndex, offsetBy: s)
    let idx2 = my_string.index(my_string.startIndex, offsetBy: s+overwrite_string.count)
    
    var str = my_string
    str.removeSubrange(idx1..<idx2)
    str.insert(contentsOf: overwrite_string, at: idx1)
    
    return str
}