# Desmos.py
Desmos.py is a python API that provides intergration between Desmos Graphing Calculator and Python.

## Why
Desmos's offical API is currently supported in only javascript, making intergration between Python and Desmos more tricky.

## Examples
```python
import Desmos

api = Desmos.API()
api.SetExpression("1", "y=mx+b")
api.SetExpressionNote("2", "This is a note!")
api.Compile("index.html")
```