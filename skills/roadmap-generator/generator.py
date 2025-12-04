"""
Roadmap Generator

Generates structured implementation roadmaps with Epic/Story/Task breakdown,
effort estimates, and validation checkpoints.

Usage:
    from generator import RoadmapGenerator

    generator = RoadmapGenerator()
    roadmap = generator.create_roadmap(
        project_name="Notification System",
        phases=[phase1, phase2, phase3],
        team_size=5,
        start_date="2025-01-15"
    )

    print(roadmap.to_markdown())
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Dict
import json


class Size(Enum):
    """T-shirt sizing for effort estimation"""
    XS = 1  # 2-4 hours
    S = 2   # 0.5-1 day
    M = 3   # 1-2 days
    L = 5   # 3-5 days
    XL = 8  # 1-2 weeks
    XXL = 13  # > 2 weeks, should be broken down


class Priority(Enum):
    """Task priority levels"""
    CRITICAL = 1  # Blocks everything
    HIGH = 2      # Core functionality
    MEDIUM = 3    # Important but not blocking
    LOW = 4       # Nice to have


class RiskLevel(Enum):
    """Risk probability and impact levels"""
    HIGH = 3
    MEDIUM = 2
    LOW = 1


@dataclass
class Task:
    """Technical work item (2-8 hours)"""
    title: str
    size: Size
    owner: Optional[str] = None
    completed: bool = False

    def hours(self) -> float:
        """Estimated hours based on size"""
        hours_map = {
            Size.XS: 3,
            Size.S: 6,
            Size.M: 12,
            Size.L: 32,
            Size.XL: 64,
            Size.XXL: 104
        }
        return hours_map[self.size]

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "size": self.size.name,
            "hours": self.hours(),
            "owner": self.owner,
            "completed": self.completed
        }


@dataclass
class Story:
    """User-facing functionality (2-5 days)"""
    title: str
    description: str
    size: Size
    tasks: List[Task] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    owner: Optional[str] = None
    priority: Priority = Priority.MEDIUM

    def points(self) -> int:
        """Story points based on size"""
        return self.size.value

    def total_hours(self) -> float:
        """Total estimated hours from tasks"""
        if self.tasks:
            return sum(t.hours() for t in self.tasks)
        # Estimate from size if no tasks defined
        return self.size.value * 8

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "size": self.size.name,
            "points": self.points(),
            "total_hours": self.total_hours(),
            "tasks": [t.to_dict() for t in self.tasks],
            "dependencies": self.dependencies,
            "owner": self.owner,
            "priority": self.priority.name
        }


@dataclass
class Epic:
    """High-level capability (2-6 weeks)"""
    title: str
    description: str
    stories: List[Story] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    owner: Optional[str] = None

    def total_points(self) -> int:
        """Total story points"""
        return sum(s.points() for s in self.stories)

    def total_hours(self) -> float:
        """Total estimated hours"""
        return sum(s.total_hours() for s in self.stories)

    def estimated_weeks(self, team_capacity_hours_per_week: float = 30) -> float:
        """Estimated weeks based on team capacity"""
        return self.total_hours() / team_capacity_hours_per_week

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "stories": [s.to_dict() for s in self.stories],
            "dependencies": self.dependencies,
            "owner": self.owner,
            "total_points": self.total_points(),
            "total_hours": self.total_hours()
        }


@dataclass
class Risk:
    """Project risk"""
    title: str
    description: str
    probability: RiskLevel
    impact: RiskLevel
    mitigation: str
    owner: Optional[str] = None

    def score(self) -> int:
        """Risk score (probability × impact)"""
        return self.probability.value * self.impact.value

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "probability": self.probability.name,
            "impact": self.impact.name,
            "score": self.score(),
            "mitigation": self.mitigation,
            "owner": self.owner
        }


@dataclass
class ExitCriteria:
    """Phase exit gate criteria"""
    criterion: str
    met: bool = False

    def to_dict(self) -> dict:
        return {
            "criterion": self.criterion,
            "met": self.met
        }


@dataclass
class Phase:
    """Implementation phase (MVP, Scale, Advanced)"""
    name: str
    description: str
    goals: List[str]
    epics: List[Epic] = field(default_factory=list)
    exit_criteria: List[ExitCriteria] = field(default_factory=list)
    risks: List[Risk] = field(default_factory=list)
    duration_weeks: Optional[int] = None

    def total_points(self) -> int:
        """Total story points across all epics"""
        return sum(e.total_points() for e in self.epics)

    def total_hours(self) -> float:
        """Total estimated hours"""
        return sum(e.total_hours() for e in self.epics)

    def estimated_weeks(self, team_capacity_hours_per_week: float = 30) -> float:
        """Estimated weeks based on team capacity"""
        if self.duration_weeks:
            return self.duration_weeks
        return self.total_hours() / team_capacity_hours_per_week

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "goals": self.goals,
            "epics": [e.to_dict() for e in self.epics],
            "exit_criteria": [c.to_dict() for c in self.exit_criteria],
            "risks": [r.to_dict() for r in self.risks],
            "total_points": self.total_points(),
            "total_hours": self.total_hours(),
            "estimated_weeks": self.estimated_weeks()
        }


@dataclass
class TeamAllocation:
    """Team resource allocation per phase"""
    role: str
    phase1_fte: float
    phase2_fte: float
    phase3_fte: float

    def to_dict(self) -> dict:
        return {
            "role": self.role,
            "phase1_fte": self.phase1_fte,
            "phase2_fte": self.phase2_fte,
            "phase3_fte": self.phase3_fte
        }


@dataclass
class Roadmap:
    """Complete implementation roadmap"""
    project_name: str
    created_date: str
    owner: str
    summary: str
    phases: List[Phase]
    team: List[TeamAllocation] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    open_questions: List[str] = field(default_factory=list)

    def total_weeks(self) -> float:
        """Total estimated weeks across all phases"""
        return sum(p.estimated_weeks() for p in self.phases)

    def total_points(self) -> int:
        """Total story points"""
        return sum(p.total_points() for p in self.phases)

    def to_dict(self) -> dict:
        return {
            "project_name": self.project_name,
            "created_date": self.created_date,
            "owner": self.owner,
            "summary": self.summary,
            "phases": [p.to_dict() for p in self.phases],
            "team": [t.to_dict() for t in self.team],
            "assumptions": self.assumptions,
            "open_questions": self.open_questions,
            "total_weeks": self.total_weeks(),
            "total_points": self.total_points()
        }

    def to_json(self, indent: int = 2) -> str:
        """Export roadmap as JSON"""
        return json.dumps(self.to_dict(), indent=indent)

    def to_markdown(self) -> str:
        """Export roadmap as Markdown"""
        lines = [
            f"# Implementation Roadmap: {self.project_name}",
            "",
            f"**Created**: {self.created_date}",
            f"**Owner**: {self.owner}",
            f"**Total Duration**: ~{self.total_weeks():.1f} weeks",
            f"**Total Story Points**: {self.total_points()}",
            "",
            "## Executive Summary",
            "",
            self.summary,
            "",
            "---",
            ""
        ]

        # Phases
        for i, phase in enumerate(self.phases, 1):
            lines.extend([
                f"## Phase {i}: {phase.name}",
                "",
                phase.description,
                "",
                f"**Estimated Duration**: ~{phase.estimated_weeks():.1f} weeks",
                f"**Story Points**: {phase.total_points()}",
                "",
                "### Goals",
                ""
            ])

            for goal in phase.goals:
                lines.append(f"- {goal}")

            lines.extend(["", "### Epics", ""])

            for j, epic in enumerate(phase.epics, 1):
                lines.extend([
                    f"#### Epic {i}.{j}: {epic.title}",
                    "",
                    epic.description,
                    "",
                    f"**Points**: {epic.total_points()} | **Hours**: ~{epic.total_hours():.0f}",
                    ""
                ])

                if epic.stories:
                    lines.extend([
                        "| Story | Size | Points | Dependencies |",
                        "|-------|------|--------|--------------|"
                    ])
                    for story in epic.stories:
                        deps = ", ".join(story.dependencies) if story.dependencies else "None"
                        lines.append(f"| {story.title} | {story.size.name} | {story.points()} | {deps} |")
                    lines.append("")

            # Exit criteria
            if phase.exit_criteria:
                lines.extend(["### Exit Criteria", ""])
                for criteria in phase.exit_criteria:
                    status = "x" if criteria.met else " "
                    lines.append(f"- [{status}] {criteria.criterion}")
                lines.append("")

            # Risks
            if phase.risks:
                lines.extend([
                    "### Risks",
                    "",
                    "| Risk | Probability | Impact | Score | Mitigation |",
                    "|------|-------------|--------|-------|------------|"
                ])
                for risk in sorted(phase.risks, key=lambda r: r.score(), reverse=True):
                    lines.append(f"| {risk.title} | {risk.probability.name} | {risk.impact.name} | {risk.score()} | {risk.mitigation} |")
                lines.append("")

            lines.extend(["---", ""])

        # Team allocation
        if self.team:
            lines.extend([
                "## Resource Requirements",
                "",
                "| Role | Phase 1 | Phase 2 | Phase 3 |",
                "|------|---------|---------|---------|"
            ])
            for alloc in self.team:
                lines.append(f"| {alloc.role} | {alloc.phase1_fte} FTE | {alloc.phase2_fte} FTE | {alloc.phase3_fte} FTE |")
            lines.extend(["", "---", ""])

        # Assumptions
        if self.assumptions:
            lines.extend(["## Assumptions", ""])
            for assumption in self.assumptions:
                lines.append(f"- {assumption}")
            lines.extend(["", "---", ""])

        # Open questions
        if self.open_questions:
            lines.extend(["## Open Questions", ""])
            for question in self.open_questions:
                lines.append(f"- {question}")
            lines.append("")

        return "\n".join(lines)


class RoadmapGenerator:
    """Factory for creating roadmaps"""

    def __init__(self,
                 team_hours_per_week: float = 30,
                 buffer_percentage: float = 0.25):
        self.team_hours_per_week = team_hours_per_week
        self.buffer_percentage = buffer_percentage

    def create_roadmap(self,
                      project_name: str,
                      owner: str,
                      summary: str,
                      phases: List[Phase],
                      team: Optional[List[TeamAllocation]] = None,
                      assumptions: Optional[List[str]] = None,
                      open_questions: Optional[List[str]] = None) -> Roadmap:
        """Create a complete roadmap"""
        return Roadmap(
            project_name=project_name,
            created_date=datetime.now().strftime("%Y-%m-%d"),
            owner=owner,
            summary=summary,
            phases=phases,
            team=team or [],
            assumptions=assumptions or [],
            open_questions=open_questions or []
        )

    def estimate_duration(self,
                         total_points: int,
                         team_size: int,
                         velocity_per_person: float = 8) -> float:
        """Estimate duration in weeks"""
        team_velocity = team_size * velocity_per_person
        weeks = total_points / team_velocity
        # Add buffer
        return weeks * (1 + self.buffer_percentage)


# Example usage
if __name__ == "__main__":
    # Create a sample roadmap
    phase1 = Phase(
        name="MVP",
        description="Core notification functionality",
        goals=[
            "Deliver real-time push notifications",
            "Integrate with existing order system",
            "Achieve < 5 second delivery latency"
        ],
        epics=[
            Epic(
                title="Push Notification Infrastructure",
                description="Set up push notification delivery system",
                stories=[
                    Story("Implement FCM integration", "Integrate Firebase Cloud Messaging", Size.L),
                    Story("Create notification service", "Build core notification microservice", Size.XL),
                    Story("Add delivery tracking", "Track notification delivery status", Size.M)
                ]
            )
        ],
        exit_criteria=[
            ExitCriteria("Push notifications delivered to iOS and Android"),
            ExitCriteria("Delivery latency < 5 seconds at p95"),
            ExitCriteria("Integration tests passing")
        ],
        risks=[
            Risk(
                "FCM rate limits",
                "Firebase may throttle at high volume",
                RiskLevel.MEDIUM,
                RiskLevel.HIGH,
                "Implement batching and retry logic"
            )
        ]
    )

    generator = RoadmapGenerator()
    roadmap = generator.create_roadmap(
        project_name="Notification System",
        owner="Platform Team",
        summary="Implement real-time notification system to reduce support tickets by 60%",
        phases=[phase1],
        team=[
            TeamAllocation("Backend", 2, 3, 2),
            TeamAllocation("Mobile", 1, 2, 1),
            TeamAllocation("DevOps", 0.5, 1, 0.5)
        ],
        assumptions=[
            "FCM/APNs credentials available",
            "Order service can emit events"
        ],
        open_questions=[
            "What's the notification preference UI scope?",
            "Do we need SMS fallback in Phase 1?"
        ]
    )

    print(roadmap.to_markdown())
