from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RequestPayloadModel(object):
    name: str
    job: str

    # @staticmethod
    # def get_serialize_json_string() -> str:
    #     obj_payload = RequestPayloadModel('sj', 350000, 35)
    #     print(obj_payload)
    #     json_string = obj_payload.to_json()
    #     return json_string
