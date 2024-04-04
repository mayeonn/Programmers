struct Queue<T> {
    private var queue: [T] = []
    private var front: Int = 0

    public var size: Int {
        return queue.count
    }

    public var isEmpty: Bool {
        return queue.isEmpty
    }

    public mutating func enqueue(_ element: T) {
        queue.append(element)
    }

    public mutating func dequeue() -> T? {
        // removeFirst: 맨 앞에 원소를 빼면 모든 원소를 앞으로 당겨야 함 -> 시간 복잡도 O(n)
        // return isEmpty ? nil : queue.removeFirst()

        guard let element = queue[front], front <= size else {
            return nil
        }
        queue[front] = nil
        front += 1
        return element
    }
}

// priorities: 프로세스의 중요도가 순서대로 담긴 배열:
//              1이상 100이하 길이, 원소는 1 이상 9 이하의 정수(클 수록 높은 우선순위)
// location: 몇 번째로 실행되는지 알고 싶은 프로세스의 위치(0부터 시작)
def solution(priorities, location):
    answer = 0

    queue = Queue<Int>()



    return answer
