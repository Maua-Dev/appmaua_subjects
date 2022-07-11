import os
import shutil

LAMBDA_LAYER_OUTPUT = "lambda_layer_out"


def load_lambda_layer_output() -> None:
    """
    Craetes a folder for the lambda layer output with the ["domain", "external", "infra", "helpers"] directories from src.
    """
    root_dir = "\\".join(os.getcwd().split("\\")[:-1])
    lambda_layer_directories = ["domain", "external", "infra", "helpers"]

    if os.path.exists(LAMBDA_LAYER_OUTPUT):
        shutil.rmtree(LAMBDA_LAYER_OUTPUT)

    os.makedirs(LAMBDA_LAYER_OUTPUT)

    for dir in lambda_layer_directories:
        shutil.copytree(src=os.path.join(root_dir, f"src/{dir}"), dst=f"{LAMBDA_LAYER_OUTPUT}/src/{dir}")

    open(f"{LAMBDA_LAYER_OUTPUT}/src/__init__.py", "w").close()