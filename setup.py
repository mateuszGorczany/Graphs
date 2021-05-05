import setuptools

setuptools.setup(
    name="example-pkg-Autografy", # Replace with your own username
    version="0.0.1",
    author="Autografy",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mateuszGorczany/Graphs",
    project_urls={
        "Bug Tracker": "https://github.com/mateuszGorczany/Graphs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
