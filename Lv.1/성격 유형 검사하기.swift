import Foundation
var dict: [Character : Int] = ["R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0]

func choiceToValue(choice: Int) -> Int {
    switch choice {
    case 1, 7:
        return 3
    case 2, 6:
        return 2
    case 3, 5:
        return 1
    default:
        return 0
    }
}

func printDict() -> String{
    var result: String = ""
    result += dict["T"]! > dict["R"]! ? "T" : "R"
    result += dict["F"]! > dict["C"]! ? "F" : "C"
    result += dict["M"]! > dict["J"]! ? "M" : "J"
    result += dict["N"]! > dict["A"]! ? "N" : "A"

    return result
}

func solution(_ survey:[String], _ choices:[Int]) -> String {
    for i in 0..<survey.count{
        let charArr = Array(survey[i])
        let characteristic = choices[i]>4 ? charArr[1] : charArr[0]
        let score: Int = dict[characteristic]! + choiceToValue(choice: choices[i])

        dict.updateValue(score, forKey: characteristic)
    }
    return printDict()
}

print(solution(["TR", "RT", "TR"], [7, 1, 3]))