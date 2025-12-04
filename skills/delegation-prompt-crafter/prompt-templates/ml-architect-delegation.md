# ML Architect Delegation Template

Use this template when delegating ML/AI design work to **cv-ml-architect**.

## Template

```markdown
## CONTEXT

### Business Goal
[What business outcome does the ML/AI capability enable?]
[How does ML success translate to measurable business value?]

### ML Problem Framing
- **Problem Type**: [Classification / Regression / Recommendation / Generation / Detection / Other]
- **Success Metric**: [Accuracy / Precision / Recall / F1 / RMSE / Custom metric]
- **Baseline**: [Current performance or human-level benchmark]
- **Target**: [What improvement makes this worthwhile?]

### Current State
**Existing Systems:**
- [Current ML infrastructure, if any]
- [Data pipelines and storage]
- [Model serving infrastructure]

**Data Situation:**
- [What training data exists?]
- [Data volume and quality]
- [Labeling status]
- [Privacy/compliance considerations]

**Previous Attempts:**
- [What ML approaches were tried before?]
- [Why did they fail or underperform?]

### Key Constraints
- **Budget**: [Infrastructure budget, labeling budget, API costs]
- **Timeline**: [Time to first model, time to production]
- **Team**: [ML experience level, available data scientists/engineers]
- **Technical**: [Must integrate with existing systems, latency requirements]
- **Data**: [Privacy restrictions, data availability, labeling constraints]

### Scale Parameters
- **Inference Volume**: [Predictions per day/hour/second]
- **Latency Requirements**: [Real-time vs batch, acceptable response time]
- **Model Update Frequency**: [How often should model retrain?]

---

## TASK

### Primary Deliverable
Design ML architecture for [specific ML capability]

### Format Requirements
Provide ML architecture document with:
1. **Problem Analysis**: ML problem framing, success metrics, feasibility assessment
2. **Data Strategy**: Data requirements, collection, labeling, pipeline design
3. **Model Architecture**: Model selection, architecture decisions, trade-offs
4. **Training Pipeline**: Training infrastructure, experiment tracking, validation
5. **Serving Architecture**: Inference infrastructure, latency optimization, scaling
6. **MLOps Design**: Monitoring, retraining triggers, A/B testing, rollback
7. **Implementation Roadmap**: MVP to production phases with validation gates
8. **Risk Assessment**: Data risks, model risks, operational risks

### Scope Boundaries
**In Scope:**
- [Specific ML capabilities to design]
- [Specific decisions to make]

**Out of Scope:**
- [Non-ML components (handled by cto-architect)]
- [Future ML features]
- [Already decided aspects]

---

## REQUIREMENTS

### Must-Haves
- [ ] [Critical ML requirement 1]
- [ ] [Critical ML requirement 2]
- [ ] [Critical data requirement]

### Nice-to-Haves
- [ ] [ML enhancement 1]
- [ ] [Advanced capability]

### Quality Criteria
- **Model Performance**: [Accuracy/precision/recall targets]
- **Latency**: [Inference time requirements]
- **Scalability**: [Volume handling requirements]
- **Cost**: [Training and inference cost constraints]
- **Reliability**: [Uptime, fallback handling]

### Non-Functional Requirements
- **Explainability**: [Model interpretability needs]
- **Fairness**: [Bias detection and mitigation requirements]
- **Privacy**: [Data protection, differential privacy needs]
- **Monitoring**: [Drift detection, performance monitoring]

---

## DATA CONTEXT

### Available Data
| Dataset | Size | Quality | Labels | Access |
|---------|------|---------|--------|--------|
| [Dataset 1] | [Size] | [High/Med/Low] | [Yes/No/Partial] | [Available/Restricted] |
| [Dataset 2] | [Size] | [Quality] | [Label status] | [Access status] |

### Data Gaps
- [Missing data that would improve model]
- [Quality issues to address]
- [Labeling work needed]

### Data Constraints
- [Privacy/compliance restrictions]
- [Data retention policies]
- [Cross-border data transfer limitations]

---

## INTEGRATION POINTS

### Upstream
- [What triggers predictions? What data feeds the model?]

### Downstream
- [What consumes predictions? What decisions are made?]

### Workflow Context
- [What happens after ML design is complete?]
- [Will this be validated by strategic-cto-mentor?]
- [How does this integrate with overall system architecture from cto-architect?]

---

## ADDITIONAL CONTEXT

### Stakeholder Expectations
- [What do stakeholders expect from ML? (Realistic?)]
- [Previous ML projects and outcomes]

### Build vs Buy Considerations
- [Has third-party ML/AI been evaluated?]
- [API options (OpenAI, Claude, etc.) considered?]
- [Why custom ML over pre-built?]

### Open Questions
- [Decisions still open for ML architect input]
```

## Example: Product Recommendation Engine

