import pyaml_env
import pydantic

from check_links.content import ContentConfig

# Create a pydantic model with pyyaml_env with an overloaded __init__ method that takes a config.yaml file path argument


class Config(pydantic.BaseModel):
    content: ContentConfig

    def __init__(self, config_path: str):
        super().__init__(**pyaml_env.parse_config(config_path))
