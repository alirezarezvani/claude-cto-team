# Architecture Pattern Comparison

Side-by-side comparison of architecture patterns across key dimensions.

## Overview Comparison

| Aspect | Monolith | Modular Monolith | Microservices | Serverless |
|--------|----------|------------------|---------------|------------|
| **Deployment** | Single unit | Single unit | Multiple units | Functions |
| **Database** | Shared | Shared (module schemas) | Per-service | Per-function or shared |
| **Scaling** | Vertical + horizontal | Vertical + horizontal | Per-service | Auto per-function |
| **Team Structure** | Any | Feature teams | Service teams | Function owners |
| **Complexity** | Low | Medium | High | Medium-High |
| **Initial Cost** | Low | Low-Medium | High | Low |
| **Operational Cost** | Medium | Medium | High | Variable |

---

## Detailed Comparison

### Development Experience

| Aspect | Monolith | Modular Monolith | Microservices | Serverless |
|--------|----------|------------------|---------------|------------|
| Local development | Easy | Easy | Complex | Medium |
| Debugging | Easy | Easy | Hard | Hard |
| Testing | Easy | Medium | Complex | Medium |
| Onboarding new devs | Fast | Fast | Slow | Medium |
| IDE support | Excellent | Excellent | Fragmented | Good |
| Refactoring | Easy | Medium | Hard | Medium |

### Operational Characteristics

| Aspect | Monolith | Modular Monolith | Microservices | Serverless |
|--------|----------|------------------|---------------|------------|
| Deployment frequency | Limited by size | Limited by size | Per-service | Per-function |
| Rollback | All or nothing | All or nothing | Per-service | Per-function |
| Monitoring | Simple | Simple | Complex | Complex |
| Distributed tracing | Not needed | Not needed | Essential | Essential |
| Service discovery | Not needed | Not needed | Required | Managed |
| Load balancing | Simple | Simple | Complex | Managed |

### Scaling Characteristics

| Aspect | Monolith | Modular Monolith | Microservices | Serverless |
|--------|----------|------------------|---------------|------------|
| Scale granularity | Entire app | Entire app | Per-service | Per-function |
| Scale speed | Medium | Medium | Fast | Instant |
| Scale to zero | No | No | Possible | Yes |
| Cost at low scale | Fixed | Fixed | Fixed (higher) | Near-zero |
| Cost at high scale | Efficient | Efficient | Variable | Can be high |

### Reliability Characteristics

| Aspect | Monolith | Modular Monolith | Microservices | Serverless |
|--------|----------|------------------|---------------|------------|
| Failure blast radius | Entire app | Entire app | Per-service | Per-function |
| Partial degradation | Hard | Hard | Built-in | Built-in |
| Data consistency | Easy (ACID) | Easy (ACID) | Complex (eventual) | Complex |
| Network failures | Not an issue | Not an issue | Major concern | Major concern |

---

## Cost Analysis

### Development Costs

| Pattern | Initial Build | Feature Development | Maintenance |
|---------|---------------|---------------------|-------------|
| Monolith | $ | $ | $ |
| Modular Monolith | $$ | $ | $$ |
| Microservices | $$$$ | $$ | $$$$ |
| Serverless | $$ | $$ | $$ |

### Infrastructure Costs (at different scales)

| Pattern | 10K users/mo | 100K users/mo | 1M users/mo | 10M users/mo |
|---------|--------------|---------------|-------------|--------------|
| Monolith | $50-200 | $200-500 | $500-2K | $2K-10K |
| Modular Monolith | $50-200 | $200-500 | $500-2K | $2K-10K |
| Microservices | $200-500 | $500-2K | $2K-10K | $10K-50K |
| Serverless | $10-50 | $50-500 | $500-5K | $5K-50K |

*Note: Costs are illustrative. Actual costs depend heavily on workload characteristics.*

### Hidden Costs

