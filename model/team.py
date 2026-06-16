from dataclasses import dataclass
@dataclass
class Team:
    id: int
    team_code: str
    name: str
    tot_salari : float

    def __hash__(self):
        return hash(self.id)