import glob
import os

import pytest

path_output_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')


@pytest.fixture()
def clear_dir():
    """Fixture: delete all files from dir with archive"""
    all_files = os.path.join(path_output_files, '*.*')
    for file in glob.glob(all_files):
        os.remove(file)
