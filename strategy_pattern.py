"""
Strategy Pattern Implementation
Стратегически шаблон - позволява избор на алгоритъм по време на изпълнение
"""

from abc import ABC, abstractmethod
from typing import List


# Интерфейс за стратегията
class SortStrategy(ABC):
    """Абстрактен клас, дефиниращ интерфейса за различните стратегии за сортиране"""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """Сортира списъка и го връща"""
        pass


# Конкретни стратегии
class BubbleSortStrategy(SortStrategy):
    """Стратегия за сортиране с метода на мехурчето"""
    
    def sort(self, data: List[int]) -> List[int]:
        """Имплементация на Bubble Sort"""
        arr = data.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr
    
    def __str__(self):
        return "Bubble Sort"


class QuickSortStrategy(SortStrategy):
    """Стратегия за сортиране с Quick Sort алгоритъм"""
    
    def sort(self, data: List[int]) -> List[int]:
        """Имплементация на Quick Sort"""
        arr = data.copy()
        
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)
        
        return quicksort(arr)
    
    def __str__(self):
        return "Quick Sort"


class MergeSortStrategy(SortStrategy):
    """Стратегия за сортиране с Merge Sort алгоритъм"""
    
    def sort(self, data: List[int]) -> List[int]:
        """Имплементация на Merge Sort"""
        arr = data.copy()
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        return merge_sort(arr)
    
    def __str__(self):
        return "Merge Sort"


# Context клас - използва стратегията
class Sorter:
    """Контекстен клас, който използва различни стратегии за сортиране"""
    
    def __init__(self, strategy: SortStrategy):
        """
        Инициализира Sorter с конкретна стратегия
        
        Args:
            strategy: Стратегия за сортиране (BubbleSortStrategy, QuickSortStrategy, и т.н.)
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        """Променя стратегията по време на изпълнение"""
        self._strategy = strategy
    
    def sort_data(self, data: List[int]) -> List[int]:
        """
        Сортира данните, използвайки текущата стратегия
        
        Args:
            data: Списък с числа за сортиране
            
        Returns:
            Сортиран списък
        """
        return self._strategy.sort(data)
    
    def get_strategy_name(self) -> str:
        """Връща името на текущата стратегия"""
        return str(self._strategy)


# Примерна употреба
if __name__ == "__main__":
    # Тестови данни
    test_data = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Оригинални данни: {test_data}\n")
    
    # Използване на Bubble Sort стратегия
    print("=== Използване на Bubble Sort ===")
    bubble_sorter = Sorter(BubbleSortStrategy())
    sorted_bubble = bubble_sorter.sort_data(test_data)
    print(f"Стратегия: {bubble_sorter.get_strategy_name()}")
    print(f"Резултат: {sorted_bubble}\n")
    
    # Промяна на стратегията към Quick Sort
    print("=== Промяна на стратегията към Quick Sort ===")
    bubble_sorter.set_strategy(QuickSortStrategy())
    sorted_quick = bubble_sorter.sort_data(test_data)
    print(f"Стратегия: {bubble_sorter.get_strategy_name()}")
    print(f"Резултат: {sorted_quick}\n")
    
    # Използване на Merge Sort стратегия
    print("=== Използване на Merge Sort ===")
    merge_sorter = Sorter(MergeSortStrategy())
    sorted_merge = merge_sorter.sort_data(test_data)
    print(f"Стратегия: {merge_sorter.get_strategy_name()}")
    print(f"Резултат: {sorted_merge}\n")
    
    # Демонстрация на динамична смяна на стратегия
    print("=== Демонстрация на динамична смяна ===")
    sorter = Sorter(BubbleSortStrategy())
    print(f"Първоначална стратегия: {sorter.get_strategy_name()}")
    
    sorter.set_strategy(QuickSortStrategy())
    print(f"Нова стратегия: {sorter.get_strategy_name()}")
    result = sorter.sort_data([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Резултат: {result}")
