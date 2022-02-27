# from src.aa.a import Producer
# from src.bb.b import Consumer
from src.bb.b import Consumer
from src.aa.a import Producer
from enum import Enum
class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3

def search(data, anns_field, param, limit, expr=None, partition_names=None,
               output_fields=None, timeout=None, round_decimal=-1, **kwargs):
    print("data", data)
    print("anns_field", anns_field)
    print("param", param)
    print("limit", limit)
    print("expr", expr)
    print("partition_names", partition_names)
    print("output_fields", output_fields)
    print("timeout", timeout)
    print("round_decimal", round_decimal)
    print("kwargs", kwargs)
    travel_timestamp = kwargs.get("travel_timestamp", 0),
    print("travel_timestamp", travel_timestamp)
    guarantee_timestamp = kwargs.get("guarantee_timestamp", 0)
    print("guarantee_timestamp", guarantee_timestamp)
    consistency_level = kwargs.get("consistency_level")
    print("consistency_level", consistency_level)
    print(consistency_level == Color.GREEN)
    print(Color.GREEN)


search_param = {
            "data": [[1.0, 1.0]],
            "anns_field": "films",
            "param": {"metric_type": "L2"},
            "limit": 2,
            "expr": "film_id > 0",
            }
# search(**search_param)
# search([[1.0, 1.0]], "films", {"metric_type": "L2"}, 2, **{"consistency_level":2})
search([[1.0, 1.0]], "films", {"metric_type": "L2"}, 2, **{"consistency_level":Color.GREEN})

# if __name__ == "__main__":
#     p = Producer()
#     print("p", p.get_name())
#     c = Consumer()
#     print(c.get_name())
