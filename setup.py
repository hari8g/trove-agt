from setuptools import setup, find_packages

setup(
    name="trove-agt",
    version="0.2.0",
    author="Hariprasad G",
    author_email="your.email@example.com",
    description="Trove - AI agent framework",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        "fastapi",
        "uvicorn",
        "pyyaml"
    ],
)
