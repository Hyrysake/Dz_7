from setuptools import setup

setup(
    name="clean_folder",
    version="0.1",
    description="A utility package for folder operations",
    author="GO_IT",
    packages=["clean_folder"],
    entry_points={
        "console_scripts": [
            "clean-folder = clean_folder.clean:main"
        ]
    },
)
