import os
from os.path import isfile, join
from pathlib import Path
import shutil

fontextensions = ['.ttf']  # , '.otf', '.fon']
fontSizes = [6, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24]


fontList = os.listdir()
cwd = os.getcwd()
fontList = os.listdir(cwd+rf'\fontsToImport')


def isFont(font):
    ext = Path(font).suffix
    if ext in fontextensions:
        return True

    return False


# // create directories and copy font into them
file1 = open("addedFonts.txt", "w")
for font in fontList:
    if isFont(font):
        dirName = font
        dirName = dirName.replace('.', '-')
        dirName = dirName.replace(' ', '_')
        dirPath = cwd + rf'\GFX_Fonts' + '\\' + dirName
        if not Path(dirPath).exists():
            os.mkdir(dirPath)

        fontName = font
        src_dir = cwd + rf'\fontsToImport' + '\\' + font
        dst_dir = dirPath + '\\' + font
        shutil.copy(src_dir, dst_dir)

dirList = os.listdir(cwd+rf'\GFX_Fonts')
for dirName in dirList:
    fontList = os.listdir(cwd+rf'\GFX_Fonts'+ rf'\\' + dirName)
        
    for font in fontList:
        if isFont(font):
            # convert fonts
            dirPath = cwd + rf'\GFX_Fonts' + '\\' + dirName
            srcFont = font
            gfxFontName = Path(srcFont).stem

            gfxFontName = gfxFontName.replace('.', '-')
            gfxFontName = gfxFontName.replace(' ', '_')
            for size in fontSizes:
                # `fontconvert myCoolFont.ttf 9 > myCoolFont9pt7b.h`
                pathToBinary = rf'{cwd}/GFX_Font_Converter-binary/fontconvert.exe'
                srcFile = f'"{dirPath}/{font}"'
                outputfile = rf'{dirPath}/{gfxFontName}_{size}pt7b.h'
                cmd = rf'{pathToBinary} {srcFile} {size} > {outputfile}'
                os.system(cmd)
                print(f'converted {font} into {gfxFontName}_{size}pt7b.h')

            # add to list
            file1.write(f"- {font}\n")

file1.close()
