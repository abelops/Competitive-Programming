from typing import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter_list = sorted(Counter(tasks).values(), reverse = True)
        print(counter_list)
        num_intervals = counter_list[0] - 1
        num_idles = num_intervals * n
        for n_task in counter_list[1:]:
            num_idles -= min(num_intervals, n_task)
        return len(tasks) + max(0, num_idles)