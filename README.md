# LLM Misin Nesin Ya

Kişisel öğrenme projesi: LLM'in içini (tokenization, model mimarisi, eğitim) sıfırdan anlamak,
öğrenirken paralelde küçük bir modeli ESP32 üzerinde çalışacak şekilde geliştirmek.

## Hedef

- LLM temellerini pratik yaparak öğrenmek: tokenization, embedding, attention, eğitim döngüsü.
- Öğrenirken aynı anda gerçek bir hedefe doğru inşa etmek: ESP32-S3 (PSRAM'li) üzerinde çalışacak,
  çok küçük parametreli (TinyStories/llama2.c tarzı, ~260K–15M parametre) bir dil modeli.
- Eğitim PC'de (CUDA GPU) yapılacak, ESP32'de yalnızca çıkarım (inference) çalışacak.

## Yaklaşım

Sabit bir plan/roadmap dosyası bilinçli olarak tutulmuyor: bir yandan öğrenip bir yandan
geliştirmek akışkan bir süreç, konular ilerledikçe şekilleniyor. Her oturumda ne öğrenildiği ve
ne yapıldığı `egitim/` altındaki notebook'larda ve kod dosyalarında kalıyor.

## Klasör yapısı

- `egitim/` — öğrenme notebook'ları ve destek kodu.
  - `day1.ipynb` — tokenizer temelleri: boşluk-bazlı basit tokenizer, sabit sözlük (vocab) ile
    id↔token dönüşümü, tiktoken (`cl100k_base`) ve Qwen3 tokenizer karşılaştırması, Türkçe
    tokenizer makale notları.
  - `tokenizer.py` — notebook'taki tokenizer mantığının sınıf haline getirilmiş ilk hali (vocab
    dosyasından yükleme; henüz erken aşamada).
- `.venv/` — proje ortamı, `--system-site-packages` ile açıldı (sistemdeki torch'u tekrar
  indirmeden kullanıyor).

## Ortam kurulumu

```bash
python3 -m venv --system-site-packages .venv
.venv/bin/pip install ipykernel transformers torch tiktoken datasets matplotlib
.venv/bin/python -m ipykernel install --user --name llm_misin_nesin_ya \
    --display-name "Python (llm_misin_nesin_ya)"
```

Kurulu sürümler: torch 2.11.0+cu130 (CUDA), transformers 5.17.0, tiktoken 0.14.0,
datasets 5.0.1, matplotlib 3.10.8, ipykernel 7.3.0.

VS Code'da notebook kernel'i: **Python (llm_misin_nesin_ya)**.

## Şu ana kadar öğrenilenler / yapılanlar

- Basit boşluk-bazlı tokenizer, sabit vocab ile id↔token dönüşümü (encode/decode), `<unk>` fallback.
- tiktoken (`cl100k_base`) ile karşılaştırma.
- Qwen3-0.6B tokenizer'ının HuggingFace'ten çekilmesi (`AutoTokenizer.from_pretrained`).
- Türkçe tokenizer makalesi ([arxiv 2502.07057](https://arxiv.org/pdf/2502.07057)) okundu, notlar
  `day1.ipynb` içinde: token saflığı (%Pure), dile özgü token yüzdesi (%TR), sözlük boyutu
  dengesi, TR-MMLU, Selective Language Modeling (SLM).

## Sıradaki adımlar (açık, sabitlenmemiş)

- Gerçek bir tokenizer eğitimi (BPE) denemek, Türkçe metin üzerinde.
- Küçük bir transformer mimarisi kurup eğitim döngüsünü yazmak.
- ESP32-S3 için bellek/hız bütçesini hesaplamak, quantization (INT8/INT4) planlamak.
