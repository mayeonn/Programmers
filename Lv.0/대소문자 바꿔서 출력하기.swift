import Foundation

let s1 = readLine()!
var result:String = ""

for x in s1{
    if x.isUppercase{
        result.append(x.lowercased())
    }
    else{
        result.append(x.uppercased())
    }
}

print(result)