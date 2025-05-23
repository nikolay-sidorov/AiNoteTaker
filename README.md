AiNoteTaker

AiNoteTaker is a Python-based tool designed to automate the process of transcribing audio recordings and generating concise, structured notes. It leverages speech recognition and natural language processing to assist users in efficiently capturing and summarizing spoken content.

Features
	•	🎙️ Audio Transcription: Converts audio files into text using speech recognition.
	•	🧠 Text Chunking: Processes transcribed text into manageable segments for analysis.
	•	📝 Note Generation: Summarizes text chunks into coherent notes.
	•	🖥️ Graphical User Interface: User-friendly GUI for easy interaction.
	•	🔧 Modular Design: Structured codebase with separate modules for each functionality. ￼ ￼

Installation
1.	Clone the Repository:

`git clone https://github.com/nikolay-sidorov/AiNoteTaker.git
cd AiNoteTaker`


2.	Create a Virtual Environment (Optional but Recommended):

`python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate`


3.	Install Dependencies:

`pip install -r req.txt`



Usage
	1.	Prepare Your Audio File: Ensure your audio file is in a supported format (e.g., WAV, MP3).
	2.	Run the Application:

python main.py


	3.	Follow the GUI Prompts: Use the graphical interface to select your audio file and initiate the transcription and note generation process.

Project Structure
	•	main.py – Entry point of the application.
	•	audioToTextF.py – Handles audio transcription.
	•	buildTextChunks.py – Processes transcribed text into chunks.
	•	generateNotes.py – Generates notes from text chunks.
	•	processF.py – Additional processing functions.
	•	gui.spec, main.spec, etc. – Configuration files for building executables.
	•	req.txt – List of required Python packages.
	•	setup.py – Setup script for packaging. ￼

Dependencies

Ensure the following Python packages are installed (as listed in req.txt):
	•	speechrecognition
	•	pydub
	•	nltk
	•	tkinter
	•	pyinstaller
	•	…and others as specified. ￼
