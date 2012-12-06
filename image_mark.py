"""Adds current git hash to given images' metadata."""
import subprocess
import glob

import Image
import PngImagePlugin

def get_git_rev():
    # TODO: catch case not git repo
    cmd = 'git rev-parse HEAD'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    rev = p.stdout.read()
    return rev

def make_metadata():
    # TODO: more info needed - location of repository (local,
    # remote...)
    rev = get_git_rev()
    metadata = {'rev': rev}
    return metadata

def write_png_data(fname, metadata):
    im = Image.open(fname)
    meta = PngImagePlugin.PngInfo()
    for x in metadata:
        meta.add_text(x, metadata[x])
    im.save(fname, "png", pnginfo=meta)

def main():
    md = make_metadata()
    files = glob.glob('*png')
    for f in files:
        write_png_data(f, md)

if __name__ == '__main__':
    main()