```markdown
## CONTEXT

### Business Goal
Increase average order value by 15% and conversion rate by 10% through personalized product recommendations on e-commerce platform.

### ML Problem Framing
- **Problem Type**: Recommendation (collaborative filtering + content-based)
- **Success Metric**: Click-through rate (CTR), add-to-cart rate, revenue per recommendation
- **Baseline**: Current rule-based recommendations: 2% CTR, 0.5% add-to-cart
- **Target**: 5% CTR, 1.5% add-to-cart (2.5x improvement)

### Current State
**Existing Systems:**
- No ML infrastructure currently
- PostgreSQL for product catalog and orders
- Redis for session caching
- AWS infrastructure (EC2, RDS, S3)

**Data Situation:**
- 2 years of order history (500K orders)
- Product catalog with categories, descriptions, images
- User browsing sessions (partial - last 6 months)
- No explicit ratings or reviews

**Previous Attempts:**
- Rule-based "customers also bought" implemented 1 year ago
- Static category-based recommendations (poor performance)

### Key Constraints
- **Budget**: < $5K/month infrastructure, no budget for external APIs at scale
- **Timeline**: MVP in 8 weeks, production in 12 weeks
- **Team**: 1 ML engineer (junior), 2 backend engineers familiar with AWS
- **Technical**: Must integrate with existing product pages, < 100ms latency requirement
- **Data**: No PII in recommendations, GDPR compliant

### Scale Parameters
- **Inference Volume**: 10M recommendations/day (peak 500 req/sec)
- **Latency Requirements**: p95 < 100ms for API response
- **Model Update Frequency**: Daily batch retraining acceptable

---

## TASK

### Primary Deliverable
Design ML architecture for personalized product recommendation system

### Format Requirements
Full ML architecture document with emphasis on:
- Cold start problem handling (new users, new products)
- Real-time vs batch recommendation strategy
- A/B testing framework for recommendation models
- Cost analysis at current and 10x scale

### Scope Boundaries
**In Scope:**
- Product recommendation model architecture
- Training and serving infrastructure
- MLOps and monitoring design
- Cold start handling strategies

**Out of Scope:**
- Search ranking (separate project)
- Email recommendation personalization (Phase 2)
- Image-based visual similarity (Phase 2)

---

## REQUIREMENTS

### Must-Haves
- [ ] Handle cold start for new users (< 5 interactions)
- [ ] Handle cold start for new products (< 10 views)
- [ ] Serve recommendations in < 100ms
- [ ] Support 10M daily recommendation requests
- [ ] GDPR compliant (no PII stored in model)

### Nice-to-Haves
- [ ] Context-aware recommendations (time of day, device)
- [ ] Explainability ("Recommended because you bought...")
- [ ] Cross-sell vs upsell recommendation types

### Quality Criteria
- **Model Performance**: CTR > 4% (2x baseline)
- **Latency**: p95 < 100ms, p99 < 200ms
- **Scalability**: Handle 1000 req/sec at peak
- **Cost**: < $5K/month at current scale, < $15K at 10x
- **Reliability**: 99.9% availability with graceful fallback

---

## DATA CONTEXT

### Available Data
| Dataset | Size | Quality | Labels | Access |
|---------|------|---------|--------|--------|
| Order history | 500K orders | High | Implicit (purchases) | Full access |
| Product catalog | 50K SKUs | High | Categories, attributes | Full access |
| Browse sessions | 10M sessions | Medium | Click events | 6 months only |
| User profiles | 100K users | Medium | Demographics | Anonymized |

### Data Gaps
- No explicit ratings (must use implicit signals)
- Browse data only 6 months (recommend extending)
- Limited product descriptions (could improve content-based)

### Data Constraints
- No PII can be used in model features
- User data must be deletable (GDPR right to erasure)
- Cross-border: EU user data stays in EU region

---

## INTEGRATION POINTS

### Upstream
- Product page views trigger recommendation requests
- Cart events update user preferences in real-time
- Product catalog updates feed content-based features

### Downstream
- Recommendations displayed on product pages, cart, homepage
- A/B test results feed back to model evaluation
- Business analytics consumes CTR and revenue metrics

### Workflow Context
- ML design will be validated by strategic-cto-mentor
- Backend integration designed by cto-architect
- ML engineer implements training pipeline, backend team implements serving

---

## ADDITIONAL CONTEXT

### Stakeholder Expectations
VP of Product expects "Amazon-like" recommendations. Need to set realistic expectations for MVP with limited data.

### Build vs Buy Considerations
- Evaluated Algolia Recommend ($3K/month at current scale)
- AWS Personalize evaluated ($2K/month + complexity)
- Decision: Build custom for learning and flexibility, with fallback to rule-based

### Open Questions
- Should we start with collaborative filtering only, or hybrid from day 1?
- How to handle product categories with < 100 items (sparse data)?
- Acceptable fallback behavior when model confidence is low?
```
