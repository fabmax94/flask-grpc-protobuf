import logging

import grpc
from concurrent import futures
import messages.recipe_pb2_grpc as recipe_service
from services.recipe import RecipeService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recipe_serve = RecipeService()
    recipe_service.add_RecipeServicer_to_server(recipe_serve, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
