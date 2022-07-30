from concurrent import futures
import threading

import grpc
from proto.cafenow_pb2 import BasicVO 
import proto.cafenow_pb2_grpc as pb2_grpc

SERVER_PORT = 40080


class CafenowServicer(pb2_grpc.CafenowAgentServicer):
    def handleProcess(self, request, context):
        print(request)
        return BasicVO(api_type="handleProcess", message="SUCCESS")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CafenowAgentServicer_to_server(CafenowServicer(), server)
    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    server.start()
    server.wait_for_termination()

# request
def requestGrpc():
    ip_to_connect = "localhost"
    try:
        with grpc.insecure_channel(f"{ip_to_connect}:{SERVER_PORT}") as channel:
            stub = pb2_grpc.CafenowAgentStub(channel)
            response = stub.handleProcess(BasicVO(api_type="handleProcess", message="SUCCESS"))
            return response
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # grpc 스타드
    grpc_thread = threading.Thread(target=serve)
    grpc_thread.start()  
    import time
    time.sleep(3)
    requestGrpc()

    