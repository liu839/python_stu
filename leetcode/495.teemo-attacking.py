def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    time = len(timeSeries) * duration
    try:
        for index in range(len(timeSeries)):
            if timeSeries[index] + duration > timeSeries[index + 1]:
                time -= duration-(timeSeries[index + 1] - timeSeries[index])
    except IndexError:
        pass
    return time