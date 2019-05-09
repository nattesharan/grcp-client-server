import payloadresponse_pb2_grpc
import payloadresponse_pb2
import grpc
from concurrent import futures
import time
from utils import fetch_similarity_score

# this is basically a class which holds the all the services which are mentioned in the protofile
class ServiceListener(payloadresponse_pb2_grpc.ImageSimilarityServiceServicer):
    def __init__(self, *args, **kwargs):
        # Here just like how we initialized message we can initialize db and all
        self.message = "Hello it works"

    # this is the service defined in the proto file
    def image_similarity(self, request, context):
        # all the attrs we send in the Payload message are available in the request
        similarity_score = fetch_similarity_score(request.image_url1, request.image_url2)
        # return the similarity score and image_urls back to the client as Response message
        return payloadresponse_pb2.Response(image_similarity_score=similarity_score, image_url1=request.image_url1,\
                                            image_url2=request.image_url2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    # create a server and bing it with the serviceListener
    payloadresponse_pb2_grpc.add_ImageSimilarityServiceServicer_to_server(ServiceListener(), server)
    # bind the port the server should run on
    server.add_insecure_port('[::]:4001')
    # start the server
    server.start()
    print("Grpc server started on Post 4001")
    try:
        while True:
            time.sleep(20)
    except KeyboardInterrupt:
        # stop the server
        server.stop(0)
        print("Server stopped gracefully")

if __name__ == "__main__":
    serve()
