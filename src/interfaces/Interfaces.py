import jsonpickle


class ResponseInterface:
  def deserialize(self, json_str: str) -> object:
    return jsonpickle.decode(string=json_str)


class RequestInterface:
  def serialize(self) -> dict | None:
    return jsonpickle.encode(self, unpicklable=False)
