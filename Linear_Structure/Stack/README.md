# 🧱 Stack (Python Implementation)

> 🎯 **Educational Purpose Only**  
> Python에서 직접 **Stack (스택)** 자료구조를 구현하여  
> **LIFO (Last-In, First-Out)** 원리를 이해하기 위한 프로젝트입니다.  
> 실제 프로덕션에서는 `list` 또는 `collections.deque` 사용을 권장합니다.  

이 리포지토리는 Python에서 Stack 자료구조를 구현한 예제입니다. Array(리스트) 기반과 Linked List 기반 구현을 포함합니다.

## Stack 개요
Stack은 LIFO(Last In, First Out) 원칙을 따르는 자료구조입니다. 주요 연산은 top 요소에 집중되어 효율적입니다.

### 🛠️ 구현 메서드
- `push(item)` : 스택 top에 요소 추가  
- `pop()` : top의 요소 제거 및 반환  
- `peek()` : top 요소 확인 (삭제 X)  
- `is_empty()` : 스택이 비었는지 확인  
- `size()` : 스택의 현재 크기 반환  

## 주요 메소드와 시간 복잡도
아래 테이블은 Stack의 표준 메소드와 일반적인 시간 복잡도를 요약합니다. (Array 구현은 amortized O(1), Linked List 구현은 O(1)입니다.)

| 메소드     | 설명                                      | 시간 복잡도 (Array) | 시간 복잡도 (Linked List) |
|------------|-------------------------------------------|---------------------|---------------------------|
| push      | 요소를 top에 추가                         | O(1)               | O(1)                     |
| pop       | top 요소를 제거하고 반환                  | O(1)               | O(1)                     |
| peek/top  | top 요소를 확인 (제거하지 않음)           | O(1)               | O(1)                     |
| is_empty  | 스택이 비어 있는지 확인                   | O(1)               | O(1)                     |
| size      | 요소 개수 반환                            | O(1)               | O(1)                     |

- **주의**: Array 구현에서 pop/push는 리스트 크기 재할당 시 O(n)이 될 수 있지만, amortized O(1)입니다. Linked List는 메모리 오버헤드가 더 큽니다.

## Python에서 Stack 활용 가능한 라이브러리
Python 내장 라이브러리를 활용해 Stack을 쉽게 사용할 수 있습니다. 직접 구현할 필요 없이 아래 모듈을 추천합니다:

- **collections.deque**:
  - Stack으로 사용: `append()` (push), `pop()` (pop).
  - 장점: O(1) 시간 복잡도, thread-safe 하지 않음 (단순 사용에 적합).
  - 예제: `from collections import deque; stack = deque(); stack.append(1); print(stack.pop())`.

- **queue.LifoQueue**:
  - Stack으로 사용: `put()` (push), `get()` (pop).
  - 장점: thread-safe, 멀티스레딩 환경에 적합.
  - 예제: `from queue import LifoQueue; stack = LifoQueue(); stack.put(1); print(stack.get())`.

- **list (내장 리스트)**:
  - Stack으로 사용: `append()` (push), `pop()` (pop).
  - 장점: 가장 간단, 하지만 대규모 사용 시 deque가 더 효율적.
  - 예제: `stack = []; stack.append(1); print(stack.pop())`.

이 라이브러리들은 Stack의 기본 기능을 제공하며, 특정 요구사항에 따라 선택하세요.

## 구현 예제 파일
- `array_stack.py`: Array 기반 Stack 클래스.
- `linkedlist_stack.py`: Linked List 기반 Stack 클래스.