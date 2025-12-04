---
name: ml-cv-specialist
description: Deep expertise in ML/CV model selection, training pipelines, and inference architecture. Use when designing machine learning systems, computer vision pipelines, or AI-powered features.
---

# ML/CV Specialist

Provides specialized guidance for machine learning and computer vision system design, model selection, and production deployment.

## When to Use

- Selecting ML models for specific use cases
- Designing training and inference pipelines
- Optimizing ML system performance and cost
- Evaluating build vs. API for ML capabilities
- Planning data pipelines for ML workloads

## ML System Design Framework

### Model Selection Decision Tree

```
Use Case Identified
    │
    ├─► Text/Language Tasks
    │   ├─► Classification → BERT, DistilBERT, or API (OpenAI, Claude)
    │   ├─► Generation → GPT-4, Claude, Llama (self-hosted)
    │   ├─► Embeddings → OpenAI Ada, sentence-transformers
    │   └─► Search/RAG → Vector DB + Embeddings + LLM
    │
    ├─► Computer Vision Tasks
    │   ├─► Classification → ResNet, EfficientNet, ViT
    │   ├─► Object Detection → YOLOv8, DETR, Faster R-CNN
    │   ├─► Segmentation → SAM, Mask R-CNN, U-Net
    │   ├─► OCR → Tesseract, PaddleOCR, Cloud Vision API
    │   └─► Face Recognition → InsightFace, DeepFace
    │
    ├─► Audio Tasks
    │   ├─► Speech-to-Text → Whisper, DeepSpeech, Cloud APIs
    │   ├─► Text-to-Speech → ElevenLabs, Coqui TTS
    │   └─► Audio Classification → PANNs, AudioSet models
    │
    └─► Structured Data
        ├─► Tabular → XGBoost, LightGBM, CatBoost
        ├─► Time Series → Prophet, ARIMA, Transformer-based
        └─► Recommendations → Two-tower, matrix factorization
```

---

## API vs. Self-Hosted Decision

### When to Use APIs

| Factor | API Preferred | Self-Hosted Preferred |
|--------|---------------|----------------------|
| **Volume** | < 10K requests/month | > 100K requests/month |
| **Latency** | > 500ms acceptable | < 100ms required |
| **Customization** | General use case | Domain-specific fine-tuning |
| **Data Privacy** | Non-sensitive data | PII, HIPAA, financial |
| **Team Expertise** | No ML engineers | ML team available |
| **Budget** | Predictable per-call costs | High volume justifies infra |

### Cost Comparison Framework

```markdown
## API Costs (Example: OpenAI GPT-4)
- Input: $0.03/1K tokens
- Output: $0.06/1K tokens
- Average request: 500 input + 200 output tokens
- Cost per request: $0.027
- 100K requests/month: $2,700

## Self-Hosted Costs (Example: Llama 70B)
- GPU instance: $3/hour (A100 40GB)
- Throughput: ~50 requests/minute = 3K/hour
- Cost per request: $0.001
- 100K requests/month: $100 + $500 engineering time

## Break-even Analysis
- < 50K requests: API likely cheaper
- > 50K requests: Self-hosted may be cheaper
- Factor in: engineering time, ops burden, model quality
```

---

## Training Pipeline Architecture

