"""Reproducible build: detailed lessons, 458 cards and colourful precise 9:16 guides."""
import json,re,runpy
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
runpy.run_path(str(ROOT/'data/build_content.py'))
topics=json.loads((ROOT/'data/topics.json').read_text())
raw=json.dumps(topics,ensure_ascii=False).replace('</','<\\/')
page=(ROOT/'index.html').read_text()
page=re.sub(r'(<script id="topic-data" type="application/json">).*?(</script>)',lambda m:m[1]+raw+m[2],page,flags=re.S)
(ROOT/'index.html').write_text(page)
F=Path('/usr/share/fonts/truetype/dejavu')
def font(s,b=False):return ImageFont.truetype(str(F/('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf')),s)
def lines(d,text,f,width):
    out=[];line=''
    for word in text.split():
        trial=(line+' '+word).strip()
        if line and d.textlength(trial,font=f)>width:out.append(line);line=word
        else:line=trial
    return out+[line]
def put(d,text,x,y,size,width,color,bold=False,gap=10):
    f=font(size,bold)
    for line in lines(d,text,f,width):
        assert d.textlength(line,font=f)<=width,(text,line,'width')
        d.text((x,y),line,font=f,fill=color);y+=size+gap
    return y
panels=[('#dbf4e8','#19735f'),('#dfeeff','#285e97'),('#fff0cd','#916018'),('#ffe2df','#a44740')]
for t in topics:
    im=Image.new('RGB',(1080,1920),'#f8f7f2');d=ImageDraw.Draw(im);ink='#123b46'
    d.rectangle((0,0,1080,370),fill=ink)
    for i,(_,accent) in enumerate(panels):d.rectangle((i*270,0,(i+1)*270,14),fill=accent)
    d.text((66,51),'ANÄSTHESIE LERNWELT   /   '+t['id'],font=font(27,True),fill='#afe8d8')
    size=57 if len(t['title'])<37 else 48
    y=put(d,t['title'],66,116,size,948,'white',True,10)
    assert y<320,(t['id'],'title overflow',y)
    d.text((66,315),'VERSTEHEN  ·  EINORDNEN  ·  ERINNERN',font=font(25,True),fill='#f0d59e')
    for i,(text,(bg,accent)) in enumerate(zip(t['guide'],panels)):
        top=410+i*251
        d.rounded_rectangle((45,top,1035,top+230),radius=25,fill=bg)
        d.rounded_rectangle((45,top,58,top+230),radius=6,fill=accent)
        d.ellipse((80,top+22,135,top+77),fill=accent)
        d.text((96,top+28),str(i+1),font=font(30,True),fill='white')
        d.text((158,top+31),'MERKPUNKT '+str(i+1),font=font(26,True),fill=accent)
        bottom=put(d,text,85,top+88,37,904,ink,False,9)
        assert bottom<=top+225,(t['id'],i,'panel overflow',bottom,top)
    top=1450
    d.rounded_rectangle((45,top,1035,1736),radius=25,fill=ink)
    d.text((80,top+22),'DEINE LERNBRÜCKE',font=font(27,True),fill='#f0d59e')
    bottom=put(d,t['mnemonic'],80,top+77,32,920,'white',False,10)
    assert bottom<1722,(t['id'],'mnemonic overflow',bottom)
    d.text((66,1770),'Lernhilfe · 22.11.2026 · Quellen in der Fortbildung',font=font(24),fill=ink)
    put(d,'Lokale SOP und Fachinformation beachten. Kein vollständiger Notfallalgorithmus.',66,1817,24,940,'#52666d',False,7)
    im.save(ROOT/t['guideImage'],optimize=True)
print('Built 22 detailed lessons, 458 cards and 22 colour PNGs (1080 × 1920), overflow checked.')
