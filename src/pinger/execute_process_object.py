import subprocess


def execute_process_object(world: int, logger, process):
    try:
        ping_out, _ = process.communicate()
        return ping_out

    except subprocess.CalledProcessError as ex:
        logger.error('An exception occured when executing process %s', ex)
