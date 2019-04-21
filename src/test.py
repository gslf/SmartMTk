import time
from SmartMTk import SmartMTk

if __name__ == "__main__":
    mtk = SmartMTk()
    
    print("SmartMTk test routine")
    print("> Forward")
    mtk.forward()
    time.sleep(5)
    mtk.shortBrake()

    print("> Backward")
    mtk.backward()
    time.sleep(5)
    mtk.shortBrake()

    print("> Left")
    mtk.turnLeft()
    time.sleep(5)
    mtk.straight()

    print("> Right")
    mtk.turnRight()
    time.sleep(5)
    mtk.straight()


