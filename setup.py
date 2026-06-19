import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="TiberianSunCABAL-Talk",
    version="0.0.1",
    author="ASp2004",
    description="CABAL (Milton James) text-to-speech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ASp2004/TiberianSunCABAL-Talk",
    packages=["tibsuncabal_talk"],
    entry_points={
        "console_scripts": ["tibsuncabal_talk=tibsuncabal_talk.__main__:main"],
    },
    install_requires=["g2p_en", "numpy", "pydub", "sounddevice"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
