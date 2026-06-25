from dataclasses import dataclass

@dataclass
class PipelineResult:

    success: bool

    steps: list

    duration: float
