from PIL import Image

def iter_frames(im):
    try:
        while True:
            current_frame = im.copy()
            yield current_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass

im = Image.open(r'Bg.gif')

frames = []
try:
    while True:
        frames.append(im.copy())
        im.seek(im.tell() + 1)
except EOFError:
    pass

for i, frame in enumerate(frames):
    frame.save(r'/storage/emulated/0/gif_to_png/Img/convert%d.png' % i)