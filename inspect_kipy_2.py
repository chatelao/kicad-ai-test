import kipy.proto.common.commands as cmds
from kipy.proto.common.types import base_types_pb2, enums_pb2
import google.protobuf.any_pb2

def inspect_any(any_msg):
    print(f"Any type_url: {any_msg.type_url}")

print_message_fields = lambda msg_class: [print(f"  {f.name} ({f.type})") for f in msg_class.DESCRIPTOR.fields]

print("--- CreateItemsResponse ---")
print_message_fields(cmds.CreateItemsResponse)
