from setuptools import setup, find_packages

setup(
    name="eagi_processor",
    version="1.0.0",
    author="Eduardo",
    author_email="eduardo@araizainc.com",
    description="Procesador de voz EAGI para Asterisk PBX con reconocimiento de voz",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/araizaeduardo/eagi_processor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Communications :: Telephony",
    ],
    python_requires=">=3.6",
    install_requires=[
        "SpeechRecognition>=3.8.1",
        "pyaudio>=0.2.11",
        "wave>=0.0.2",
    ],
    entry_points={
        "console_scripts": [
            "eagi-processor=eagi_processor.eagi_script:main",
        ],
    },
)
