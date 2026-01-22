"""
Тестове за Strategy Pattern имплементацията
"""

import unittest
import sys
import os

# Добавяне на родителската директория към пътя
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategy_pattern import (
    Sorter,
    BubbleSortStrategy,
    QuickSortStrategy,
    MergeSortStrategy
)


class TestStrategyPattern(unittest.TestCase):
    """Тестове за Strategy Pattern"""
    
    def setUp(self):
        """Подготовка на тестови данни"""
        self.test_data = [64, 34, 25, 12, 22, 11, 90, 5]
        self.expected_sorted = [5, 11, 12, 22, 25, 34, 64, 90]
    
    def test_bubble_sort_strategy(self):
        """Тест за Bubble Sort стратегия"""
        sorter = Sorter(BubbleSortStrategy())
        result = sorter.sort_data(self.test_data)
        self.assertEqual(result, self.expected_sorted)
        self.assertEqual(sorter.get_strategy_name(), "Bubble Sort")
    
    def test_quick_sort_strategy(self):
        """Тест за Quick Sort стратегия"""
        sorter = Sorter(QuickSortStrategy())
        result = sorter.sort_data(self.test_data)
        self.assertEqual(result, self.expected_sorted)
        self.assertEqual(sorter.get_strategy_name(), "Quick Sort")
    
    def test_merge_sort_strategy(self):
        """Тест за Merge Sort стратегия"""
        sorter = Sorter(MergeSortStrategy())
        result = sorter.sort_data(self.test_data)
        self.assertEqual(result, self.expected_sorted)
        self.assertEqual(sorter.get_strategy_name(), "Merge Sort")
    
    def test_strategy_switching(self):
        """Тест за смяна на стратегия по време на изпълнение"""
        sorter = Sorter(BubbleSortStrategy())
        self.assertEqual(sorter.get_strategy_name(), "Bubble Sort")
        
        sorter.set_strategy(QuickSortStrategy())
        self.assertEqual(sorter.get_strategy_name(), "Quick Sort")
        
        result = sorter.sort_data(self.test_data)
        self.assertEqual(result, self.expected_sorted)
    
    def test_empty_list(self):
        """Тест с празен списък"""
        sorter = Sorter(BubbleSortStrategy())
        result = sorter.sort_data([])
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Тест с един елемент"""
        sorter = Sorter(QuickSortStrategy())
        result = sorter.sort_data([42])
        self.assertEqual(result, [42])
    
    def test_already_sorted(self):
        """Тест с вече сортиран списък"""
        sorted_data = [1, 2, 3, 4, 5]
        sorter = Sorter(MergeSortStrategy())
        result = sorter.sort_data(sorted_data)
        self.assertEqual(result, sorted_data)
    
    def test_negative_numbers(self):
        """Тест с отрицателни числа"""
        test_data = [-5, -1, -3, 0, 2, -2]
        expected = [-5, -3, -2, -1, 0, 2]
        sorter = Sorter(QuickSortStrategy())
        result = sorter.sort_data(test_data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
