# 📚 Fixed Array & Dynamic Array (Python Implementation)

> 🎯 **Educational Purpose Only**  
> Python의 `list`와 `array.array`를 직접 구현해보며 **배열의 원리와 시간/공간 복잡도**를 이해하기 위한 프로젝트입니다.  
> 실제 프로덕션에서는 내장 자료구조(`list`, `array`, `deque`) 사용을 권장합니다.  

---

## 🔹 Fixed Array

### ✨ 특징
- **고정 크기 배열**: 초기 크기 지정 후 변경 불가
- 미사용 슬롯도 메모리를 차지
- `Python list`와 다르게 **동적 확장 불가**
- `array.array`와 유사 (단, 타입 제한 없음)

### 🛠️ 구현 메서드
- `__init__(size)` : 고정 크기 초기화  
- `get(index)` : 값 반환 (O(1))  
- `set(index, value)` : 값 설정 (O(1))  
- `length()` : 배열 크기 반환 (O(1))  

### ⏱️ 시간 복잡도
| 연산       | 시간 |
|------------|------|
| init       | O(n) |
| get/set    | O(1) |
| length     | O(1) |

---

## 🔹 Dynamic Array

### ✨ 특징
- **동적 크기 배열**: 요소 추가 시 자동 확장  
- 공간이 1/4 이하로 줄면 자동 축소  
- Python `list`와 매우 유사 (Amortized O(1) append)

### 🛠️ 구현 메서드
- `__init__(initial_capacity=10)` : 초기 용량  
- `get(index)` / `set(index, value)` : 값 접근/설정 O(1)  
- `append(value)` : 끝에 추가 (Amortized O(1))  
- `pop()` : 마지막 제거 (Amortized O(1))  
- `length()` : 현재 길이  
- `_resize(new_capacity)` : 내부 크기 조정 (O(n))  

### ⏱️ 시간 복잡도
| 연산     | 평균 시간 | 최악의 경우 |
|----------|-----------|-------------|
| append   | O(1)      | O(n) (확장 시) |
| pop      | O(1)      | O(n) (축소 시) |
| get/set  | O(1)      | O(1) |
| resize   | -         | O(n) |

---

## 🆚 Python 내장과 비교

| 구조체           | 특징 |
|------------------|------|
| **FixedArray**   | 고정 크기, 메모리 낭비 줄임. `array.array`와 유사 |
| **DynamicArray** | `list`와 유사. Amortized O(1) append/pop |
| **Python list**  | 내부적으로 Dynamic Array 구현 (C로 최적화, 더 빠름) |
| **array.array**  | 고정 크기 & 타입 제한 (메모리 효율 ↑) |

---

## 🚀 실행 예제
```python
from fixed_array import FixedArray
from dynamic_array import DynamicArray

# Fixed Array
fa = FixedArray(5)
fa.set(0, 10)
print(fa.get(0))      # 10
print(fa.length())    # 5

# Dynamic Array
da = DynamicArray()
da.append(1)
da.append(2)
print(da.get(1))      # 2
print(da.length())    # 2
da.pop()
