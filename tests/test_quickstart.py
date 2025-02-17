import subprocess
import pytest
import utils


@pytest.mark.parametrize(
    "script_loc",
    [
        "./_includes/code/quickstart.autoschema.endtoend.py",
        "./_includes/code/quickstart.byov.all.py",
    ],
)
def test_py(empty_weaviates, script_loc):
    proc_script = utils.load_and_prep_script(script_loc)
    exec(proc_script)


@pytest.mark.parametrize(
    "script_loc",
    [
        "./_includes/code/quickstart.autoschema.endtoend.js",
    ],
)
def test_js(empty_weaviates, script_loc):
    temp_proc_script_loc = utils.load_and_prep_temp_file(script_loc)
    try:
        # If the script throws an error, this will raise a CalledProcessError
        subprocess.check_call(['node', temp_proc_script_loc])
    except subprocess.CalledProcessError as error:
        pytest.fail(f'Script {temp_proc_script_loc} failed with error: {error}')


@pytest.mark.parametrize(
    "script_loc",
    [
        "./_includes/code/quickstart.autoschema.endtoend.ts",
    ],
)
def test_ts(empty_weaviates, script_loc):
    temp_proc_script_loc = utils.load_and_prep_temp_file(script_loc, lang="ts")
    command = ["npx", "ts-node", "-O", '{ "module": "commonjs" }', temp_proc_script_loc]

    try:
        # If the script throws an error, this will raise a CalledProcessError
        subprocess.check_call(command)
    except subprocess.CalledProcessError as error:
        pytest.fail(f'Script {temp_proc_script_loc} failed with error: {error}')
