# Model Catalog

Comprehensive comparison of ML/CV models by category with performance benchmarks and use case recommendations.

---

## Large Language Models (LLMs)

### API-Based Models

| Model | Provider | Context | Speed | Cost | Best For |
|-------|----------|---------|-------|------|----------|
| **GPT-4 Turbo** | OpenAI | 128K | Medium | $$$$ | Complex reasoning, code |
| **GPT-4o** | OpenAI | 128K | Fast | $$$ | Multimodal, general |
| **GPT-3.5 Turbo** | OpenAI | 16K | Fast | $ | Simple tasks, chat |
| **Claude 3 Opus** | Anthropic | 200K | Medium | $$$$ | Analysis, long context |
| **Claude 3.5 Sonnet** | Anthropic | 200K | Fast | $$ | Balanced quality/speed |
| **Claude 3 Haiku** | Anthropic | 200K | Very Fast | $ | High volume, simple |
| **Gemini Pro** | Google | 32K | Fast | $$ | Google ecosystem |

### Open Source Models (Self-Hosted)

| Model | Parameters | VRAM | Speed | Quality | License |
|-------|------------|------|-------|---------|---------|
| **Llama 3 70B** | 70B | 140GB | Slow | Excellent | Meta |
| **Llama 3 8B** | 8B | 16GB | Fast | Good | Meta |
| **Mistral 7B** | 7B | 14GB | Fast | Good | Apache 2.0 |
| **Mixtral 8x7B** | 47B active | 90GB | Medium | Very Good | Apache 2.0 |
| **Phi-3 Mini** | 3.8B | 8GB | Very Fast | Good | MIT |
| **Qwen 2 72B** | 72B | 144GB | Slow | Excellent | Apache 2.0 |

### LLM Selection Guide

```
Need reasoning/analysis?
├── YES → Budget available?
│   ├── YES → GPT-4 / Claude Opus
│   └── NO → Llama 70B / Mixtral (self-hosted)
│
└── NO → Simple chat/completion?
    ├── High volume → GPT-3.5 / Claude Haiku
    └── Data privacy → Llama 8B / Mistral 7B
```

---

## Computer Vision Models

### Image Classification

| Model | Top-1 Accuracy | Params | Latency (GPU) | Best For |
|-------|----------------|--------|---------------|----------|
| **EfficientNet-B0** | 77.1% | 5.3M | 3ms | Mobile/edge |
| **EfficientNet-B4** | 82.9% | 19M | 8ms | Balanced |
| **EfficientNet-B7** | 84.3% | 66M | 25ms | High accuracy |
| **ResNet-50** | 76.1% | 25M | 5ms | Standard baseline |
| **ResNet-152** | 78.3% | 60M | 15ms | Higher accuracy |
| **ViT-B/16** | 81.8% | 86M | 10ms | Modern, attention-based |
| **ConvNeXt-Base** | 83.8% | 89M | 12ms | SOTA CNN |

### Object Detection

| Model | mAP (COCO) | Params | FPS (V100) | Best For |
|-------|------------|--------|------------|----------|
| **YOLOv8-n** | 37.3% | 3.2M | 200+ | Real-time, edge |
| **YOLOv8-s** | 44.9% | 11.2M | 150+ | Balanced |
| **YOLOv8-m** | 50.2% | 25.9M | 100+ | Good accuracy |
| **YOLOv8-l** | 52.9% | 43.7M | 60+ | High accuracy |
| **YOLOv8-x** | 53.9% | 68.2M | 40+ | Best accuracy |
| **DETR** | 42.0% | 41M | 28 | Transformer-based |
| **RT-DETR-L** | 53.0% | 32M | 100+ | Real-time transformer |

### Segmentation

