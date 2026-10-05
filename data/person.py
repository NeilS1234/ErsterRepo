from dataclasses import dataclass, fields


@dataclass
class Person:
    name: str
    age: int
    job: str
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            age=data.get("age"),
            job=data.get("job")
        )

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "job": self.job
        }

    @staticmethod 
    def fieldnames():
        return [field.name for field in fields(Person)]
    



       
p1 = Person("Hana", 18, "Studentin")
print(p1) 




