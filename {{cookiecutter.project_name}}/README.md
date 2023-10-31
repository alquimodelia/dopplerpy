# {{cookiecutter.module_name }}

{{cookiecutter.project_desc }}

[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/)
[![Keras](https://img.shields.io/badge/keras-2.4.3-blue)](https://keras.io/)

It provides the loss function and callbacks to apply to keras models


## Usage

To use {{cookiecutter.module_name }}, follow these steps:

```bash
    pip install {{cookiecutter.module_name }}
```

Since Aquitable is based on keras-core you can choose which backend to use, otherwise it will default to tensorflow.
To change backend change the ```KERAS-BACKEND``` enviromental variable. Follow [this](https://keras.io/keras_core/#configuring-your-backend).

To get an arquiteture you only need to have a simple configuration and call the module:

```python
# Previous code and imports
...
from {{cookiecutter.module_name }} import losses, callbacks

# Based on {{cookiecutter.module_name }} StackedCNN


loss_funtion=losses.weighted_loss
callback = callbacks.StopOnNanLoss

StackedCNN.compile(loss=loss_funtion)

StackedCNN.fit(
    ...
    callbacks=callback
)


```

## [Contribution](CONTRIBUTING.md)

Contributions to {{cookiecutter.module_name }} are welcome! If you find any issues or have suggestions for improvement, please feel free to contribute. Make sure to update tests as appropriate and follow the contribution guidelines.

## License

{{cookiecutter.module_name }} is licensed under the MIT License, which allows you to use, modify, and distribute the package according to the terms of the license. For more details, please refer to the [LICENSE](LICENSE) file.
