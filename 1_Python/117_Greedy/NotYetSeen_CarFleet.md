这个的核心思想
```python
def carFleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)  # 按位置从大到小排序
    times = [(target - pos) / spd for pos, spd in cars]  # 计算每辆车到达终点的时间

    fleets = 0
    last_time = 0  # 前一个车队的到达时间

    for time in times:
        if time > last_time:  # 当前车形成新的车队
            fleets += 1
            last_time = time  # 更新车队的到达时间

    return fleets
```