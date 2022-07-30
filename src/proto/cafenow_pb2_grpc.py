# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.cafenow_pb2 as cafenow__pb2


class CafenowAgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.handleProcess = channel.unary_unary(
                '/cafenow.grpc.CafenowAgent/handleProcess',
                request_serializer=cafenow__pb2.BasicVO.SerializeToString,
                response_deserializer=cafenow__pb2.BasicVO.FromString,
                )


class CafenowAgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def handleProcess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CafenowAgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'handleProcess': grpc.unary_unary_rpc_method_handler(
                    servicer.handleProcess,
                    request_deserializer=cafenow__pb2.BasicVO.FromString,
                    response_serializer=cafenow__pb2.BasicVO.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafenow.grpc.CafenowAgent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CafenowAgent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def handleProcess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafenow.grpc.CafenowAgent/handleProcess',
            cafenow__pb2.BasicVO.SerializeToString,
            cafenow__pb2.BasicVO.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
