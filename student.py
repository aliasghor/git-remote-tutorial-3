from dataclasses import dataclass
import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.digits,k=8))

@dataclass
class Student:
    def greet(self,students_name: object) -> None:
        """Greet another student's name."""
        print(f"{self.name} greets {students_name.name}")