### Standard ML Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                │
├─────────────────────────────────────────────────────────────┤
│  Data Sources → ETL → Feature Store → Training Data         │
│  (S3, DBs)     (Airflow)  (Feast)     (Versioned)          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  TRAINING LAYER                              │
├─────────────────────────────────────────────────────────────┤
│  Experiment Tracking → Training Jobs → Model Registry       │
│  (MLflow, W&B)         (SageMaker)    (MLflow, S3)         │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  SERVING LAYER                               │
├─────────────────────────────────────────────────────────────┤
│  Model Server → Load Balancer → Monitoring                  │
│  (TorchServe)   (K8s/ELB)      (Prometheus)                │
└─────────────────────────────────────────────────────────────┘
```

### Component Selection Guide

| Component | Options | Recommendation |
|-----------|---------|----------------|
| **Feature Store** | Feast, Tecton, SageMaker | Feast (open source), Tecton (enterprise) |
| **Experiment Tracking** | MLflow, Weights & Biases, Neptune | MLflow (free), W&B (best UX) |
| **Training Orchestration** | Kubeflow, SageMaker, Vertex AI | SageMaker (AWS), Vertex (GCP) |
| **Model Registry** | MLflow, SageMaker, custom S3 | MLflow (standard) |
| **Model Serving** | TorchServe, TFServing, Triton | Triton (multi-framework) |

---

## Inference Architecture Patterns

### Pattern 1: Synchronous API

Best for: Low-latency requirements, simple integration

```
Client → API Gateway → Model Server → Response
                           │
                      Load Balancer
                           │
                    ┌──────┴──────┐
                    │             │
                Model Pod    Model Pod
```

**Latency targets**:
- P50: < 100ms
- P95: < 300ms
- P99: < 500ms

### Pattern 2: Asynchronous Processing

Best for: Long-running inference, batch processing

```
Client → API → Queue (SQS) → Worker → Result Store → Webhook/Poll
                                          │
                                     S3/Redis
```

**Use when**:
- Inference > 5 seconds
- Batch processing required
- Variable load patterns

### Pattern 3: Edge Inference

Best for: Privacy, offline capability, ultra-low latency

```
┌─────────────────────────────────────────┐
│              EDGE DEVICE                 │
│  ┌─────────┐    ┌─────────────────────┐ │
│  │ Camera  │───▶│ Optimized Model     │ │
│  └─────────┘    │ (ONNX, TFLite)      │ │
│                 └─────────────────────┘ │
│                          │              │
│                     Local Result        │
└─────────────────────────────────────────┘
                           │
                    Sync to Cloud
                    (non-blocking)
```

**Model optimization for edge**:
- Quantization (INT8): 4x smaller, 2-3x faster
- Pruning: 50-90% sparsity possible
- Distillation: Smaller model, similar accuracy
- ONNX/TFLite: Optimized runtime

---

## Computer Vision Pipeline Design

### Real-Time Video Processing

```
Camera Stream → Frame Extraction → Preprocessing → Model → Postprocessing → Output
     │              │                   │            │           │
   RTSP/         1-30 FPS           Resize,      Batch or    NMS, tracking,
   WebRTC                           normalize    single       annotation
```

**Performance optimization**:
- Process every Nth frame (skip frames)
- Resize to model input size early
- Batch frames when latency allows
- Use GPU preprocessing (NVIDIA DALI)

### Object Detection System

```markdown
## Pipeline Components

1. **Input Processing**
   - Video decode: FFmpeg, OpenCV
   - Frame buffer: Ring buffer for temporal context
   - Preprocessing: NVIDIA DALI (GPU), OpenCV (CPU)

2. **Detection**
   - Model: YOLOv8 (speed), DETR (accuracy)
   - Batch size: 1-8 depending on latency requirements
   - Confidence threshold: 0.5-0.7 typical

3. **Post-processing**
   - NMS (Non-Maximum Suppression)
   - Tracking: SORT, DeepSORT, ByteTrack
   - Smoothing: Kalman filter for stable boxes

4. **Output**
   - Annotations: Bounding boxes, labels, confidence
   - Events: Trigger on detection (webhook, queue)
   - Storage: Frame + metadata to S3/DB
```

---

## LLM Integration Patterns

### RAG (Retrieval-Augmented Generation)

```
User Query → Embedding → Vector Search → Context Retrieval → LLM → Response
                              │
                         Vector DB
                       (Pinecone, Weaviate,
                        Chroma, pgvector)
