{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jnsbrdbr/RNN-plays-music/blob/master/RNN.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kj6X6TCcZ4FI",
        "outputId": "4e56585c-79d9-4b1d-a300-1ff8a7c5da71"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyfluidsynth\n",
            "  Downloading pyFluidSynth-1.3.2-py3-none-any.whl (19 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.9/dist-packages (from pyfluidsynth) (1.22.4)\n",
            "Installing collected packages: pyfluidsynth\n",
            "Successfully installed pyfluidsynth-1.3.2\n"
          ]
        }
      ],
      "source": [
        "#PyFluidSynth is a Python binding for the FluidSynth software synthesizer.\n",
        "#It allows to use the FluidSynth library in Python code,\n",
        "#providing a way to play MIDI files and generate sounds from MIDI data.\n",
        "!pip install --upgrade pyfluidsynth"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IDJmdkzAafKe",
        "outputId": "2b435b85-8461-42ad-ea85-450a7bec9d9a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pretty_midi\n",
            "  Downloading pretty_midi-0.2.10.tar.gz (5.6 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.6/5.6 MB\u001b[0m \u001b[31m42.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: numpy>=1.7.0 in /usr/local/lib/python3.9/dist-packages (from pretty_midi) (1.22.4)\n",
            "Collecting mido>=1.1.16\n",
            "  Downloading mido-1.2.10-py2.py3-none-any.whl (51 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m51.1/51.1 kB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: six in /usr/local/lib/python3.9/dist-packages (from pretty_midi) (1.16.0)\n",
            "Building wheels for collected packages: pretty_midi\n",
            "  Building wheel for pretty_midi (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pretty_midi: filename=pretty_midi-0.2.10-py3-none-any.whl size=5592303 sha256=06966d7a39322004ffb9b59f4bbb51a3808431cf7aa5403808bbee64bbb2cfb9\n",
            "  Stored in directory: /root/.cache/pip/wheels/75/ec/20/b8e937a5bcf1de547ea5ce465db7de7f6761e15e6f0a01e25f\n",
            "Successfully built pretty_midi\n",
            "Installing collected packages: mido, pretty_midi\n",
            "Successfully installed mido-1.2.10 pretty_midi-0.2.10\n"
          ]
        }
      ],
      "source": [
        "!pip install pretty_midi \n",
        "#Pretty_midi is a Python library for handling MIDI data, allowing to easily read, write, and modify MIDI files."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cqday1ISzboS",
        "outputId": "0ab51638-2eaf-400b-af92-4cafa759b7c7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following additional packages will be installed:\n",
            "  fluid-soundfont-gm libfluidsynth2 libinstpatch-1.0-2 qsynth\n",
            "  timgm6mb-soundfont\n",
            "Suggested packages:\n",
            "  fluid-soundfont-gs timidity jackd musescore\n",
            "The following NEW packages will be installed:\n",
            "  fluid-soundfont-gm fluidsynth libfluidsynth2 libinstpatch-1.0-2 qsynth\n",
            "  timgm6mb-soundfont\n",
            "0 upgraded, 6 newly installed, 0 to remove and 24 not upgraded.\n",
            "Need to get 126 MB of archives.\n",
            "After this operation, 157 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu focal/universe amd64 fluid-soundfont-gm all 3.1-5.1 [119 MB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 libinstpatch-1.0-2 amd64 1.1.2-2build1 [238 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu focal/universe amd64 timgm6mb-soundfont all 1.3-3 [5,420 kB]\n",
            "Get:4 http://archive.ubuntu.com/ubuntu focal/universe amd64 libfluidsynth2 amd64 2.1.1-2 [198 kB]\n",
            "Get:5 http://archive.ubuntu.com/ubuntu focal/universe amd64 fluidsynth amd64 2.1.1-2 [25.6 kB]\n",
            "Get:6 http://archive.ubuntu.com/ubuntu focal/universe amd64 qsynth amd64 0.6.1-1build1 [245 kB]\n",
            "Fetched 126 MB in 2s (74.6 MB/s)\n",
            "debconf: unable to initialize frontend: Dialog\n",
            "debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76, <> line 6.)\n",
            "debconf: falling back to frontend: Readline\n",
            "debconf: unable to initialize frontend: Readline\n",
            "debconf: (This frontend requires a controlling tty.)\n",
            "debconf: falling back to frontend: Teletype\n",
            "dpkg-preconfigure: unable to re-open stdin: \n",
            "Selecting previously unselected package fluid-soundfont-gm.\n",
            "(Reading database ... 122352 files and directories currently installed.)\n",
            "Preparing to unpack .../0-fluid-soundfont-gm_3.1-5.1_all.deb ...\n",
            "Unpacking fluid-soundfont-gm (3.1-5.1) ...\n",
            "Selecting previously unselected package libinstpatch-1.0-2:amd64.\n",
            "Preparing to unpack .../1-libinstpatch-1.0-2_1.1.2-2build1_amd64.deb ...\n",
            "Unpacking libinstpatch-1.0-2:amd64 (1.1.2-2build1) ...\n",
            "Selecting previously unselected package timgm6mb-soundfont.\n",
            "Preparing to unpack .../2-timgm6mb-soundfont_1.3-3_all.deb ...\n",
            "Unpacking timgm6mb-soundfont (1.3-3) ...\n",
            "Selecting previously unselected package libfluidsynth2:amd64.\n",
            "Preparing to unpack .../3-libfluidsynth2_2.1.1-2_amd64.deb ...\n",
            "Unpacking libfluidsynth2:amd64 (2.1.1-2) ...\n",
            "Selecting previously unselected package fluidsynth.\n",
            "Preparing to unpack .../4-fluidsynth_2.1.1-2_amd64.deb ...\n",
            "Unpacking fluidsynth (2.1.1-2) ...\n",
            "Selecting previously unselected package qsynth.\n",
            "Preparing to unpack .../5-qsynth_0.6.1-1build1_amd64.deb ...\n",
            "Unpacking qsynth (0.6.1-1build1) ...\n",
            "Setting up fluid-soundfont-gm (3.1-5.1) ...\n",
            "Setting up timgm6mb-soundfont (1.3-3) ...\n",
            "update-alternatives: using /usr/share/sounds/sf2/TimGM6mb.sf2 to provide /usr/share/sounds/sf2/default-GM.sf2 (default-GM.sf2) in auto mode\n",
            "update-alternatives: using /usr/share/sounds/sf2/TimGM6mb.sf2 to provide /usr/share/sounds/sf3/default-GM.sf3 (default-GM.sf3) in auto mode\n",
            "Setting up libinstpatch-1.0-2:amd64 (1.1.2-2build1) ...\n",
            "Setting up libfluidsynth2:amd64 (2.1.1-2) ...\n",
            "Setting up qsynth (0.6.1-1build1) ...\n",
            "Setting up fluidsynth (2.1.1-2) ...\n",
            "Created symlink /etc/systemd/user/multi-user.target.wants/fluidsynth.service → /usr/lib/systemd/user/fluidsynth.service.\n",
            "Processing triggers for hicolor-icon-theme (0.17-2) ...\n",
            "Processing triggers for libc-bin (2.31-0ubuntu9.9) ...\n",
            "Processing triggers for man-db (2.9.1-1) ...\n",
            "Processing triggers for mime-support (3.64ubuntu1) ...\n"
          ]
        }
      ],
      "source": [
        "!sudo apt install -y fluidsynth"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "z76kpll7an9H"
      },
      "outputs": [],
      "source": [
        "import collections #collections is a built-in module that provides a collection of specialized container data types, in addition to the built-in data types such as lists, dictionaries, and tuples.\n",
        "import datetime #is a module that provides classes for working with dates and times. \n",
        "import fluidsynth #In Python, fluidsynth is a module that provides a Python wrapper for the FluidSynth software synthesizer. FluidSynth is an open-source software synthesizer that can be used to generate sound from MIDI files or other sources.\n",
        "import glob #In Python, glob is a module that provides a function for working with filenames and directories using pattern matching rules similar to those used in Unix shell. The glob function can be used to search for files or directories that match a specified pattern.\n",
        "import numpy as np\n",
        "import pathlib #In Python, pathlib is a module that provides an object-oriented interface for working with file system paths. It allows you to create, manipulate, and inspect paths in a platform-independent way.\n",
        "import pandas as pd\n",
        "import pretty_midi#pretty_midi is a Python library for handling MIDI files in a simple and intuitive way. It provides a high-level interface for manipulating MIDI data, such as notes, velocities, and timings, as well as lower-level access to MIDI events such as control changes and program changes.\n",
        "import seaborn as sns\n",
        "import tensorflow as tf\n",
        "\n",
        "from IPython import display\n",
        "from matplotlib import pyplot as plt\n",
        "from typing import Dict, List, Optional, Sequence, Tuple\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dN3qeVy4TLNH",
        "outputId": "c27eeaaf-bc4f-4c6c-cc8d-29c40eb28b16"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "i1GSfeEQy7BX"
      },
      "outputs": [],
      "source": [
        "seed = 42\n",
        "tf.random.set_seed(seed)\n",
        "np.random.seed(seed)\n",
        "\n",
        "# Sampling rate for audio playback\n",
        "_SAMPLING_RATE = 16000\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UgwJBos0zDNA",
        "outputId": "16a2a8b5-aec2-4ca4-fcc4-45908166ad24"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Downloading data from https://storage.googleapis.com/magentadata/datasets/maestro/v2.0.0/maestro-v2.0.0-midi.zip\n",
            "59243107/59243107 [==============================] - 0s 0us/step\n"
          ]
        }
      ],
      "source": [
        "data_dir = pathlib.Path('/content/data/maestro-v2.0.0')\n",
        "if not data_dir.exists():\n",
        "  tf.keras.utils.get_file(\n",
        "      'maestro-v2.0.0-midi.zip',\n",
        "      origin='https://storage.googleapis.com/magentadata/datasets/maestro/v2.0.0/maestro-v2.0.0-midi.zip',\n",
        "      extract=True,\n",
        "      cache_dir='.', cache_subdir='data',\n",
        "  )\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wisU6EuS2UHz",
        "outputId": "b2044b15-3619-450d-f653-6fcf67b43ec2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Number of files: 1282\n"
          ]
        }
      ],
      "source": [
        "#The dataset contains about 1,200 MIDI files.\n",
        "filenames = glob.glob(str(data_dir/'**/*.mid*'))\n",
        "print('Number of files:', len(filenames))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jniCcMkjO2_1"
      },
      "outputs": [],
      "source": [
        "#download the file\n",
        "from google.colab import files"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "DTntrURiOHPY",
        "outputId": "64eb6942-7748-4d99-d9f3-b626486e4a2c"
      },
      "outputs": [
        {
          "data": {
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "application/javascript": [
              "download(\"download_dfc9ec01-5acd-4ce0-aaff-3ee1a17ba737\", \"MIDI-Unprocessed_01_R1_2006_01-09_ORIG_MID--AUDIO_01_R1_2006_02_Track02_wav.midi\", 43697)"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "sample_file = filenames[4]\n",
        "files.download(sample_file)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "pjJd5tXMPQvG"
      },
      "outputs": [],
      "source": [
        "#create the widget\n",
        "pm = pretty_midi.PrettyMIDI(sample_file)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eZERSM89PkFI"
      },
      "outputs": [],
      "source": [
        "def display_audio(pm: pretty_midi.PrettyMIDI, seconds=30):\n",
        "  waveform = pm.fluidsynth(fs=_SAMPLING_RATE)\n",
        "  # Take a sample of the generated waveform to mitigate kernel resets\n",
        "  waveform_short = waveform[:seconds*_SAMPLING_RATE]\n",
        "  return display.Audio(waveform_short, rate=_SAMPLING_RATE)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 61
        },
        "id": "3VRZ0xGKPoYW",
        "outputId": "0753276b-2740-4544-cc1a-91f4fd3488de"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "                <audio  controls=\"controls\" >\n",
              "                    Your browser does not support the audio element.\n",
              "                </audio>\n",
              "              "
            ],
            "text/plain": [
              "<IPython.lib.display.Audio object>"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "display_audio(pm)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LVHH6kVaGD7o"
      },
      "source": [
        "#about the data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l-Y6aBpoFpoe",
        "outputId": "b7153ca0-ed9c-45e1-b31f-d2b6e3c598ad"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Number of instruments: 1\n",
            "Instrument name: Acoustic Grand Piano\n"
          ]
        }
      ],
      "source": [
        "#what instrment do they use?\n",
        "print('Number of instruments:', len(pm.instruments))\n",
        "instrument = pm.instruments[0]\n",
        "instrument_name = pretty_midi.program_to_instrument_name(instrument.program)\n",
        "print('Instrument name:', instrument_name)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F_jdsgQsGDSP",
        "outputId": "92a7357a-a692-405f-b3c6-f4959d89762a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0: pitch=79, note_name=G5, duration=0.3047\n",
            "1: pitch=74, note_name=D5, duration=0.0977\n",
            "2: pitch=71, note_name=B4, duration=0.0807\n",
            "3: pitch=67, note_name=G4, duration=0.0482\n",
            "4: pitch=74, note_name=D5, duration=0.0508\n",
            "5: pitch=72, note_name=C5, duration=0.2227\n",
            "6: pitch=69, note_name=A4, duration=0.0521\n",
            "7: pitch=62, note_name=D4, duration=0.0547\n",
            "8: pitch=72, note_name=C5, duration=0.0521\n",
            "9: pitch=71, note_name=B4, duration=0.2201\n"
          ]
        }
      ],
      "source": [
        "#extract note\n",
        "#three variables to represent a note when training the model:\n",
        "#pitch, step and duration.\n",
        "#The pitch is the perceptual quality of the sound as a MIDI note number.\n",
        "#The step is the time elapsed from the previous note or start of the track.\n",
        "#The duration is how long the note will be playing in seconds and is the difference between the note end and note start times. \n",
        "for i, note in enumerate(instrument.notes[:10]):\n",
        "  note_name = pretty_midi.note_number_to_name(note.pitch)\n",
        "  duration = note.end - note.start\n",
        "  print(f'{i}: pitch={note.pitch}, note_name={note_name},'\n",
        "        f' duration={duration:.4f}')\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tgG4qnWyH5W8"
      },
      "outputs": [],
      "source": [
        "#Extract the notes from the sample MIDI file.\n",
        "def midi_to_notes(midi_file: str) -> pd.DataFrame:\n",
        "  pm = pretty_midi.PrettyMIDI(midi_file)\n",
        "  instrument = pm.instruments[0]\n",
        "  notes = collections.defaultdict(list)\n",
        "\n",
        "  # Sort the notes by start time\n",
        "  sorted_notes = sorted(instrument.notes, key=lambda note: note.start)\n",
        "  prev_start = sorted_notes[0].start\n",
        "\n",
        "  for note in sorted_notes:\n",
        "    start = note.start\n",
        "    end = note.end\n",
        "    notes['pitch'].append(note.pitch)\n",
        "    notes['start'].append(start)\n",
        "    notes['end'].append(end)\n",
        "    notes['step'].append(start - prev_start)\n",
        "    notes['duration'].append(end - start)\n",
        "    prev_start = start\n",
        "\n",
        "  return pd.DataFrame({name: np.array(value) for name, value in notes.items()})\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "SXG5zd0RIA55",
        "outputId": "f25b496d-814a-4d92-d1e7-ad2367a6d6cc"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-6523f7b3-bb13-4e93-9923-89dc3f5b0481\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>pitch</th>\n",
              "      <th>start</th>\n",
              "      <th>end</th>\n",
              "      <th>step</th>\n",
              "      <th>duration</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>79</td>\n",
              "      <td>1.052083</td>\n",
              "      <td>1.356771</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.304688</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>74</td>\n",
              "      <td>1.326823</td>\n",
              "      <td>1.424479</td>\n",
              "      <td>0.274740</td>\n",
              "      <td>0.097656</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>71</td>\n",
              "      <td>1.403646</td>\n",
              "      <td>1.484375</td>\n",
              "      <td>0.076823</td>\n",
              "      <td>0.080729</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>67</td>\n",
              "      <td>1.506510</td>\n",
              "      <td>1.554688</td>\n",
              "      <td>0.102865</td>\n",
              "      <td>0.048177</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>74</td>\n",
              "      <td>1.735677</td>\n",
              "      <td>1.786458</td>\n",
              "      <td>0.229167</td>\n",
              "      <td>0.050781</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6523f7b3-bb13-4e93-9923-89dc3f5b0481')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-6523f7b3-bb13-4e93-9923-89dc3f5b0481 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-6523f7b3-bb13-4e93-9923-89dc3f5b0481');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   pitch     start       end      step  duration\n",
              "0     79  1.052083  1.356771  0.000000  0.304688\n",
              "1     74  1.326823  1.424479  0.274740  0.097656\n",
              "2     71  1.403646  1.484375  0.076823  0.080729\n",
              "3     67  1.506510  1.554688  0.102865  0.048177\n",
              "4     74  1.735677  1.786458  0.229167  0.050781"
            ]
          },
          "execution_count": 22,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "raw_notes = midi_to_notes(sample_file)\n",
        "raw_notes.head()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-GMNQCzPNIz1"
      },
      "outputs": [],
      "source": [
        "#It may be easier to interpret the note names rather than the pitches, so you can use the function below to convert from the numeric pitch values to note names. The note name shows the type of note, accidental and octave number (e.g. C#4). "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6pmK0DaCcj6t"
      },
      "outputs": [],
      "source": [
        "\n",
        "num_files = 50\n",
        "all_notes = []\n",
        "for f in filenames[:num_files]:\n",
        "  notes = midi_to_notes(f)\n",
        "  all_notes.append(notes)\n",
        "\n",
        "all_notes = pd.concat(all_notes)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OJ86pfugg8K_",
        "outputId": "993bedf8-efa8-4bae-e2a6-4c7f85d34155"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Number of notes parsed: 380351\n"
          ]
        }
      ],
      "source": [
        "n_notes = len(all_notes)\n",
        "print('Number of notes parsed:', n_notes)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vZXSjTcLhWEF"
      },
      "outputs": [],
      "source": [
        "#create a tf.data.Dataset from the parsed notes."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9zdD75W-hQ-v"
      },
      "outputs": [],
      "source": [
        "key_order = ['pitch', 'step', 'duration']\n",
        "train_notes = np.stack([all_notes[key] for key in key_order], axis=1)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uxj1u3VmhaCS",
        "outputId": "0cbd41e2-6fb9-4b17-cbc7-c83f91fd5213"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "TensorSpec(shape=(3,), dtype=tf.float64, name=None)"
            ]
          },
          "execution_count": 30,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "notes_ds = tf.data.Dataset.from_tensor_slices(train_notes)\n",
        "notes_ds.element_spec\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "E2-UgtD6h6C4"
      },
      "outputs": [],
      "source": [
        "#train the model on batches of sequences of notes.\n",
        "#Each example will consist of a sequence of notes as the input features,\n",
        "#and the next note as the label.\n",
        "#In this way, the model will be trained to predict the next note in a sequence. \n",
        "def create_sequences(\n",
        "    dataset: tf.data.Dataset, \n",
        "    seq_length: int,\n",
        "    vocab_size = 128,\n",
        ") -> tf.data.Dataset:\n",
        "  \"\"\"Returns TF Dataset of sequence and label examples.\"\"\"\n",
        "  seq_length = seq_length+1\n",
        "\n",
        "  # Take 1 extra for the labels\n",
        "  windows = dataset.window(seq_length, shift=1, stride=1,\n",
        "                              drop_remainder=True)\n",
        "\n",
        "  # `flat_map` flattens the\" dataset of datasets\" into a dataset of tensors\n",
        "  flatten = lambda x: x.batch(seq_length, drop_remainder=True)\n",
        "  sequences = windows.flat_map(flatten)\n",
        "\n",
        "  # Normalize note pitch\n",
        "  def scale_pitch(x):\n",
        "    x = x/[vocab_size,1.0,1.0]\n",
        "    return x\n",
        "\n",
        "  # Split the labels\n",
        "  def split_labels(sequences):\n",
        "    inputs = sequences[:-1]\n",
        "    labels_dense = sequences[-1]\n",
        "    labels = {key:labels_dense[i] for i,key in enumerate(key_order)}\n",
        "\n",
        "    return scale_pitch(inputs), labels\n",
        "\n",
        "  return sequences.map(split_labels, num_parallel_calls=tf.data.AUTOTUNE)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h8ZqyJHaq0Pu",
        "outputId": "1bed78c5-0764-4607-94b0-a0c6c19f7c50"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(TensorSpec(shape=(25, 3), dtype=tf.float64, name=None),\n",
              " {'pitch': TensorSpec(shape=(), dtype=tf.float64, name=None),\n",
              "  'step': TensorSpec(shape=(), dtype=tf.float64, name=None),\n",
              "  'duration': TensorSpec(shape=(), dtype=tf.float64, name=None)})"
            ]
          },
          "execution_count": 32,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "seq_length = 25\n",
        "vocab_size = 128\n",
        "seq_ds = create_sequences(notes_ds, seq_length, vocab_size)\n",
        "seq_ds.element_spec\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lztm2GqWq2S2",
        "outputId": "12b28cbc-e3ee-48c9-af4f-56feccfc8711"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "sequence shape: (25, 3)\n",
            "sequence elements (first 10): tf.Tensor(\n",
            "[[0.390625   0.         0.5625    ]\n",
            " [0.296875   0.02734375 0.48828125]\n",
            " [0.3828125  0.35546875 0.36979167]\n",
            " [0.2890625  0.01822917 0.359375  ]\n",
            " [0.421875   0.25260417 0.390625  ]\n",
            " [0.328125   0.02083333 0.34765625]\n",
            " [0.3203125  0.34114583 0.76822917]\n",
            " [0.4140625  0.0078125  0.74869792]\n",
            " [0.390625   2.26171875 0.53255208]\n",
            " [0.296875   0.01692708 0.44921875]], shape=(10, 3), dtype=float64)\n",
            "\n",
            "target: {'pitch': <tf.Tensor: shape=(), dtype=float64, numpy=41.0>, 'step': <tf.Tensor: shape=(), dtype=float64, numpy=0.018229166666666963>, 'duration': <tf.Tensor: shape=(), dtype=float64, numpy=0.46614583333333215>}\n"
          ]
        }
      ],
      "source": [
        "for seq, target in seq_ds.take(1):\n",
        "  print('sequence shape:', seq.shape)\n",
        "  print('sequence elements (first 10):', seq[0: 10])\n",
        "  print()\n",
        "  print('target:', target)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jkEDSGprrEpn"
      },
      "outputs": [],
      "source": [
        "batch_size = 64\n",
        "buffer_size = n_notes - seq_length  # the number of items in the dataset\n",
        "train_ds = (seq_ds\n",
        "            .shuffle(buffer_size)\n",
        "            .batch(batch_size, drop_remainder=True)\n",
        "            .cache()\n",
        "            .prefetch(tf.data.experimental.AUTOTUNE))\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gq16L5TprImc",
        "outputId": "232987fc-c5f1-4417-9e4f-80bb92f657c0"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(TensorSpec(shape=(64, 25, 3), dtype=tf.float64, name=None),\n",
              " {'pitch': TensorSpec(shape=(64,), dtype=tf.float64, name=None),\n",
              "  'step': TensorSpec(shape=(64,), dtype=tf.float64, name=None),\n",
              "  'duration': TensorSpec(shape=(64,), dtype=tf.float64, name=None)})"
            ]
          },
          "execution_count": 35,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "train_ds.element_spec"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wBWVE3k7rMIb"
      },
      "outputs": [],
      "source": [
        "def mse_with_positive_pressure(y_true: tf.Tensor, y_pred: tf.Tensor):\n",
        "  mse = (y_true - y_pred) ** 2\n",
        "  positive_pressure = 10 * tf.maximum(-y_pred, 0.0)\n",
        "  return tf.reduce_mean(mse + positive_pressure)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RRjkbGRdrRhw",
        "outputId": "26726bd4-b4c7-4897-a1c7-7a1b55cdd701"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Model: \"model\"\n",
            "__________________________________________________________________________________________________\n",
            " Layer (type)                   Output Shape         Param #     Connected to                     \n",
            "==================================================================================================\n",
            " input_1 (InputLayer)           [(None, 25, 3)]      0           []                               \n",
            "                                                                                                  \n",
            " lstm (LSTM)                    (None, 128)          67584       ['input_1[0][0]']                \n",
            "                                                                                                  \n",
            " duration (Dense)               (None, 1)            129         ['lstm[0][0]']                   \n",
            "                                                                                                  \n",
            " pitch (Dense)                  (None, 128)          16512       ['lstm[0][0]']                   \n",
            "                                                                                                  \n",
            " step (Dense)                   (None, 1)            129         ['lstm[0][0]']                   \n",
            "                                                                                                  \n",
            "==================================================================================================\n",
            "Total params: 84,354\n",
            "Trainable params: 84,354\n",
            "Non-trainable params: 0\n",
            "__________________________________________________________________________________________________\n"
          ]
        }
      ],
      "source": [
        "input_shape = (seq_length, 3)\n",
        "learning_rate = 0.005\n",
        "\n",
        "inputs = tf.keras.Input(input_shape)\n",
        "x = tf.keras.layers.LSTM(128)(inputs)\n",
        "\n",
        "outputs = {\n",
        "  'pitch': tf.keras.layers.Dense(128, name='pitch')(x),\n",
        "  'step': tf.keras.layers.Dense(1, name='step')(x),\n",
        "  'duration': tf.keras.layers.Dense(1, name='duration')(x),\n",
        "}\n",
        "\n",
        "model = tf.keras.Model(inputs, outputs)\n",
        "\n",
        "loss = {\n",
        "      'pitch': tf.keras.losses.SparseCategoricalCrossentropy(\n",
        "          from_logits=True),\n",
        "      'step': mse_with_positive_pressure,\n",
        "      'duration': mse_with_positive_pressure,\n",
        "}\n",
        "\n",
        "optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)\n",
        "\n",
        "model.compile(loss=loss, optimizer=optimizer)\n",
        "\n",
        "model.summary()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EHnqp0Z7rUNt",
        "outputId": "d9f6ee3c-ab18-4ba3-e3c9-62a5022128cc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "5942/5942 [==============================] - 214s 24ms/step - loss: 5.5027 - duration_loss: 0.3199 - pitch_loss: 4.8526 - step_loss: 0.3302\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "{'loss': 5.502748966217041,\n",
              " 'duration_loss': 0.3199348747730255,\n",
              " 'pitch_loss': 4.852625846862793,\n",
              " 'step_loss': 0.3301902413368225}"
            ]
          },
          "execution_count": 38,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "losses = model.evaluate(train_ds, return_dict=True)\n",
        "losses"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nKPo9A2orZLx"
      },
      "outputs": [],
      "source": [
        "model.compile(\n",
        "    loss=loss,\n",
        "    loss_weights={\n",
        "        'pitch': 0.05,\n",
        "        'step': 1.0,\n",
        "        'duration':1.0,\n",
        "    },\n",
        "    optimizer=optimizer,\n",
        ")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W0S-z82Drhc0",
        "outputId": "51b0bb0e-92fb-488d-dad1-b810aca05570"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "   1869/Unknown - 52s 27ms/step - loss: 0.8987 - duration_loss: 0.3182 - pitch_loss: 4.8527 - step_loss: 0.3379"
          ]
        }
      ],
      "source": [
        "model.evaluate(train_ds, return_dict=True)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RqqdHb7YrkeZ"
      },
      "outputs": [],
      "source": [
        "callbacks = [\n",
        "    tf.keras.callbacks.ModelCheckpoint(\n",
        "        filepath='./training_checkpoints/ckpt_{epoch}',\n",
        "        save_weights_only=True),\n",
        "    tf.keras.callbacks.EarlyStopping(\n",
        "        monitor='loss',\n",
        "        patience=5,\n",
        "        verbose=1,\n",
        "        restore_best_weights=True),\n",
        "]\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "BLOn_fvvrsb3",
        "outputId": "bd535085-6bc6-4177-ff2c-edaded2d20be"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Epoch 1/50\n",
            "5942/5942 [==============================] - 342s 57ms/step - loss: 0.3613 - duration_loss: 0.1060 - pitch_loss: 3.9398 - step_loss: 0.0583\n",
            "Epoch 2/50\n",
            "5942/5942 [==============================] - 336s 56ms/step - loss: 0.3518 - duration_loss: 0.1026 - pitch_loss: 3.8613 - step_loss: 0.0561\n",
            "Epoch 3/50\n",
            "5942/5942 [==============================] - 337s 57ms/step - loss: 0.3460 - duration_loss: 0.1009 - pitch_loss: 3.8004 - step_loss: 0.0551\n",
            "Epoch 4/50\n",
            "5942/5942 [==============================] - 326s 55ms/step - loss: 0.3416 - duration_loss: 0.0991 - pitch_loss: 3.7693 - step_loss: 0.0541\n",
            "Epoch 5/50\n",
            "5942/5942 [==============================] - 304s 51ms/step - loss: 0.3385 - duration_loss: 0.0977 - pitch_loss: 3.7481 - step_loss: 0.0534\n",
            "Epoch 6/50\n",
            "5942/5942 [==============================] - 302s 51ms/step - loss: 0.3362 - duration_loss: 0.0967 - pitch_loss: 3.7272 - step_loss: 0.0531\n",
            "Epoch 7/50\n",
            "5942/5942 [==============================] - 301s 51ms/step - loss: 0.3352 - duration_loss: 0.0962 - pitch_loss: 3.7185 - step_loss: 0.0531\n",
            "Epoch 8/50\n",
            "5942/5942 [==============================] - 332s 56ms/step - loss: 0.3340 - duration_loss: 0.0957 - pitch_loss: 3.7109 - step_loss: 0.0528\n",
            "Epoch 9/50\n",
            "5942/5942 [==============================] - 332s 56ms/step - loss: 0.3323 - duration_loss: 0.0949 - pitch_loss: 3.7115 - step_loss: 0.0518\n",
            "Epoch 10/50\n",
            "5942/5942 [==============================] - 338s 57ms/step - loss: 0.3305 - duration_loss: 0.0938 - pitch_loss: 3.7050 - step_loss: 0.0515\n",
            "Epoch 11/50\n",
            "5942/5942 [==============================] - 336s 57ms/step - loss: 0.3293 - duration_loss: 0.0930 - pitch_loss: 3.7015 - step_loss: 0.0513\n",
            "Epoch 12/50\n",
            "5942/5942 [==============================] - 338s 57ms/step - loss: 0.3283 - duration_loss: 0.0925 - pitch_loss: 3.6924 - step_loss: 0.0511\n",
            "Epoch 13/50\n",
            "5942/5942 [==============================] - 343s 58ms/step - loss: 0.3297 - duration_loss: 0.0929 - pitch_loss: 3.6997 - step_loss: 0.0518\n",
            "Epoch 14/50\n",
            "5942/5942 [==============================] - 333s 56ms/step - loss: 0.3264 - duration_loss: 0.0913 - pitch_loss: 3.6869 - step_loss: 0.0508\n",
            "Epoch 15/50\n",
            "5942/5942 [==============================] - 307s 52ms/step - loss: 0.3282 - duration_loss: 0.0925 - pitch_loss: 3.6914 - step_loss: 0.0512\n",
            "Epoch 16/50\n",
            "5942/5942 [==============================] - 311s 52ms/step - loss: 0.3270 - duration_loss: 0.0913 - pitch_loss: 3.6900 - step_loss: 0.0512\n",
            "Epoch 17/50\n",
            "5942/5942 [==============================] - 332s 56ms/step - loss: 0.3269 - duration_loss: 0.0921 - pitch_loss: 3.6856 - step_loss: 0.0505\n",
            "Epoch 18/50\n",
            "5942/5942 [==============================] - 350s 59ms/step - loss: 0.3346 - duration_loss: 0.0959 - pitch_loss: 3.7141 - step_loss: 0.0530\n",
            "Epoch 19/50\n",
            "5942/5942 [==============================] - ETA: 0s - loss: 0.3406 - duration_loss: 0.0989 - pitch_loss: 3.7378 - step_loss: 0.0548Restoring model weights from the end of the best epoch: 14.\n",
            "5942/5942 [==============================] - 349s 59ms/step - loss: 0.3406 - duration_loss: 0.0989 - pitch_loss: 3.7378 - step_loss: 0.0548\n",
            "Epoch 19: early stopping\n",
            "CPU times: user 2h 17min 52s, sys: 5min 56s, total: 2h 23min 48s\n",
            "Wall time: 1h 49min 16s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "epochs = 50\n",
        "\n",
        "history = model.fit(\n",
        "    train_ds,\n",
        "    epochs=epochs,\n",
        "    callbacks=callbacks,\n",
        ")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "-bAYyuHAr06k",
        "outputId": "ffebdb7b-1cb1-4d32-d1f2-fb4929f07e94"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "plt.plot(history.epoch, history.history['loss'], label='total loss')\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "9D8M6BhEr3sw"
      },
      "outputs": [],
      "source": [
        "def predict_next_note(\n",
        "    notes: np.ndarray, \n",
        "    keras_model: tf.keras.Model, \n",
        "    temperature: float = 1.0) -> int:\n",
        "  \"\"\"Generates a note IDs using a trained sequence model.\"\"\"\n",
        "\n",
        "  assert temperature > 0\n",
        "\n",
        "  # Add batch dimension\n",
        "  inputs = tf.expand_dims(notes, 0)\n",
        "\n",
        "  predictions = model.predict(inputs)\n",
        "  pitch_logits = predictions['pitch']\n",
        "  step = predictions['step']\n",
        "  duration = predictions['duration']\n",
        "\n",
        "  pitch_logits /= temperature\n",
        "  pitch = tf.random.categorical(pitch_logits, num_samples=1)\n",
        "  pitch = tf.squeeze(pitch, axis=-1)\n",
        "  duration = tf.squeeze(duration, axis=-1)\n",
        "  step = tf.squeeze(step, axis=-1)\n",
        "\n",
        "  # `step` and `duration` values should be non-negative\n",
        "  step = tf.maximum(0, step)\n",
        "  duration = tf.maximum(0, duration)\n",
        "\n",
        "  return int(pitch), float(step), float(duration)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Np4Hw0Zfr8a1"
      },
      "outputs": [],
      "source": [
        "temperature = 2.0\n",
        "num_predictions = 120\n",
        "\n",
        "sample_notes = np.stack([raw_notes[key] for key in key_order], axis=1)\n",
        "\n",
        "# The initial sequence of notes; pitch is normalized similar to training\n",
        "# sequences\n",
        "input_notes = (\n",
        "    sample_notes[:seq_length] / np.array([vocab_size, 1, 1]))\n",
        "\n",
        "generated_notes = []\n",
        "prev_start = 0\n",
        "for _ in range(num_predictions):\n",
        "  pitch, step, duration = predict_next_note(input_notes, model, temperature)\n",
        "  start = prev_start + step\n",
        "  end = start + duration\n",
        "  input_note = (pitch, step, duration)\n",
        "  generated_notes.append((*input_note, start, end))\n",
        "  input_notes = np.delete(input_notes, 0, axis=0)\n",
        "  input_notes = np.append(input_notes, np.expand_dims(input_note, 0), axis=0)\n",
        "  prev_start = start\n",
        "\n",
        "generated_notes = pd.DataFrame(\n",
        "    generated_notes, columns=(*key_order, 'start', 'end'))\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "pSDoXCh8sAcS",
        "outputId": "a2d4bdd1-da33-4257-8f3f-3649bc539b34"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-b6565939-ddc6-4a7a-b226-609596fd6bd8\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>pitch</th>\n",
              "      <th>step</th>\n",
              "      <th>duration</th>\n",
              "      <th>start</th>\n",
              "      <th>end</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>62</td>\n",
              "      <td>0.135042</td>\n",
              "      <td>0.266271</td>\n",
              "      <td>0.135042</td>\n",
              "      <td>0.401312</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>95</td>\n",
              "      <td>0.174374</td>\n",
              "      <td>0.304895</td>\n",
              "      <td>0.309415</td>\n",
              "      <td>0.614311</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>97</td>\n",
              "      <td>0.139008</td>\n",
              "      <td>0.403706</td>\n",
              "      <td>0.448423</td>\n",
              "      <td>0.852129</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>90</td>\n",
              "      <td>0.125875</td>\n",
              "      <td>0.427138</td>\n",
              "      <td>0.574298</td>\n",
              "      <td>1.001436</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>92</td>\n",
              "      <td>0.114378</td>\n",
              "      <td>0.443265</td>\n",
              "      <td>0.688676</td>\n",
              "      <td>1.131940</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>90</td>\n",
              "      <td>0.112692</td>\n",
              "      <td>0.442413</td>\n",
              "      <td>0.801368</td>\n",
              "      <td>1.243781</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>86</td>\n",
              "      <td>0.112536</td>\n",
              "      <td>0.441621</td>\n",
              "      <td>0.913905</td>\n",
              "      <td>1.355526</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>91</td>\n",
              "      <td>0.108062</td>\n",
              "      <td>0.445183</td>\n",
              "      <td>1.021966</td>\n",
              "      <td>1.467149</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>80</td>\n",
              "      <td>0.107015</td>\n",
              "      <td>0.441443</td>\n",
              "      <td>1.128981</td>\n",
              "      <td>1.570424</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>90</td>\n",
              "      <td>0.096809</td>\n",
              "      <td>0.450551</td>\n",
              "      <td>1.225790</td>\n",
              "      <td>1.676342</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b6565939-ddc6-4a7a-b226-609596fd6bd8')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b6565939-ddc6-4a7a-b226-609596fd6bd8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b6565939-ddc6-4a7a-b226-609596fd6bd8');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   pitch      step  duration     start       end\n",
              "0     62  0.135042  0.266271  0.135042  0.401312\n",
              "1     95  0.174374  0.304895  0.309415  0.614311\n",
              "2     97  0.139008  0.403706  0.448423  0.852129\n",
              "3     90  0.125875  0.427138  0.574298  1.001436\n",
              "4     92  0.114378  0.443265  0.688676  1.131940\n",
              "5     90  0.112692  0.442413  0.801368  1.243781\n",
              "6     86  0.112536  0.441621  0.913905  1.355526\n",
              "7     91  0.108062  0.445183  1.021966  1.467149\n",
              "8     80  0.107015  0.441443  1.128981  1.570424\n",
              "9     90  0.096809  0.450551  1.225790  1.676342"
            ]
          },
          "execution_count": 40,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "generated_notes.head(10)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vwNKbrLrsLMN"
      },
      "outputs": [],
      "source": [
        "out_file = 'output.mid'\n",
        "out_pm = notes_to_midi(\n",
        "    generated_notes, out_file=out_file, instrument_name=instrument_name)\n",
        "display_audio(out_pm)\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOMgorkkqAatoihnMqcHQnh",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}