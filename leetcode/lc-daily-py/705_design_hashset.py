# https://leetcode.com/problems/design-hashset/
# 705. Design HashSet


class MyHashSet:
    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        self.data.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.data


testcases = [
    (
        [
            "MyHashSet",
            "add",
            "add",
            "contains",
            "contains",
            "add",
            "contains",
            "remove",
            "contains",
            "remove",  # delete non-existent item
        ],
        [[], [1], [2], [1], [3], [2], [2], [2], [2], [19]],
        [[], None, None, True, False, None, True, None, False, None],
    ),
]
for exts, data, expected in testcases:
    hm = MyHashSet()
    for inst, vals, exp in zip(exts, data, expected):
        if not vals:
            continue
        val = vals[0]
        assert getattr(hm, inst)(val) == exp
