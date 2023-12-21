from future import standard_library
standard_library.install_aliases()
from builtins import *
from shutil import copytree, copy, rmtree
from setuptools import setup
import os
import sys
from distutils.command.build_ext import build_ext
import glob
from setuptools.command.install import install

def remove_if_exists(file_path):
    if os.path.exists(file_path):
        if os.path.islink(file_path) or os.path.isfile(file_path):
            os.remove(file_path)
        else:
            assert os.path.isdir(file_path)
            rmtree(file_path)


def find_file_path(pattern):
    files = glob.glob(pattern)
    if len(files) < 1:
        print("Failed to find the file %s." % pattern)
        exit(-1)
    if len(files) > 1:
        print("The file pattern %s is ambiguous: %s" % (pattern, files))
        exit(-1)
    return files[0]


current_dir = os.path.abspath(os.path.dirname(__file__))

JAR_PATH = "jars"

in_source_dir = os.path.isfile("../pom.xml")
try:
  if in_source_dir:
      try:
        os.mkdir(JAR_PATH)
      except:
        print("Jar path already exists {0}".format(JAR_PATH),
              file=sys.stderr)

      copy("../target/odm-cli-1.0.0.jar", os.path.join(JAR_PATH, "odm-cli-1.0.0.jar"))

  PACKAGES = ["odm_cli_java_integration", "odm_cli_java_integration.jars"]
  PACKAGE_DIR = {"odm_cli_java_integration.jars" : "jars"}
  PACKAGE_DATA = {"odm_cli_java_integration.jars" : ["*.jar"]}

  setup(
          name='odm-cli',
          version="1.0.0",
          packages=PACKAGES,
          include_package_data=True,
          package_dir=PACKAGE_DIR,
          package_data=PACKAGE_DATA,
          author='TEST',
          author_email='test@gmail.com',
          description='Hybrid python - java packaged code',
          python_requires='>=3.5',
          entry_points = {
          'console_scripts': ['odm-cli=odm_cli_java_integration.launcher:launch']
        },
          zip_safe=False,
          classifiers=[
              'Programming Language :: Python :: 3.8']
        
      )
finally:
    if in_source_dir:
      remove_if_exists(JAR_PATH)
    print("done")