```

**Vector DB Selection**:
| Database | Best For | Limitations |
|----------|----------|-------------|
| **Pinecone** | Managed, scale | Cost at scale |
| **Weaviate** | Self-hosted, features | Operational overhead |
| **Chroma** | Simple, local dev | Not for production scale |
| **pgvector** | PostgreSQL users | Performance at >1M vectors |
| **Qdrant** | Performance | Newer, smaller community |

### LLM Serving Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    API GATEWAY                               │
│  Rate limiting, auth, request routing                       │
└─────────────────────────────────────────────────────────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
         ┌────────┐   ┌────────┐   ┌────────┐
         │ GPT-4  │   │ Claude │   │ Local  │
         │  API   │   │  API   │   │ Llama  │
         └────────┘   └────────┘   └────────┘
                            │
                    Model Router
              (cost/latency/capability)
```

**Multi-model strategy**:
- Simple queries → Cheaper model (GPT-3.5, Haiku)
- Complex reasoning → Expensive model (GPT-4, Opus)
- Sensitive data → Self-hosted (Llama, Mistral)

---

## Performance Optimization

### GPU Memory Optimization

| Technique | Memory Reduction | Speed Impact |
|-----------|-----------------|--------------|
| **FP16 (Half Precision)** | 50% | Neutral to faster |
| **INT8 Quantization** | 75% | 10-20% slower |
| **INT4 Quantization** | 87.5% | 20-40% slower |
| **Gradient Checkpointing** | 60-80% | 20-30% slower |
| **Model Sharding** | Distributed | Communication overhead |

### Batching Strategies

```python
# Dynamic batching pseudocode
class DynamicBatcher:
    def __init__(self, max_batch=32, max_wait_ms=50):
        self.queue = []
        self.max_batch = max_batch
        self.max_wait = max_wait_ms

    async def add_request(self, request):
        self.queue.append(request)

        # Batch when full or timeout
        if len(self.queue) >= self.max_batch:
            return await self.process_batch()

        await asyncio.sleep(self.max_wait / 1000)
        return await self.process_batch()

    async def process_batch(self):
        batch = self.queue[:self.max_batch]
        self.queue = self.queue[self.max_batch:]
        return await self.model.predict_batch(batch)
```

---

## Model Monitoring

### Key Metrics to Track

| Metric | What It Measures | Alert Threshold |
|--------|------------------|-----------------|
| **Latency (P95)** | Response time | > 2x baseline |
| **Throughput** | Requests/second | < 80% capacity |
| **Error Rate** | Failed predictions | > 1% |
| **Model Drift** | Distribution shift | PSI > 0.2 |
| **Data Quality** | Input anomalies | > 5% anomalies |

### Drift Detection

```
Training Distribution ──┐
                        ├──► Statistical Test ──► Alert
Production Distribution ─┘
                         (PSI, KS test, JS divergence)
```

**Population Stability Index (PSI)**:
- PSI < 0.1: No significant change
- 0.1 < PSI < 0.2: Moderate change, monitor
- PSI > 0.2: Significant change, investigate

---

## Quick Reference Tables

### Model Selection by Use Case

| Use Case | Recommended Model | Latency | Cost |
|----------|-------------------|---------|------|
| Text Classification | DistilBERT | 10ms | Low |
| Text Generation | GPT-4 / Claude | 1-5s | Medium |
| Image Classification | EfficientNet-B0 | 5ms | Low |
| Object Detection | YOLOv8-n | 10ms | Low |
| Object Detection (Accurate) | YOLOv8-x | 50ms | Medium |
| Semantic Segmentation | SAM | 100ms | Medium |
| Speech-to-Text | Whisper-base | Real-time | Low |
| Embeddings | text-embedding-ada-002 | 50ms | Low |

### Infrastructure Sizing

| Scale | GPU | Model Size | Throughput |
|-------|-----|------------|------------|
| Development | T4 (16GB) | < 7B params | 10-50 req/s |
| Production Small | A10G (24GB) | < 13B params | 50-100 req/s |
| Production Medium | A100 (40GB) | < 70B params | 100-500 req/s |
| Production Large | A100 (80GB) x 2+ | > 70B params | 500+ req/s |

---

## References

- [Model Catalog](model-catalog.md) - Detailed model comparison and benchmarks
- [Inference Patterns](inference-patterns.md) - Architecture patterns for different use cases
