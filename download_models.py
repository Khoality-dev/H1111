import os

def download(url, save_path):
    os.system("wget " + url + " -O " + save_path)

def main():
    hunyuan_model_path = "hunyuan/"
    download(url="https://huggingface.co/maybleMyers/framepack_h1111/resolve/main/FramePackI2V_HY_bf16.safetensors?download=true", save_path = os.path.join(hunyuan_model_path, "FramePackI2V_HY_bf16.safetensors"))
    download(url="https://huggingface.co/maybleMyers/framepack_h1111/resolve/main/FramePack_F1_I2V_HY_20250503.safetensors?download=true", save_path = os.path.join(hunyuan_model_path, "FramePack_F1_I2V_HY_20250503.safetensors"))
    download(url="https://huggingface.co/maybleMyers/framepack_h1111/resolve/main/clip_l.safetensors?download=true", save_path = os.path.join(hunyuan_model_path, "clip_l.safetensors"))
    download(url="https://huggingface.co/maybleMyers/framepack_h1111/resolve/main/llava_llama3_fp16.safetensors?download=true", save_path = os.path.join(hunyuan_model_path, "llava_llama3_fp16.safetensors"))
    download(url="https://huggingface.co/maybleMyers/framepack_h1111/resolve/main/model.safetensors?download=true", save_path = os.path.join(hunyuan_model_path, "model.safetensors"))
    download(url="https://huggingface.co/maybleMyers/framepack_h1111/resolve/main/pytorch_model.pt?download=true", save_path = os.path.join(hunyuan_model_path, "pytorch_model.pt"))

if __name__ == '__main__':
    main()