from pathlib import Path
path = Path('txt_files/pi_digits.txt')
contents = path.read_text()
contents +='done!'
print(contents)