from sqlite3 import Row
from typing import NamedTuple
import time


class Copilots(NamedTuple):
    id: str
    user: str
    title: str
    animation1: str
    animation2: str
    animation3: str
    animation1threshold: int
    animation2threshold: int
    animation3threshold: int
    animation1webhook: str
    animation2webhook: str
    animation3webhook: str
    lnurl_title: str
    show_message: int
    show_ack: int
    amount_made: int
    timestamp: int
    fullscreen_cam: int
    iframe_url: str

    @classmethod
    def from_row(cls, row: Row) -> "Copilots":
        return cls(**dict(row))