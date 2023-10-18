from dataclasses import dataclass, asdict


@dataclass
class RequestStoreModel:
    id: int
    petId: int
    quantity: int
    shipDate: float
    status: str
    complete: str

    def to_dict(self):
        return asdict(self)