| Pattern | Hidden Costs |
|---------|-------------|
| Monolith | Technical debt accumulation, scaling ceiling |
| Modular Monolith | Discipline required to maintain boundaries |
| Microservices | Platform team, tooling, training, debugging time |
| Serverless | Cold starts, vendor lock-in, debugging complexity |

---

## Team Requirements

### Minimum Team for Effective Operation

| Pattern | Min Engineers | Required Roles |
|---------|---------------|----------------|
| Monolith | 1 | Full-stack developer |
| Modular Monolith | 3 | Full-stack developers with architecture awareness |
| Microservices | 15+ | Platform team (2-3), service teams, SRE |
| Serverless | 2 | Cloud-native developers |

### Skills Required

| Pattern | Essential Skills |
|---------|-----------------|
| Monolith | Language/framework, SQL, basic deployment |
| Modular Monolith | Above + DDD, module design, interface design |
| Microservices | Above + containers, K8s, service mesh, distributed systems |
| Serverless | Cloud provider, event-driven design, IAM, monitoring |

---

## Migration Paths

### From Monolith

```
Monolith
    │
    ├──► Modular Monolith (lowest risk)
    │         │
    │         └──► Microservices (when ready)
    │
    ├──► Hybrid (extract specific services)
    │
    └──► Serverless (for specific workloads)
```

### Migration Triggers

| From | To | Trigger |
|------|-----|---------|
| Monolith | Modular Monolith | Team growing, code getting tangled |
| Modular Monolith | Microservices | Modules need independent scaling/deployment |
| Any | Serverless | Event-driven workloads, cost optimization |
| Microservices | Modular Monolith | Over-distributed, too much overhead |

---

## Technology Stack Examples

### Monolith

```
┌─────────────────────────────────────┐
│           Load Balancer             │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│         Application Server          │
│  ┌─────────────────────────────┐    │
│  │  Rails / Django / Spring     │    │
│  │  All features in one codebase│    │
│  └─────────────────────────────┘    │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│           PostgreSQL                │
└─────────────────────────────────────┘
```

### Modular Monolith

```
┌─────────────────────────────────────┐
│           Load Balancer             │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│         Application Server          │
│  ┌─────────┬─────────┬─────────┐   │
│  │ Users   │ Orders  │ Products│   │
│  │ Module  │ Module  │ Module  │   │
│  └────┬────┴────┬────┴────┬────┘   │
│       │ Internal APIs     │        │
└───────┴─────────┬─────────┴────────┘
                  │
┌─────────────────▼───────────────────┐
│   PostgreSQL (schema per module)    │
└─────────────────────────────────────┘
```

### Microservices

```
┌─────────────────────────────────────┐
│         API Gateway / Mesh          │
└───┬─────────────┬─────────────┬─────┘
    │             │             │
┌───▼───┐    ┌────▼───┐    ┌───▼────┐
│ Users │    │ Orders │    │Products│
│Service│    │Service │    │Service │
└───┬───┘    └────┬───┘    └───┬────┘
    │             │             │
┌───▼───┐    ┌────▼───┐    ┌───▼────┐
│User DB│    │Order DB│    │Prod DB │
└───────┘    └────────┘    └────────┘
```

### Serverless

```
┌─────────────────────────────────────┐
│          API Gateway                │
└───┬─────────────┬─────────────┬─────┘
    │             │             │
┌───▼───┐    ┌────▼───┐    ┌───▼────┐
│Lambda │    │Lambda  │    │Lambda  │
│GetUser│    │CreateOrd│   │ListProd│
└───┬───┘    └────┬───┘    └───┬────┘
    │             │             │
    └─────────────┼─────────────┘
                  │
         ┌────────▼────────┐
         │   DynamoDB      │
         └─────────────────┘
```

---

## Decision Checklist

Before finalizing pattern selection, verify:

- [ ] Team has required skills (or plan to acquire)
- [ ] Budget covers operational costs at projected scale
- [ ] Timeline accounts for infrastructure setup
- [ ] Migration path exists if requirements change
- [ ] Trade-offs are explicitly accepted by stakeholders
- [ ] Pattern matches actual needs, not industry hype
