import Desmos

api = Desmos.API()
api.SetExpression("1", "y=mx+b")
api.Compile("index.html")