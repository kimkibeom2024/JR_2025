# Jetson Nano ONNX-Runtime-GPU & TensorRT 설치 가이드

이 가이드는 Jetson Nano에서 ONNX-Runtime-GPU와 TensorRT를 수동으로 다운로드하여 설치하는 방법을 설명합니다. Docker 이미지를 사용하지 않고 직접 설치하는 방법을 포함합니다.

## 📁 폴더 생성

먼저, 필요한 패키지 파일을 저장할 폴더를 생성합니다.

```bash
mkdir -p ~/jetson_pkgs && cd ~/jetson_pkgs
```

## 📦 패키지 파일 다운로드

### 1. ONNX-Runtime-GPU (1.8.0)

```bash
wget https://nvidia.box.com/shared/static/gjqofg7rkg97z3gc8jeyup6t8n9j8xjw.whl -O onnxruntime_gpu-1.8.0-cp38-cp38-linux_aarch64.whl
```

### 2. TensorRT (8.2.0.6)

```bash
wget https://forums.developer.nvidia.com/uploads/short-url/hASzFOm9YsJx6VVFrDW1g44CMmv.whl -O tensorrt-8.2.0.6-cp38-none-linux_aarch64.whl
```

## 🛠 패키지 설치

### 1. ONNX-Runtime-GPU 설치

```bash
pip install ./onnxruntime_gpu-1.8.0-cp38-cp38-linux_aarch64.whl
```

### 2. TensorRT 설치

```bash
pip install ./tensorrt-8.2.0.6-cp38-none-linux_aarch64.whl
```

## ✅ 설치 확인

설치된 패키지 버전을 확인하여 제대로 설치되었는지 확인합니다.

```bash
python3 -c "import onnxruntime; print('ONNX Runtime:', onnxruntime.__version__)"
python3 -c "import tensorrt; print('TensorRT:', tensorrt.__version__)"
```

## 🧹 파일 정리 (선택)

다운로드된 **.whl** 파일을 삭제하거나 보관할 폴더로 이동합니다.

```bash
rm -rf ~/jetson_pkgs/*.whl
```

## ⚙️ 최적화 (선택)

NVIDIA의 기본 설정을 최적화하여 성능을 향상시킬 수 있습니다.

```bash
export NVIDIA_TF32_OVERRIDE=0
```

## 🚀 마무리

이제 Jetson Nano에서 ONNX-Runtime-GPU와 TensorRT가 성공적으로 설치되었습니다. 모델 변환 및 추론 테스트를 진행할 준비가 완료되었습니다.
