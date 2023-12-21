import subprocess
import sys
from odm_cli_java_integration.find_modules import _find_dummy_java_module


def launch():
    jar_path = _find_dummy_java_module()
    try:
        params = sys.argv
        params.pop(0)
        jar_args = ["java", "-jar", jar_path]
        jar_args.extend(params)
        output = subprocess.check_output(jar_args)
        print(str(output))
    except Exception as e:
        print("An error has occurred")

if __name__ == "__main__":
    launch()