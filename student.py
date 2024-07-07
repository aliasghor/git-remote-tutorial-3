import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.digits,k=8))

@dataclass
class Student:
    name: str
    age: int
    student_id: str=field(default_factory=generate_id)

    def greet(self,students_name: object) -> None:
        """Greet another student's name."""
        print(f"{self.name} greets {students_name.name}")
