1. 다운로드 링크 확인 (필수)
ONNX Runtime GPU 1.8.0
onnxruntime_gpu-1.8.0-cp38-cp38-linux_aarch64.whl

TensorRT 8.2.0.6
tensorrt-8.2.0.6-cp38-none-linux_aarch64.whl

2. 파일 다운로드 (필수)
작업 디렉토리 이동:
mkdir -p ~/jetson_pkgs && cd ~/jetson_pkgs

파일 다운로드:
```
wget https://nvidia.box.com/shared/static/gjqofg7rkg97z3gc8jeyup6t8n9j8xjw.whl -O onnxruntime_gpu-1.8.0-cp38-cp38-linux_aarch64.whl
wget https://forums.developer.nvidia.com/uploads/short-url/hASzFOm9YsJx6VVFrDW1g44CMmv.whl -O tensorrt-8.2.0.6-cp38-none-linux_aarch64.whl
```

3. 패키지 설치 (필수)
onnxruntime-gpu 설치:
```
pip install ./onnxruntime_gpu-1.8.0-cp38-cp38-linux_aarch64.whl
```

TensorRT 설치:
```
pip install ./tensorrt-8.2.0.6-cp38-none-linux_aarch64.whl
```

4. 설치 확인 (필수)
각 패키지가 정상적으로 설치되었는지 확인:
```
python3 -c "import onnxruntime; print('ONNX Runtime:', onnxruntime.__version__)"
python3 -c "import tensorrt; print('TensorRT:', tensorrt.__version__)"
```

5. 파일 정리 (선택)
다운로드된 .whl 파일을 삭제하거나 보관할 폴더로 이동:
```
rm -rf ~/jetson_pkgs/*.whl
```

6. 최적화 (선택)
NVIDIA_TF32_OVERRIDE 환경 변수 설정:
```
export NVIDIA_TF32_OVERRIDE=0
```
