# {{cookiecutter.project_slug }}

{{cookiecutter.project_desc }}

[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/)
[![Keras](https://img.shields.io/badge/keras-2.4.3-blue)](https://keras.io/)

It provides the loss function and callbacks to apply to keras models


## Usage

To use {{cookiecutter.project_slug }}, follow these steps:

```bash
    pip install {{cookiecutter.project_slug }}
```

Since Aquitable is based on keras-core you can choose which backend to use, otherwise it will default to tensorflow.
To change backend change the ```KERAS-BACKEND``` enviromental variable. Follow [this](https://keras.io/keras_core/#configuring-your-backend).

To get an arquiteture you only need to have a simple configuration and call the module:

```python
# Previous code and imports
...
from {{cookiecutter.project_slug }} import losses, callbacks

# Based on {{cookiecutter.project_slug }} StackedCNN


loss_funtion=losses.weighted_loss
callback = callbacks.StopOnNanLoss

StackedCNN.compile(loss=loss_funtion)

StackedCNN.fit(
    ...
    callbacks=callback
)


```

## [Contribution](CONTRIBUTING.md)

Contributions to {{cookiecutter.project_slug }} are welcome! If you find any issues or have suggestions for improvement, please feel free to contribute. Make sure to update tests as appropriate and follow the contribution guidelines.

## License

{{cookiecutter.project_slug }} is licensed under the MIT License, which allows you to use, modify, and distribute the package according to the terms of the license. For more details, please refer to the [LICENSE](LICENSE) file.
