import grpc
import payloadresponse_pb2_grpc
import payloadresponse_pb2
import os
from flask import jsonify
def remote_procedure_call(images):
    img_1 = images[0]
    img_2 = images[1]
    # get both the images
    # this is just because in case if we start the application with docker compose then we cant access the server with
    # localhost we need to provide the service name
    # so passed a ENV var if it runs in docker
    server_url = 'server:4001' if 'USING_DOCKER' in os.environ else '127.0.0.1:4001'
    with grpc.insecure_channel(server_url) as channel:
        # get the service from server
        stub = payloadresponse_pb2_grpc.ImageSimilarityServiceStub(channel)
        # make an RPC Hurrayyyyyyy!!!!!!!
        response = stub.image_similarity(payloadresponse_pb2.Payload(image_url1=img_1, image_url2=img_2))
        # the server send the reponse
        return {
            "status": True,
            "score": response.image_similarity_score,
            "img_1": response.image_url1,
            "img_2": response.image_url2
        }
    return {
        'status': False,
        'message': 'Error occured while comparing images'
    }