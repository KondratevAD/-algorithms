# https://contest.yandex.ru/contest/24735/run-report/52298905/
def broken_search(nums: list, target: int) -> int:
    """Поиск индекса элемента в списке.

    Ключевые аргументы:
    arr -- список для поиска.
    target -- элемент для поиска.
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)//2
        item = nums[mid]
        if item == target:
            return mid
        if (
            nums[left] > item and target < item or
            target >= nums[left] and target < item
        ):
            right = mid - 1
        else:
            left = mid + 1
    return -1
