# 🔗 Singly & Doubly Linked List (Python Implementation)

> 🎯 **Educational Purpose Only**  
> Python에서 직접 **단일 연결 리스트(Singly Linked List)** 와 **이중 연결 리스트(Doubly Linked List)** 를 구현해보며 **포인터 기반 자료구조의 동작 원리**를 이해하기 위한 프로젝트입니다.  
> 실제 프로덕션에서는 `collections.deque`, `list` 등을 사용하는 것이 훨씬 효율적입니다.  

---

## 🔹 Singly Linked List

### ✨ 특징
- 각 노드가 **값(value)** + **next 포인터** 보유  
- **앞/뒤 순차 탐색**만 가능 (역방향 불가)  
- 특정 노드 기준 **삽입/삭제 O(1)**, 임의 접근은 **O(n)**  

### 🛠️ 구현 메서드
- `append(value)` : 끝에 추가  
- `prepend(value)` : 맨 앞에 추가  
- `find(value)` : 값 탐색 (O(n))  
- `remove(value)` : 값 삭제 (O(n))  
- `__iter__()` : 리스트 순회  

### ⏱️ 시간 복잡도
| 연산         | 시간 |
|--------------|------|
| append       | O(1) (tail 유지 시) |
| prepend      | O(1) |
| find/remove  | O(n) |
| 접근(index)  | O(n) |

---

## 🔹 Doubly Linked List

### ✨ 특징
- 각 노드가 **값(value)** + **prev/next 포인터** 보유  
- **양방향 탐색 가능** → 특정 노드 삭제 완전 O(1)  
- 메모리 사용량 ↑ (포인터 2개 저장)  

### 🛠️ 구현 메서드
- `append(value)` : 끝에 추가  
- `remove_node(node)` : 특정 노드 삭제 (O(1))  

### ⏱️ 시간 복잡도
| 연산         | 시간 |
|--------------|------|
| append       | O(1) |
| remove_node  | O(1) (노드 참조 알고 있을 때) |
| 탐색         | O(n) |

---

## 🆚 비교

| 자료구조              | 접근 | 삽입/삭제 | 탐색 | 메모리 |
|------------------------|------|-----------|------|--------|
| **Singly Linked List** | O(n) | O(1) (head/tail) | O(n) | 노드+next |
| **Doubly Linked List** | O(n) | O(1) (노드 참조시) | O(n) | 노드+prev+next |
| **Python list**        | O(1) | O(n) (중간) | O(n) | 연속 배열 |
| **deque**              | O(1) | O(1) 양끝 | O(n) | 양쪽 빠른 큐 |

---