| Model | Type | mIoU | Speed | Best For |
|-------|------|------|-------|----------|
| **SAM (ViT-H)** | Instance/Semantic | N/A | 50ms | Zero-shot, interactive |
| **SAM (ViT-B)** | Instance/Semantic | N/A | 15ms | Faster SAM |
| **Mask R-CNN** | Instance | 38.2% | 100ms | Standard instance seg |
| **U-Net** | Semantic | Varies | 20ms | Medical imaging |
| **DeepLabV3+** | Semantic | 82.1% | 30ms | High accuracy |
| **SegFormer-B5** | Semantic | 84.0% | 25ms | Transformer-based |

### Face Recognition

| Model | LFW Accuracy | Speed | Features |
|-------|--------------|-------|----------|
| **InsightFace (ArcFace)** | 99.83% | 10ms | Industry standard |
| **DeepFace** | 99.65% | 15ms | Easy integration |
| **FaceNet** | 99.63% | 12ms | Google, well-documented |
| **RetinaFace** | Detection + landmarks | 30ms | Accurate detection |

---

## Speech & Audio Models

### Speech-to-Text

| Model | WER (LibriSpeech) | Speed | Languages | Best For |
|-------|-------------------|-------|-----------|----------|
| **Whisper Large-v3** | 2.0% | 0.5x real-time | 99 | Best quality |
| **Whisper Medium** | 2.9% | 1x real-time | 99 | Balanced |
| **Whisper Small** | 3.4% | 2x real-time | 99 | Fast |
| **Whisper Tiny** | 5.6% | 4x real-time | 99 | Edge/mobile |
| **DeepSpeech** | 5.0% | 1x real-time | EN only | Lightweight |
| **Google Speech API** | ~2% | Real-time | 125+ | Managed, reliable |
| **AWS Transcribe** | ~3% | Real-time | 100+ | AWS ecosystem |

### Text-to-Speech

| Model | Quality | Speed | Voices | Best For |
|-------|---------|-------|--------|----------|
| **ElevenLabs** | Excellent | Fast | Cloning | Most realistic |
| **OpenAI TTS** | Very Good | Fast | 6 | Simple integration |
| **Coqui TTS** | Good | Medium | Many | Open source |
| **Google TTS** | Good | Fast | 200+ | Multi-language |
| **Amazon Polly** | Good | Fast | 60+ | AWS ecosystem |

---

## Embedding Models

### Text Embeddings

| Model | Dimensions | Speed | Quality | Cost |
|-------|------------|-------|---------|------|
| **text-embedding-3-large** | 3072 | Fast | Best | $0.13/1M tokens |
| **text-embedding-3-small** | 1536 | Very Fast | Good | $0.02/1M tokens |
| **text-embedding-ada-002** | 1536 | Fast | Good | $0.10/1M tokens |
| **sentence-transformers/all-MiniLM-L6** | 384 | Very Fast | Good | Free |
| **sentence-transformers/all-mpnet-base** | 768 | Fast | Very Good | Free |
| **Cohere embed-v3** | 1024 | Fast | Very Good | $0.10/1M tokens |

### Image Embeddings

| Model | Dimensions | Use Case |
|-------|------------|----------|
| **CLIP ViT-B/32** | 512 | Text-image matching |
| **CLIP ViT-L/14** | 768 | Higher quality |
| **DINOv2** | 384-1536 | Visual similarity |
| **ResNet-50 features** | 2048 | Image retrieval |

---

## Structured Data Models

### Tabular/Regression

| Model | Type | Best For | Training Speed |
|-------|------|----------|----------------|
| **XGBoost** | Gradient Boosting | General tabular | Fast |
| **LightGBM** | Gradient Boosting | Large datasets | Very Fast |
| **CatBoost** | Gradient Boosting | Categorical features | Fast |
| **Random Forest** | Ensemble | Baseline, interpretable | Medium |
| **TabNet** | Deep Learning | End-to-end learning | Slow |

### Time Series

| Model | Type | Best For |
|-------|------|----------|
| **Prophet** | Additive | Business metrics, seasonality |
| **ARIMA** | Statistical | Short-term, stationary |
| **LSTM** | Deep Learning | Complex patterns |
| **Temporal Fusion Transformer** | Deep Learning | Multi-horizon |
| **N-BEATS** | Deep Learning | Univariate forecasting |

