# dev_PythonML
PythonML Developments

##### Check Hardware GPU (NVIDIA)
```
$lspci | grep -i nvidia
```
![https://github.com/lel99999/dev_PythonML/blob/master/lspci-01.png](https://github.com/lel99999/dev_PythonML/blob/master/lspci-01.png) <br/>

##### GPU Specs: NVIDA CUDA Specs - CUDA 10.2
![https://github.com/lel99999/dev_PythonML/blob/master/nvidia-smi-03.png](https://github.com/lel99999/dev_PythonML/blob/master/nvidia-smi-03.png) <br/>

##### Python - Tensorflow2 and Keras
- Install GPU Supported
  `$pip install tensorflow-gpu`

  - Test Python Code:
    ```
    import tensorflow as tf
    
    tf.__versions__
  ```
