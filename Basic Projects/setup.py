from cx_Freeze import setup,Executable
python_file_path=r"D:\OneDrive\Coading\Python\Basic Projects\Automatic_copy-paste.py"
icon_path=r"D:\OneDrive\Coading\Python\Basic Projects\past.ico"
setup(
    name="Automatic paste programme",
    version='1.0',
    author="Dountless",
    description="it creat a file and paste from the clip board ",
    executables=[Executable(python_file_path,
                icon = icon_path,
                shortcutName="Auto Copy paste",
                shortcutDir='DesktopFolder')]
)