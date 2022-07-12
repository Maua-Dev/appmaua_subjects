import os
import shutil

LAMBDA_LAYER_OUTPUT = "lambda_layer_out"


def load_lambda_layer_output() -> None:
    """
    Craetes a folder for the lambda layer output with the ["domain", "external", "infra", "helpers"] directories from src.
    """
    root_dir = "\\".join(os.getcwd().split("\\")[:-1])
    lambda_layer_directories = ["domain", "external", "infra", "helpers"]


    # creates the directory "LAMBDA_LAYER_OUTPUT/python"
    if os.path.exists(LAMBDA_LAYER_OUTPUT):
        shutil.rmtree(LAMBDA_LAYER_OUTPUT)
    os.makedirs(LAMBDA_LAYER_OUTPUT)
    os.mkdir(LAMBDA_LAYER_OUTPUT + "\\" + "python")

    ## STEP 1 - CREATE LAYER FOR APPLICATION SHARED FILES

    # Copy the directories from src to the lambda layer output
    for dir in lambda_layer_directories:
        shutil.copytree(src=os.path.join(root_dir, f"src/{dir}"), dst=f"{LAMBDA_LAYER_OUTPUT}/application/python/src/{dir}")

    # create a __init__.py file and copy envs.py in the lambda layer output directory
    open(f"{LAMBDA_LAYER_OUTPUT}/application/python/src/__init__.py", "w").close()
    shutil.copy(os.path.join(root_dir, "src/envs.py"), f"{LAMBDA_LAYER_OUTPUT}/application/python/src/envs.py")

    # zip the lambda layer output directory
    shutil.make_archive("lambda_layer", 'zip', os.path.join(LAMBDA_LAYER_OUTPUT, "application"))


    ## STEP 2 - CREATE LAYER FOR APPLICATION REQUIREMENTS
    os.mkdir(LAMBDA_LAYER_OUTPUT + "\\" + "requirements")

    # Copy the directories from root/venv/lib/site-packages/ to the lambda layer output
    shutil.copytree(src=os.path.join(root_dir, "venv\\lib\\site-packages"), dst=f"{LAMBDA_LAYER_OUTPUT}/requirements/python/")
    shutil.make_archive("lambda_layer_requirements", 'zip', os.path.join(LAMBDA_LAYER_OUTPUT, "requirements"))

    # clears the lambda layer output directory
    shutil.rmtree(LAMBDA_LAYER_OUTPUT)

    print("Lambda layer output created successfully 🐤")

if __name__ == "__main__":
    load_lambda_layer_output()
    # print("Lambda layer output created.")
