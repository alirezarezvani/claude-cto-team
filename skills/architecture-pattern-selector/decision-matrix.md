# Architecture Pattern Decision Matrix

Scoring framework for selecting the right architecture pattern.

## How to Use

1. Score each factor (1-5) based on your situation
2. Multiply by weight
3. Sum scores for each pattern
4. Highest score = recommended pattern

## Scoring Factors

### Factor 1: Team Size (Weight: 3)

| Team Size | Monolith | Modular Monolith | Microservices | Serverless |
|-----------|----------|------------------|---------------|------------|
| < 5 engineers | 5 | 3 | 1 | 4 |
| 5-15 engineers | 4 | 5 | 2 | 3 |
| 15-50 engineers | 2 | 4 | 4 | 3 |
| > 50 engineers | 1 | 3 | 5 | 2 |

### Factor 2: Expected Scale (Weight: 3)

| Scale | Monolith | Modular Monolith | Microservices | Serverless |
|-------|----------|------------------|---------------|------------|
| < 10K users | 5 | 4 | 1 | 4 |
| 10K-100K users | 4 | 5 | 2 | 4 |
| 100K-1M users | 3 | 4 | 4 | 3 |
| 1M-10M users | 2 | 3 | 5 | 3 |
| > 10M users | 1 | 2 | 5 | 2 |

### Factor 3: DevOps Maturity (Weight: 4)

| Maturity | Monolith | Modular Monolith | Microservices | Serverless |
|----------|----------|------------------|---------------|------------|
| None (manual deploys) | 5 | 3 | 1 | 3 |
| Basic (CI/CD) | 4 | 4 | 2 | 4 |
| Intermediate (containers) | 3 | 5 | 3 | 4 |
| Advanced (K8s, service mesh) | 2 | 4 | 5 | 3 |

### Factor 4: Time to Market Pressure (Weight: 3)

| Pressure | Monolith | Modular Monolith | Microservices | Serverless |
|----------|----------|------------------|---------------|------------|
| Critical (< 3 months) | 5 | 3 | 1 | 4 |
| High (3-6 months) | 4 | 4 | 2 | 4 |
| Medium (6-12 months) | 3 | 5 | 4 | 3 |
| Low (> 12 months) | 2 | 4 | 5 | 3 |

### Factor 5: Traffic Pattern (Weight: 2)

| Pattern | Monolith | Modular Monolith | Microservices | Serverless |
|---------|----------|------------------|---------------|------------|
| Steady/predictable | 4 | 4 | 3 | 2 |
| Moderate spikes (2-3x) | 3 | 4 | 4 | 4 |
| High spikes (10x+) | 2 | 3 | 4 | 5 |
| Unpredictable/event-driven | 2 | 3 | 3 | 5 |

### Factor 6: Latency Requirements (Weight: 2)

| Requirement | Monolith | Modular Monolith | Microservices | Serverless |
|-------------|----------|------------------|---------------|------------|
| Real-time (< 50ms) | 4 | 4 | 3 | 1 |
| Interactive (< 200ms) | 4 | 4 | 4 | 3 |
| Standard (< 1s) | 4 | 4 | 4 | 4 |
| Tolerant (> 1s ok) | 4 | 4 | 4 | 5 |

### Factor 7: Domain Clarity (Weight: 3)

| Clarity | Monolith | Modular Monolith | Microservices | Serverless |
|---------|----------|------------------|---------------|------------|
| Unclear/evolving | 5 | 4 | 1 | 3 |
| Partially defined | 4 | 5 | 2 | 3 |
| Well-defined | 3 | 4 | 4 | 4 |
| Crystal clear bounded contexts | 2 | 3 | 5 | 4 |

### Factor 8: Budget Constraints (Weight: 2)

| Budget | Monolith | Modular Monolith | Microservices | Serverless |
|--------|----------|------------------|---------------|------------|
| Very tight | 5 | 4 | 1 | 4 |
| Limited | 4 | 4 | 2 | 4 |
| Moderate | 3 | 4 | 4 | 4 |
| Generous | 3 | 4 | 5 | 3 |

---

## Score Calculation Example

**Scenario**: Series A startup, 12 engineers, targeting 500K users in 12 months, basic DevOps, need to ship MVP in 4 months.

| Factor | Weight | Monolith | Mod. Mono | Microservices | Serverless |
|--------|--------|----------|-----------|---------------|------------|
| Team Size (12) | 3 | 4×3=12 | 5×3=15 | 2×3=6 | 3×3=9 |
| Scale (500K) | 3 | 3×3=9 | 4×3=12 | 4×3=12 | 3×3=9 |
| DevOps (Basic) | 4 | 4×4=16 | 4×4=16 | 2×4=8 | 4×4=16 |
| Time (4 mo) | 3 | 5×3=15 | 3×3=9 | 1×3=3 | 4×3=12 |
| Traffic (Mod.) | 2 | 3×2=6 | 4×2=8 | 4×2=8 | 4×2=8 |
| Latency (Std) | 2 | 4×2=8 | 4×2=8 | 4×2=8 | 4×2=8 |
| Domain (Partial) | 3 | 4×3=12 | 5×3=15 | 2×3=6 | 3×3=9 |
| Budget (Limited) | 2 | 4×2=8 | 4×2=8 | 2×2=4 | 4×2=8 |
| **TOTAL** | | **86** | **91** | **55** | **79** |

**Recommendation**: Modular Monolith (highest score: 91)

---

## Quick Decision Guide

### Choose Monolith If:
- Score > 80 AND team < 10 AND time critical

### Choose Modular Monolith If:
- Highest score AND team 10-30 AND moderate time pressure

### Choose Microservices If:
- Score > 75 AND team > 30 AND DevOps advanced AND domains clear

### Choose Serverless If:
- Score > 75 AND traffic spiky AND latency tolerant AND event-driven

### Choose Hybrid If:
- No pattern scores > 75 AND different components have different needs

---

## Override Conditions

Regardless of scores, certain conditions override the matrix:

### Force Monolith
- Team < 5 engineers (complexity will overwhelm)
- No product-market fit yet (need iteration speed)
- < 3 month deadline (no time for distributed systems)

### Force Microservices
- Regulatory requirement for isolation
- Acquisitions requiring integration of disparate systems
- Team > 100 with clear bounded contexts

### Force Serverless
- Extremely variable load (10x+ spikes regularly)
- Event processing workloads
- Strict budget constraints with unpredictable usage

---

## Scoring Template

Copy and fill in for your project:

```markdown
## Architecture Pattern Score

**Project**: [Name]
**Date**: [Date]

| Factor | Weight | Score | Reasoning |
|--------|--------|-------|-----------|
| Team Size | 3 | | |
| Expected Scale | 3 | | |
| DevOps Maturity | 4 | | |
| Time to Market | 3 | | |
| Traffic Pattern | 2 | | |
| Latency Req | 2 | | |
| Domain Clarity | 3 | | |
| Budget | 2 | | |

**Total Scores**:
- Monolith:
- Modular Monolith:
- Microservices:
- Serverless:

**Recommended Pattern**:
**Override Conditions**: [None / If applicable]
```
