# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import mlchain_pb2 as mlchain__pb2


class MLChainServiceStub(object):
  """Service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.get_params = channel.unary_unary(
        '/MLChainService/get_params',
        request_serializer=mlchain__pb2.String.SerializeToString,
        response_deserializer=mlchain__pb2.Byte.FromString,
        )
    self.des_func = channel.unary_unary(
        '/MLChainService/des_func',
        request_serializer=mlchain__pb2.String.SerializeToString,
        response_deserializer=mlchain__pb2.Byte.FromString,
        )
    self.ping = channel.unary_unary(
        '/MLChainService/ping',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=mlchain__pb2.Byte.FromString,
        )
    self.description = channel.unary_unary(
        '/MLChainService/description',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=mlchain__pb2.Byte.FromString,
        )
    self.list_all_function = channel.unary_unary(
        '/MLChainService/list_all_function',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=mlchain__pb2.Byte.FromString,
        )
    self.list_all_function_and_description = channel.unary_unary(
        '/MLChainService/list_all_function_and_description',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=mlchain__pb2.Byte.FromString,
        )
    self.call = channel.unary_unary(
        '/MLChainService/call',
        request_serializer=mlchain__pb2.Message.SerializeToString,
        response_deserializer=mlchain__pb2.Output.FromString,
        )


class MLChainServiceServicer(object):
  """Service definition
  """

  def get_params(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def des_func(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def description(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def list_all_function(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def list_all_function_and_description(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MLChainServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'get_params': grpc.unary_unary_rpc_method_handler(
          servicer.get_params,
          request_deserializer=mlchain__pb2.String.FromString,
          response_serializer=mlchain__pb2.Byte.SerializeToString,
      ),
      'des_func': grpc.unary_unary_rpc_method_handler(
          servicer.des_func,
          request_deserializer=mlchain__pb2.String.FromString,
          response_serializer=mlchain__pb2.Byte.SerializeToString,
      ),
      'ping': grpc.unary_unary_rpc_method_handler(
          servicer.ping,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=mlchain__pb2.Byte.SerializeToString,
      ),
      'description': grpc.unary_unary_rpc_method_handler(
          servicer.description,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=mlchain__pb2.Byte.SerializeToString,
      ),
      'list_all_function': grpc.unary_unary_rpc_method_handler(
          servicer.list_all_function,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=mlchain__pb2.Byte.SerializeToString,
      ),
      'list_all_function_and_description': grpc.unary_unary_rpc_method_handler(
          servicer.list_all_function_and_description,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=mlchain__pb2.Byte.SerializeToString,
      ),
      'call': grpc.unary_unary_rpc_method_handler(
          servicer.call,
          request_deserializer=mlchain__pb2.Message.FromString,
          response_serializer=mlchain__pb2.Output.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MLChainService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
