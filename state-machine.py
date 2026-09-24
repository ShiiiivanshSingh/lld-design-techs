from enum import Enum, auto

class State(Enum):
    IDLE = auto() 
    RUNNING  = auto()
    PAUSED = auto()
    STOPPED = auto()

TRANSITIONS = {
    (State.IDLE, "start") : State.RUNNING,
    (State.RUNNING, "pause") : State.PAUSED,
    (State.PAUSED, "resume") : State.RUNNING,
    (State.RUNNING, "stop") : State.STOPPED,
    (State.PAUSED, "stop") : State.STOPPED,
}

class StateMachine:
    def __init__(self):
        self.state = State.IDLE
    def fire(self, event: str) -> State:
        key = (self.state ,event)
        if key not in TRANSITIONS:
            raise ValueError(f"Invalid event '{event}' in state {self.state.name}")
        self.state = TRANSITIONS[key]
        return self.state
    def can_fire(self, event: str) -> bool:
        return (self.state, event) in TRANSITIONS
    
if __name__ == "__main__":
    sm = StateMachine()
    for event in ["start", "pause", "resume", "stop", "start"]:
        try:
            print(f"{event:>7} -> {sm.fire(event).name}")
        except ValueError as e:
            print(f"  error: {e}")