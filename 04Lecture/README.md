# Generating Music with SCAMP

Creating music with the library [SCAMP](http://scamp.marcevanstein.com/).

## Requirements
- Python 3.6+

## Instructions
1. Create a virtual environment 

- If you installed python with conda please follow the following steps to create a virtual environment called calc.
```bash
  conda create –-name music python
```

Activate your environment
```bash
  conda activate music
```

- If you do not have conda, create a virtual environment using the following steps

i. You need to install the library virtualenv
```bash
  pip3 install virtualenv
```

ii: Create a virtual environment called calc with virtualenv

Window users:
```bash
  python -m venv music
```

MAC users:
```bash
  virtualenv -p python music
```

iii. Activate your virtual environment

Window users:
```bash
  .\music\Scripts\activate
```

MAC users:
```bash
  source music/bin/activate
```

2. In your activated virtual environment, install the library scamp
```bash
  pip3 install scamp
```

3. Make sure the library installed corrected by creating a python script called `test.py` and execute the following code:

```python
  from scamp import test_run

  test_run.play()
```

Give it a few seconds! You should hear a piano playing. Ignore the warnings for now.

4. If you want to transcribe your music you will need to install [LilyPond](http://lilypond.org/download.html) from the link and abjad, which is a python library that generates PDFs of music notation using LilyPond.

- Install LilyPond from [here](http://lilypond.org/download.html)
- Install abjad using pip
```bash
  pip3 install abjad
```

5. Make sure everything is installed corrected by creating a python script called `test2.py` and execute the following code:

```python
    from scamp import test_run

    test_run.play(show_lilypond=True)
```

If you hear a piano gesture sweeping inward towards middle C, and then see a PDF pop up with the music, then the setup process has been successful!
