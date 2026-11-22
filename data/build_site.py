"""Reproduzierbarer statischer Build einschließlich exakter 9:16-Textguides."""
import json, re, runpy
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
runpy.run_path(str(ROOT/'data/build_content.py'))
topics=json.loads((ROOT/'data/topics.json').read_text())
raw=json.dumps(topics,ensure_ascii=False).replace('</','<\\/')
page=(ROOT/'index.html').read_text()
page=re.sub(r'(<script id="topic-data" type="application/json">).*?(</script>)',lambda m:m[1]+raw+m[2],page,flags=re.S)
(ROOT/'index.html').write_text(page)
font_root=Path('/usr/share/fonts/truetype/dejavu')
def font(size,bold=False):
    return ImageFont.truetype(str(font_root/('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')),size)
def lines(draw,text,f,width):
    result=[]
    for paragraph in text.split('\n'):
        line=''
        for word in paragraph.split():
            candidate=(line+' '+word).strip()
            if draw.textlength(candidate,font=f)>width and line:
                result.append(line);line=word
            else:line=candidate
        result.append(line)
    return result
def write(draw,text,xy,f,width,fill,gap=12):
    x,y=xy
    for line in lines(draw,text,f,width):
        draw.text((x,y),line,font=f,fill=fill)
        y+=f.size+gap
    return y
(ROOT/'guides').mkdir(exist_ok=True)
for t in topics:
    im=Image.new('RGB',(1080,1920),'#123b46');d=ImageDraw.Draw(im)
    d.rounded_rectangle((64,62,1016,130),radius=20,fill='#ccece4')
    d.text((88,78),'ANÄSTHESIE LERNWELT  /  '+t['id'],font=font(27,True),fill='#123b46')
    y=write(d,t['title'],(76,174),font(58,True),928,'#a3e2d4',10)
    assert y<410,(t['id'],'title overflow')
    start=430
    for i,text in enumerate(t['guide']):
        top=start+i*278
        d.line((76,top,1004,top),fill='#587e85',width=3)
        d.text((76,top+18),'MERKPUNKT '+str(i+1),font=font(27,True),fill='#a3e2d4')
        bottom=write(d,text,(76,top+66),font(39),928,'white',11)
        assert bottom<=top+266,(t['id'],i,'body overflow',bottom)
    y=write(d,'Lernhilfe · Stand 22.11.2026\nLokale SOP und Fachinformation beachten.',(76,1600),font(27),928,'#d6e9e9',10)
    y=write(d,'Quellen: '+ '; '.join(s['title'] for s in t['sources']),(76,y+16),font(23),928,'#d6e9e9',7)
    assert y<1850,(t['id'],'sources overflow',y)
    d.text((76,1858),'Quellenlinks und Fortbildung: siehe Lernwelt',font=font(23),fill='#a3e2d4')
    im.save(ROOT/t['guideImage'],optimize=True)
print('22 PNG-Guides mit Überlaufkontrolle erzeugt; Themen eingebettet.')
