# SAGE-HLS
SAGE-HLS: Syntax-Aware AST-Guided LLM for High-Level Synthesis Code Generation

This repository contains the resources, code, and documentation supporting our work on training a model for HLS-C++ code generation. Our work demonstrates how to leverage transformer-based architectures for understanding and generating HLS code, with a focus on applications using Xilinx Vitis HLS tool.

## Model Details

- **Model Name:** [mashnoor/hls-vitis-ast-unverified-qwen-coder-7B](https://huggingface.co/mashnoor/hls-vitis-ast-unverified-qwen-coder-7B)
- **Base Architecture:** Qwen2.5-Coder-7B
- **Training Framework:** [Unsloth](https://github.com/unslothai/unsloth)

## Dataset

- **Dataset:** [mashnoor/hls-vitis-ast-unverified](https://huggingface.co/datasets/mashnoor/hls-vitis-ast-unverified)
- The dataset consists of HLS code samples, annotated with AST information, curated to support training and evaluation of code language models in the hardware design domain.

## Quick Start

1. **Open and run the notebook**
   - Open `run_model.ipynb` in [Google Colab](https://colab.research.google.com/), JupyterLab, or any compatible environment with GPU support.
   - The notebook will:
     - Install Unsloth.
     - Load the fine-tuned Qwen Coder 7B model from Hugging Face.
     - Provide a prompt template for HLS C++ code generation.
     - Run inference to generate HLS code based on Verilog module descriptions.

2. **Example Usage**

   The notebook includes a prompt template for translating Verilog module specifications into synthesizable HLS-C++ code. You can modify the prompt or input your own Verilog modules to generate corresponding HLS implementations.

   ```python
   # Example: Loading and running the model (see notebook for full details)
   from unsloth import FastLanguageModel
   model, tokenizer = FastLanguageModel.from_pretrained(
       model_name = "mashnoor/hls-vitis-ast-unverified-qwen-coder-7B",
       max_seq_length = 2048,
       load_in_4bit = True,
   )
   FastLanguageModel.for_inference(model)
   # ...see the notebook for prompt formatting and generation code
   ```


## Citation

If you use our model, dataset, or code, please cite our paper:

```bibtex

```

## License

This repository is released under the Apache License 2.0. See [LICENSE](LICENSE) for details.

## Acknowledgements

- [Unsloth](https://github.com/unslothai/unsloth) for efficient model fine-tuning.
- [Hugging Face](https://huggingface.co/) for model and dataset hosting.
