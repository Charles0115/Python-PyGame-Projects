import cx_Freeze

executables = [cx_Freeze.Executable("Slither.py")]

cx_Freeze.setup(
    name='Slither',
    options={'build_exe': {'packages': ['pygame'], 'include_files': ['Apple.png', 'SnakeHead.png']}},
    description="Slither Game Tutorial",
    executables=executables
)

# python setup.py bdist_msi     gives you an installer
# python setup.py build         gives you the exe
