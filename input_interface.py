from typing import Any


class InputInterface:
    def read_input(self, msg: str, cast: Any) -> Any:
        return cast(input(msg))