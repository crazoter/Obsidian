#speech-to-speech #NLP

#### Page 2

> How is textless NLP different?  (p. 2) 

> In the past, connecting an NLP application (https://analyticsindiamag.com/ai-powered-audio- transcription-tools-to-check-out-in-2021/) to speech inputs meant that researchers had to first train an automatic speech recognition (ASR) system. It is often a resource-intensive operation as it introduces errors, encodes casual linguistic interactions poorly, and is available for just a handful of languages. With textless NLP, the researchers are making ASR obsolete and work in an end-to-end fashion, from the speech input to speech outputs.  (p. 2) 

> An encoder that converts ‘speech’ into ‘discrete units’ that frequently represent recurring sounds in spoken language (S2u)  An autoregressive, unit-based language model that is trained to predict the next discrete unit based on what it has seen before (pseudo-text) A decoder that converts units into speech (u2S) (p. 2) 

> The baseline GSLM consists of three parts:  (p. 2) 

> Researchers can train models on audio-�rst experiences like podcasts, radio shows, and social audio apps without annotation or training an ASR. It opens up the possibility of a set of applications never seen before, including online expressive translation https://arxiv.org/pdf/2107.05604.pdf (p. 2) 

---
#### Page 3

> r1CfnU4Pk7psSZ2DCAfzMFKGdUWsFrjiQ5dhlwel59NaaKHd8VGS7XRYePB- OAi6yj5wu4QRiQrpsCK4AAb4ry-SZUTgep6vGRsT) for multilingual video games, content search, and summarisation from archived audio.  (p. 3) 

> In the research paper ‘On generative spoken language modelling from raw audio (https://arxiv.org/pdf/2102.01192.pdf),” Facebook AI researchers tested three SOTA encoders, namely [CPC (https://github.com/facebookresearch/CPC_audio)](https://github.com/facebookresearch/CPC_audio), wav2vec 2.0 (https://github.com/mailong25/self-supervised-speech-recognition), and HuBERT (https://github.com/pytorch/fairseq/tree/master/examples/hubert?fbclid=IwAR30g8-8_yJpIePXynwouB1nQOtem0vzeJGJvKNiGrd55wIGNBMB5Rw_gZA), followed by k-means clustering and deduplication (removing successive identical units). Plus, they have used a standard causal ‘transformer’ for language modelling and[ Tacotron 2 (https://github.com/NVIDIA/tacotron2)](https://github.com/NVIDIA/tacotron2), a standard text-to-speech system, as a (p. 3) 

> In terms of use cases, Facebook researchers have developed the �rst audio-only speech-to-speech translation system (https://arxiv.org/pdf/2107.05604.pdf). In the coming months, the researchers plan to address textless versions of standard NLP tasks (https://analyticsindiamag.com/new-ai-framework-can-translate-multimodal-inputs-including-video-to-natural-language/), such as sentiment analysis, (https://analyticsindiamag.com/with-ai-translation-tech-you-may-soon-be-able-to-talk-to-your-pets/) document retrieval, summarization, (p. 3) 

---
#### Page 4

> There is a similar trend at the linguistic level, but using too many units in certain areas becomes detrimental.  (p. 4) 

> Different encoders produced very different outcomes (HuBERT provided the best overall result). 4. Autonomic generation metrics correlate well with people. (p. 4) 

> Additional research  In addition to this, Facebook researchers in a paper ‘text-free Prosody-Aware Generative Spoken Language Modeling (https://arxiv.org/abs/2109.03264)‘, presented a prosody-aware generative spoken language model (pGSLM). This new model comprises a multi- stream transformer language model (MS-TLM) of speech, represented as a discovered unit and prosodic feature streams, and an adapted HiFi-GAN model converting MS-TLM outputs to waveforms.  (p. 4) 

---
#### Page 5

> Wrapping Facebook researchers said that it would continue to apply GSLM to casual and spontaneous speech and dialogue datasets, where text-based methods and ASR struggle most. In addition, the team believes that their GSLM can be an effective method (https://analyticsindiamag.com/how-to-identify-entities-in-nlp/) for pretraining downstream tasks (p. 5) 

---
