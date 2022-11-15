import pathlib

import pandas as pd
import pydantic


class ContentConfig(pydantic.BaseModel):
    path: pathlib.Path
    allowed_extensions: list[str] = ["*.*"]
    excluded_paths: list[str] = []

    def __init__(self, **data):
        data["path"] = pathlib.Path(data["path"])
        super().__init__(**data)

    @pydantic.validator("path")
    def path_must_exist(cls, v):
        if not v.exists():
            raise ValueError(f"Path does not exist: {v}")
        return v

    @pydantic.validator("path")
    def dir_not_empty(cls, v):
        if not list(v.iterdir()):
            raise ValueError(f"Path is empty: {v}")
        return v


class Content:
    def __init__(self, config: ContentConfig):
        self._config = config

    @property
    def config(self):
        return self._config

    @property
    def files(self):
        return list(self.get_files())

    def get_files(self):
        df_files = self.get_paths()
        df_files = df_files[df_files["is_file"]]
        df_files = df_files[df_files["extension"].isin(self.config.allowed_extensions)]
        df_files = df_files[
            ~df_files["path"].apply(
                lambda x: any([y in str(x) for y in self.config.excluded_paths])
            )
        ]
        return df_files["path"]

    def get_paths(self):
        df = pd.DataFrame(
            [
                (path, path.is_file(), path.suffix, path.parts)
                for path in self.config.path.rglob("*")
            ],
            columns=["path", "is_file", "extension", "parts"],
        )
        return df