### Recommendation Systems

| Model | Type | Best For |
|-------|------|----------|
| **Two-Tower** | Neural | Large-scale retrieval |
| **Matrix Factorization** | Collaborative | Simple, interpretable |
| **Wide & Deep** | Hybrid | Google-style recommendations |
| **BERT4Rec** | Sequential | Session-based |
| **Graph Neural Networks** | Graph | Social/network data |

---

## Model Optimization Techniques

### Quantization Comparison

| Technique | Model Size | Speed | Accuracy Loss | VRAM |
|-----------|------------|-------|---------------|------|
| **FP32 (baseline)** | 100% | 1x | 0% | 100% |
| **FP16** | 50% | 1.5-2x | < 0.1% | 50% |
| **INT8** | 25% | 2-3x | 0.5-1% | 25% |
| **INT4** | 12.5% | 3-4x | 1-3% | 12.5% |
| **GPTQ** | 12.5% | 2-3x | 0.5-2% | 12.5% |
| **AWQ** | 12.5% | 3-4x | 0.3-1% | 12.5% |

### Framework Selection

| Framework | Best For | Deployment |
|-----------|----------|------------|
| **PyTorch** | Research, flexibility | TorchServe, ONNX |
| **TensorFlow** | Production, enterprise | TF Serving, TFLite |
| **JAX** | Research, TPU | FLAX, Orbax |
| **ONNX** | Cross-platform | ONNX Runtime |
| **TensorRT** | NVIDIA optimization | Maximum GPU perf |

---

## Cost-Performance Matrix

### LLM Cost per 1M Tokens

| Model | Input | Output | Quality Score |
|-------|-------|--------|---------------|
| GPT-4 Turbo | $10 | $30 | 95 |
| GPT-4o | $5 | $15 | 93 |
| Claude 3 Opus | $15 | $75 | 96 |
| Claude 3.5 Sonnet | $3 | $15 | 92 |
| Claude 3 Haiku | $0.25 | $1.25 | 82 |
| GPT-3.5 Turbo | $0.50 | $1.50 | 78 |
| Llama 3 70B (self) | ~$0.10 | ~$0.10 | 88 |

### GPU Cost per Hour

| GPU | Cloud Cost/hr | VRAM | Best For |
|-----|---------------|------|----------|
| T4 | $0.35-0.50 | 16GB | Inference, small models |
| A10G | $1.00-1.50 | 24GB | Medium models |
| A100 40GB | $3.00-4.00 | 40GB | Training, large models |
| A100 80GB | $4.00-5.00 | 80GB | Very large models |
| H100 | $8.00-12.00 | 80GB | Cutting edge |

---

## Quick Decision Tables

### "I need to classify images"

| Your Situation | Recommendation |
|----------------|----------------|
| Mobile/edge deployment | EfficientNet-B0, MobileNetV3 |
| General web app | ResNet-50, EfficientNet-B4 |
| Need best accuracy | ConvNeXt-Large, ViT-L |
| Custom domains | Fine-tune EfficientNet-B4 |

### "I need to detect objects"

| Your Situation | Recommendation |
|----------------|----------------|
| Real-time video | YOLOv8-n or YOLOv8-s |
| Security/surveillance | YOLOv8-m + DeepSORT tracking |
| High accuracy needed | YOLOv8-x or RT-DETR |
| Edge deployment | YOLOv8-n + TensorRT |

### "I need text generation"

| Your Situation | Recommendation |
|----------------|----------------|
| Best quality, no budget limit | GPT-4 / Claude Opus |
| Good quality, cost-conscious | Claude Sonnet / GPT-4o |
| High volume, simple tasks | GPT-3.5 / Claude Haiku |
| Data privacy required | Llama 3 / Mistral (self-hosted) |
| Offline/air-gapped | Llama 3 8B quantized |
