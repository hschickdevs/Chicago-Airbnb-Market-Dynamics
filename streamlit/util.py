
from os.path import join, dirname, isdir, abspath
from os import getenv, getcwd, mkdir
from dotenv import load_dotenv, find_dotenv

ENVARS = ["SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_ACCOUNT", "SNOWFLAKE_DATABASE", "SNOWFLAKE_SCHEMA"]
    
    
def handle_env():
    """Checks if the .env file exists in the current working dir, and imports the variables if so"""
    try:
        envpath = find_dotenv(raise_error_if_not_found=True, usecwd=True)
        load_dotenv(dotenv_path=envpath)
    except:
        pass
    finally:
        for var in ENVARS:
            val = getenv(var)
            if val is None:
                raise ValueError(f"Missing environment variable: {var}")