import os
from importlib.util import find_spec
import glob

def _contains_jar(path):
    jar_file = path + "/odm-cli-*.jar"
    jar_file_matches = glob.glob(jar_file)
    if len(jar_file_matches) > 0:
        return jar_file_matches[0]
    else:
        return None

def _find_dummy_java_module():
    try:
        current_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
        source_dir = os.path.abspath(current_dir + "/../../")
        build_target = glob.glob(source_dir + "odm-cli/target/")
        if len(build_target) > 0:
            jar_path = _contains_jar(build_target[0])
            if jar_path != None:
              return jar_path

        module_home = os.path.dirname(find_spec("odm_cli").origin)

        jar_path = _contains_jar(module_home + "/jars")
        if jar_path != None:
            return jar_path
    except Exception as e:
        pass
    print("Could not find valid jar in current environment.")