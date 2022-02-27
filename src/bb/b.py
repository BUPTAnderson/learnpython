from src.aa.a import Producer
print("========")


class Consumer:
    def __init__(self) -> None:
        self._p = Producer()
        print(self._p.get_name())

    def get_name(self):
        return "bb"
