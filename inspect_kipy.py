import kipy.proto.common.commands as cmds
from kipy.proto.common.types import base_types_pb2
from kipy.proto.common.types.enums_pb2 import KiCadObjectType
import google.protobuf.any_pb2

def print_message_fields(msg_class):
    print(f"--- {msg_class.__name__} ---")
    for field in msg_class.DESCRIPTOR.fields:
        print(f"  {field.name} ({field.type})")

print_message_fields(cmds.CreateItems)
print_message_fields(cmds.UpdateItems)
print_message_fields(cmds.GetItems)
