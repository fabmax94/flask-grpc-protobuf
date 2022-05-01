import logging

import grpc
from messages import recipe_pb2
from messages import recipe_pb2_grpc


def get_recipe(id: int):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = recipe_pb2_grpc.RecipeStub(channel)
        response = stub.GetRecipe(recipe_pb2.RecipeRequest(id=id))
    print("Recipe: " + response.title)


if __name__ == '__main__':
    logging.basicConfig()
    get_recipe(0)
