# Claude Code Custom CTO Team - AI-Powered Technical Leadership Agents

[![GitHub stars](https://img.shields.io/github/stars/alirezarezvani/claude-cto-team?style=social)](https://github.com/alirezarezvani/claude-cto-team)
[![GitHub forks](https://img.shields.io/github/forks/alirezarezvani/claude-cto-team?style=social)](https://github.com/alirezarezvani/claude-cto-team/fork)
[![GitHub issues](https://img.shields.io/github/issues/alirezarezvani/claude-cto-team)](https://github.com/alirezarezvani/claude-cto-team/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/alirezarezvani/claude-cto-team)](https://github.com/alirezarezvani/claude-cto-team/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blueviolet)](https://claude.ai/code)

> **Your personal CTO Team for Claude Code** - Custom AI subagents that provide strategic technical leadership, system architecture design, and brutally honest feedback on your technical decisions.

Transform how you plan and execute software projects with three specialized AI agents that challenge your thinking, design scalable architectures, and validate your roadmaps before you commit resources.

---

## Table of Contents

- [Why Use Claude Code CTO Team?](#why-use-claude-code-cto-team)
- [The Three-Agent System](#the-three-agent-system)
- [Agent Capabilities](#agent-capabilities)
  - [cto-orchestrator](#cto-orchestrator-sonnet)
  - [cto-architect](#cto-architect-opus)
  - [strategic-cto-mentor](#strategic-cto-mentor-opus)
- [How the Agents Collaborate](#how-the-agents-collaborate)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Author](#author)
- [Contributing](#contributing)
- [Support This Project](#support-this-project)
- [License](#license)

---

## Why Use Claude Code CTO Team?

- **Strategic Technical Guidance**: Get CTO-level advice on architecture, technology stack, and implementation roadmaps
- **Honest Feedback**: Receive ruthless validation of your plans before costly mistakes
- **Multi-Domain Expertise**: ML/AI integration, cloud infrastructure, full-stack development, and scalability planning
- **Faster Decision Making**: Route complex technical questions to the right specialist instantly

## The Three-Agent System

| Agent | Role | Best For |
|-------|------|----------|
| **cto-orchestrator** | Coordinator & Router | Vague requirements, multi-domain projects, unclear where to start |
| **cto-architect** | System Designer | New architecture, "How should I build X?", technology decisions, roadmaps |
| **strategic-cto-mentor** | Ruthless Validator | Validating plans, build vs buy, prioritization, need honest feedback |

## Agent Capabilities

### cto-orchestrator (Sonnet)

The intelligent entry point for complex technical requests. Challenges vague buzzwords, clarifies requirements, and routes work to the right specialist.

**Example triggers:**
- "I want to add AI capabilities to my app"
- "Here's my Q2 roadmap, what do you think?"
- "Our app is slow and users are complaining"

### cto-architect (Opus)

Designs comprehensive system architectures and implementation roadmaps with 15+ years of simulated experience in scalable web/mobile applications with ML/AI integration.

**Core expertise:**
- **Full-stack**: React, NextJS, Node.js, React Native, Swift, Kotlin
- **Backend**: Microservices, PostgreSQL, GraphQL, REST APIs
- **ML/AI**: Real-time CV pipelines, model serving, vector databases, RAG systems
- **Infrastructure**: Kubernetes, Docker, AWS/GCP, multi-region deployments

**Deliverables:**
- Executive summary with budget estimates
- System architecture with component diagrams
- Technology stack with explicit trade-off analysis
- Phased implementation roadmap with validation checkpoints
- Risk assessment and mitigation strategies

### strategic-cto-mentor (Opus)

Ruthless CTO mentor who stress-tests your ideas until they're bulletproof. Simulates 20+ years of experience with hard lessons from both failed and successful ventures.

**Seven-Dimension Evaluation Framework:**
1. Business Impact
2. Technical Risk
3. Operational Risk
4. Financial Risk
5. Timeline Risk
6. Team Risk
7. Market Risk

**Anti-patterns Identified:**
- Premature Optimization Trap
- Shiny Object Syndrome
- Technical Debt Denial
- Consensus Paralysis
- Hero Culture
- Build Trap
- Timeline Fantasy

## How the Agents Collaborate

```
User Request
     │
     ▼
┌─────────────────────────────────────────┐
│          cto-orchestrator               │
│  Clarifies → Challenges → Routes        │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┴────────────┐
    ▼                         ▼
┌───────────────┐    ┌─────────────────────┐
│ cto-architect │    │ strategic-cto-mentor│
│   (Design)    │───▶│    (Validate)       │
└───────────────┘    └─────────────────────┘
```

**Design → Validate**: Architect creates design, mentor stress-tests it
**Validate → Design**: Mentor identifies flaws, architect revises

## Prerequisites

Before installing the CTO Team agents, ensure you have:

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured
- An active Anthropic API key or Claude Pro/Max subscription
- A project directory where you want to use the agents

## Installation

### Option 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-cto-team.git

# Copy agents to your project
cp -r claude-cto-team/.claude/agents /path/to/your/project/.claude/
```

### Option 2: Manual Setup

1. Create the agents directory in your project:

```bash
mkdir -p .claude/agents
```

2. Download or copy the agent files from this repository into `.claude/agents/`:

```
.claude/
└── agents/
    ├── cto-architect.md
    ├── cto-orchestrator.md
    └── strategic-cto-mentor.md
```

3. The agents are automatically available in Claude Code when you open your project.

## Usage Examples

### Architecture Design Request
> "I want to build a mobile app that uses computer vision to identify plants. We expect 100K users in the first year."

→ Routes to **cto-architect** for comprehensive architecture design with ML pipeline recommendations

### Strategic Plan Validation
> "Here's my draft Q2 roadmap: migrate to Kubernetes, implement real-time features, refactor payments, launch mobile app."

→ Routes to **strategic-cto-mentor** for ruthless stress-testing and timeline reality check

### Build vs Buy Decision
> "Should we use OpenAI's API or host our own LLM? We're processing 50K conversations per month."

→ Routes to **strategic-cto-mentor** for TCO analysis and trade-off evaluation

## Author

**Alireza Rezvani**

[![Website](https://img.shields.io/badge/Website-alirezarezvani.com-blue)](https://alirezarezvani.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-alirezarezvani-0077B5?logo=linkedin)](https://www.linkedin.com/in/alirezarezvani/)
[![Medium](https://img.shields.io/badge/Medium-@alirezarezvani-12100E?logo=medium)](https://alirezarezvani.medium.com/)

- Website: [alirezarezvani.com](https://alirezarezvani.com)
- LinkedIn: [linkedin.com/in/alirezarezvani](https://www.linkedin.com/in/alirezarezvani/)
- Medium: [alirezarezvani.medium.com](https://alirezarezvani.medium.com/)

## Contributing

Contributions are welcome! If you have ideas for improving these agents or want to add new capabilities:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-agent`)
3. Commit your changes (`git commit -m 'Add new agent capability'`)
4. Push to the branch (`git push origin feature/new-agent`)
5. Open a Pull Request

## Support This Project

If this project saved you time or helped you make better technical decisions, consider supporting its continued development:

[![Buy me a book](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20book&emoji=📖&slug=rezarezvani&button_colour=40DCA5&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00)](https://www.buymeacoffee.com/rezarezvani)

A star on GitHub also helps others discover this project:

[![Star this repo](https://img.shields.io/github/stars/alirezarezvani/claude-cto-team?style=social)](https://github.com/alirezarezvani/claude-cto-team)

## License

MIT License - [Alireza Rezvani](https://alirezarezvani.com)

---

**Found this useful?** Share it with your network and help others discover AI-powered technical leadership for Claude Code!
