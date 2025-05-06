from dataclasses import dataclass

from model.Oggettini import Oggettini


@dataclass
class Arco:
    o1: Oggettini
    o2: Oggettini
    peso: int
