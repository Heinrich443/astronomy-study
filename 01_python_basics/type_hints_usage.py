from typing import List, Dict, Union, Optional

def process_student(students: List[Dict[str, Union[str, int]]]) -> Optional[float]:
    """
    处理学生数据，计算平均分数

    参数:
        students: 学生列表，每个学生是包含'name'和'score'的字典

    返回:
        平均分数（浮点数），如果没有学生则返回None
    """
    if not students:
        return None

    sum = 0.0
    for student in students:
        sum += student["score"]
    return sum * 1.0 / len(students)

# 测试数据
students = [
    {"name": "Alice", "score": 89},
    {"name": "Ben", "score": 86},
    {"name": "Charles", "score": 78}
]

average = process_student(students)
print(f"average: {average:.2f}")