# CTO Office - Three-Agent System Documentation

**Last Updated**: December 4, 2025
**Maintainer**: Claude Code / Technical Writer Agent
**Version**: 1.1

## Overview

This documentation describes the **CTO Office Three-Agent System**, a comprehensive framework for strategic technical leadership, architecture design, and validation. The system consists of three specialized agents that work together to transform vague business requirements into validated, actionable technical strategies.

### The Three Agents

| Agent | Role | Primary Function |
|-------|------|------------------|
| **cto-orchestrator** | Coordinator & Router | Breaks down vague requests, routes to specialists, maintains context across complex workflows |
| **cto-architect** | Designer & Builder | Creates comprehensive architecture designs, technology decisions, and implementation roadmaps |
| **strategic-cto-mentor** | Validator & Critic | Provides ruthless validation of plans, challenges assumptions, stress-tests strategies |

## Quick Start Guide

### For All Users

1. **System overview**: Read [Three-Agent System Overview](04-context-preservation/three-agent-system-overview.md) to understand the philosophy
2. **Capability matrix**: Study [Agent Capability Matrix](02-collaboration-patterns/agent-capability-matrix.md) to know when to use which agent
3. **Agent specifications**: Check [Agent Specifications](01-agent-specifications/) for detailed capabilities

### For CTOs and Technical Leaders

1. **Leverage validation**: Use strategic-cto-mentor to stress-test high-stakes decisions
2. **Orchestrate complexity**: Engage cto-orchestrator for multi-domain projects
3. **Design systematically**: Rely on cto-architect for comprehensive architecture

## Folder Structure

```
documentation/cto-office/
├── README.md (this file)
│
├── 01-agent-specifications/
│   ├── cto-orchestrator-spec.md       # Coordinator specifications
│   ├── strategic-cto-mentor-spec.md   # Validator specifications
│   └── cto-architect-spec.md          # Designer specifications
│
├── 02-collaboration-patterns/
│   └── agent-capability-matrix.md     # Comparison table & workflows
│
├── 03-use-cases/                      # (Planned: real-world examples)
│
└── 04-context-preservation/
    └── three-agent-system-overview.md # System philosophy & architecture
```

## Key Principles

### Checks and Balances

The three-agent system implements a checks-and-balances mechanism:

- **cto-orchestrator** ensures requirements are clear before design begins
- **cto-architect** creates comprehensive, well-thought-out designs
- **strategic-cto-mentor** provides ruthless validation before resource commitment

This prevents:
- Implementing vague requirements (orchestrator catches this)
- Weak architectures reaching production (architect designs robustly)
- Wishful thinking driving decisions (mentor challenges assumptions)

### Role Separation

Each agent has a distinct role:

- **Design work** → cto-architect (not validation)
- **Validation work** → strategic-cto-mentor (not design)
- **Coordination** → cto-orchestrator (not deep technical work)

This separation ensures:
- Specialists do what they do best
- No agent is overloaded
- Clear accountability for outputs

## Agent Routing Decision Tree

| User Says | Route To |
|-----------|----------|
| "I want to add [vague feature]" | cto-orchestrator (will clarify then route) |
| "How should I build X?" | cto-architect (design work) |
| "Is this plan solid?" | strategic-cto-mentor (validation work) |
| "Thoughts on my roadmap?" | strategic-cto-mentor (validation work) |
| Complex multi-domain project | cto-orchestrator (coordinates multiple agents) |

## Related Resources

### Agent Source Files
- **cto-orchestrator**: `.claude/agents/cto-orchestrator.md`
- **strategic-cto-mentor**: `.claude/agents/strategic-cto-mentor.md`
- **cto-architect**: `.claude/agents/cto-architect.md`

### Documentation Files
- [Agent Capability Matrix](02-collaboration-patterns/agent-capability-matrix.md)
- [Three-Agent System Overview](04-context-preservation/three-agent-system-overview.md)
- [cto-orchestrator Specification](01-agent-specifications/cto-orchestrator-spec.md)
- [cto-architect Specification](01-agent-specifications/cto-architect-spec.md)
- [strategic-cto-mentor Specification](01-agent-specifications/strategic-cto-mentor-spec.md)

### External Documentation
- Claude Code Documentation: https://github.com/anthropics/claude-code

## Version History

| Version | Date | Changes | Maintainer |
|---------|------|---------|------------|
| 1.1 | 2025-12-04 | Updated paths to project-relative, removed missing file references | Claude Code |
| 1.0 | 2025-12-04 | Initial documentation system created | Claude Code |

---

**Note**: This documentation serves as the reference for the CTO Office Three-Agent System. Copy the `.claude/agents/` and `documentation/` folders to your project to use these agents.
