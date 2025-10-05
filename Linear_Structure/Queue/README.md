## Queue 개요
Queue는 FIFO(First In, First Out) 원칙을 따르는 자료구조입니다. 주요 연산은 front(앞)과 rear(뒤)에서 수행됩니다.

## Queue 주요 메소드와 시간 복잡도
아래 테이블은 Queue의 표준 메소드와 일반적인 시간 복잡도를 요약합니다. (Array 구현은 enqueue O(1), dequeue O(n); Linked List 구현은 O(1)입니다.)

| 메소드     | 설명                                      | 시간 복잡도 (Array) | 시간 복잡도 (Linked List) |
|------------|-------------------------------------------|---------------------|---------------------------|
| enqueue   | 요소를 rear에 추가                        | O(1)               | O(1)                     |
| dequeue   | front 요소를 제거하고 반환                | O(n)               | O(1)                     |
| peek/front| front 요소를 확인 (제거하지 않음)         | O(1)               | O(1)                     |
| is_empty  | 큐가 비어 있는지 확인                     | O(1)               | O(1)                     |
| size      | 요소 개수 반환                            | O(1)               | O(1)                     |

- **주의**: Array 구현에서 dequeue는 리스트의 shift 연산으로 O(n)이 발생하므로, 대규모 데이터에는 비효율적입니다. 실제 사용 시 `collections.deque`를 추천합니다. Linked List는 메모리 오버헤드가 더 큽니다.

## Python에서 Queue 활용 가능한 라이브러리
Python 내장 라이브러리를 활용해 Queue를 쉽게 사용할 수 있습니다. 직접 구현할 필요 없이 아래 모듈을 추천합니다:

- **collections.deque**:
  - Queue로 사용: `append()` (enqueue), `popleft()` (dequeue).
  - 장점: O(1) 시간 복잡도, thread-safe 하지 않음 (단순 사용에 적합).
  - 예제: `from collections import deque; queue = deque(); queue.append(1); print(queue.popleft())`.

- **queue.Queue**:
  - Queue로 사용: `put()` (enqueue), `get()` (dequeue).
  - 장점: thread-safe, 멀티스레딩 환경에 적합.
  - 예제: `from queue import Queue; queue = Queue(); queue.put(1); print(queue.get())`.

- **list (내장 리스트)**:
  - Queue로 사용: `append()` (enqueue), `pop(0)` (dequeue).
  - 장점: 가장 간단, 하지만 dequeue가 O(n)이므로 대규모 사용 시 deque가 더 효율적.
  - 예제: `queue = []; queue.append(1); print(queue.pop(0))`.

이 라이브러리들은 Queue의 기본 기능을 제공하며, 특정 요구사항에 따라 선택하세요.

## 구현 예제 파일
- `queue_array.py`: Array 기반 Queue 클래스.
- `queue_linkedlist.py`: Linked List 기반 Queue 클래스.