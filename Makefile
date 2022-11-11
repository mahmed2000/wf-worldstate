
wf-worldstate:
	pyuic5 gui_base.ui -o gui_base.py
	python -m nuitka main.py --follow-imports --nofollow-import-to=requests --nofollow-import-to=PyQt5
	mv main.bin wf-worldstate && rm main.build/ -r
