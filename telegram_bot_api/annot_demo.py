from dataclasses import dataclass, field

@dataclass
class Person:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"
    full_name: str = field(init=False, repr=False)
    def __post_init__(self):
        self.full_name = self.first_name + " " + self.last_name






ahmed = Person()
print(ahmed)
print(ahmed.full_name)
