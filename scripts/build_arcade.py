"""Build self-contained SVG artwork. No external fonts or services."""
from pathlib import Path
from html import escape
import math
import random

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
FONT = 'Arial,Helvetica,sans-serif'
MONO = 'ui-monospace,SFMono-Regular,Consolas,monospace'

def text(x,y,value,size=16,color='#dbe5e8',weight=400,mono=False,extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'
def line(x1,y1,x2,y2,color='#263038',width=1,extra=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none" {extra}/>'
def rect(x,y,w,h,fill='#10171c',rx=0,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'
def circle(x,y,r,fill,extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'
def wrap(w,h,title,body):
    style='''<style>
      .blink{animation:blink 2.4s steps(2,end) infinite}
      .float{animation:float 5s ease-in-out infinite}
      .pulse{animation:pulse 3s ease-in-out infinite}
      .dash{stroke-dasharray:5 9;animation:dash 8s linear infinite}
      .scan{animation:scan 7s ease-in-out infinite}
      .orbit{transform-box:fill-box;transform-origin:center;animation:orbit 40s linear infinite}
      @keyframes blink{0%,70%,100%{opacity:1}71%,90%{opacity:.2}}
      @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
      @keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}
      @keyframes dash{to{stroke-dashoffset:-140}}
      @keyframes scan{0%,100%{transform:translateY(0);opacity:.15}50%{transform:translateY(125px);opacity:.65}}
      @keyframes orbit{to{transform:rotate(360deg)}}
      @media(prefers-reduced-motion:reduce){*{animation:none!important}}
    </style>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{style}{body}</svg>'
def write(name,w,h,title,body):
    ASSETS.joinpath(name).write_text(wrap(w,h,title,body))
def pixel_ship(x,y,scale=5,color='#c8ff64'):
    rows=['00011000','00111100','01111110','11011011','11111111','00100100','01000010']
    return ''.join(rect(x+j*scale,y+i*scale,scale-.5,scale-.5,color) for i,row in enumerate(rows) for j,v in enumerate(row) if v=='1')

def hero():
    b=rect(0,0,1200,500,'#090e13',18)+rect(1,1,1198,498,'none',18,'stroke="#2a373e"')
    for x in range(650,1200,36): b+=line(x,60,x,420,'#152027')
    for y in range(60,421,36): b+=line(650,y,1200,y,'#152027')
    b+=rect(0,0,7,500,'#c8ff64')+circle(45,34,4,'#c8ff64','class="pulse"')
    b+=text(60,39,'YADU080 / DEV ARCADE',14,'#b9c6cc',600,True,'letter-spacing="2"')
    b+=text(1030,39,'PLAYER 01',13,'#c8ff64',600,True)+line(35,59,1165,59)
    b+=text(45,113,'WELCOME TO THE BUILD ZONE',13,'#87979f',500,True,'letter-spacing="3"')
    b+=text(38,221,'YADU',130,'#f1f6f6',900,False,'letter-spacing="-7"')
    b+=text(392,221,'.EXE',81,'#c8ff64',800,False,'letter-spacing="-4"')
    b+=rect(584,154,16,69,'#c8ff64',0,'class="blink"')
    b+=text(45,277,'AI experiments. Real code.',28,'#d9e3e7',500)
    b+=text(45,315,'Pick a project. Find out how it works.',23,'#8fa1ab')
    b+=rect(45,350,252,41,'#c8ff64',5)+text(62,377,'↓ SCROLL TO SELECT',16,'#111a0b',700,True)
    b+=text(319,376,'5 WORLDS TO EXPLORE',12,'#8fa1ab',500,True)
    b+='<g class="float"><path d="M807 101L1083 125L1102 328L826 354Z" fill="#111c23" stroke="#3b515d" stroke-width="2"/><path d="M807 101L787 120L805 372L826 354Z" fill="#182930" stroke="#3b515d"/><path d="M826 354L1102 328L1080 347L805 372Z" fill="#1d3338" stroke="#3b515d"/><path d="M827 128L1064 149L1078 293L841 314Z" fill="#071613" stroke="#547745"/>'
    for i in range(12): b+=line(844,157+i*11,1059,175+i*9,'#163022',.8)
    b+=pixel_ship(922,184,8)+rect(847,149,210,2,'#c8ff64',0,'class="scan"')
    b+=text(884,282,'READY TO EXPLORE',11,'#c8ff64',600,True,'transform="rotate(-5 884 282)"')
    b+=circle(1048,320,8,'#c8ff64')+circle(1020,323,5,'#46d9ef')+line(853,338,920,332,'#46656b',4)+'</g>'
    for x,y,label,c in [(700,135,'{ }','#46d9ef'),(1114,240,'<>','#b49aff'),(719,330,'01','#c8ff64')]:
        b+=rect(x,y,57,44,'#111c23',6,f'stroke="{c}" stroke-opacity=".5"')+text(x+11,y+29,label,20,c,600,True)
    b+=line(35,425,1165,425)
    for x,label,c in [(45,'01 / CODE','#c8ff64'),(278,'02 / RECOMMEND','#46d9ef'),(511,'03 / STRESS-TEST','#b49aff'),(744,'04 / INVESTIGATE','#ffb65c'),(977,'05 / MUSIC','#ff86b6')]:
        b+=rect(x,451,7,7,c)+text(x+18,461,label,12,'#b4c2c9',500,True)
    write('arcade-hero.svg',1200,500,'YADU.EXE — AI experiments. Real code. Five project worlds to explore.',b)

def shell(n,title,category,color):
    b=rect(0,0,600,310,'#0a1016',12)+rect(1,1,598,308,'none',12,'stroke="#2b3942"')+rect(0,0,600,4,color)
    b+=text(25,32,f'WORLD {n:02d}',12,color,700,True,'letter-spacing="2"')+text(575,32,category,11,'#80939f',500,True,'text-anchor="end"')
    b+=text(25,76,title,32,'#eff6f8',700,False,'letter-spacing="-.7"')+line(25,99,575,99,'#24333c')
    return b+text(25,285,'ENTER WORLD',12,color,700,True,'letter-spacing="2"')+text(574,286,'↗',23,color,600,False,'text-anchor="end"')

def analyzer():
    b=shell(1,'AI Codebase Analyzer','RETRIEVAL / EXPLORATION','#c8ff64')
    for y,w,label in [(125,111,'api.py'),(161,137,'retriever.py'),(197,126,'qa_engine.py')]:
        b+=rect(30,y,w,24,'#18252a',4,'stroke="#394f4c"')+text(39,y+16,label,11,'#b2c5c4',400,True)+line(30+w,y+12,245,174,'#547647',1.5,'class="dash"')
    b+='<path d="M245 174L286 132L328 174L286 216Z" fill="#1b3021" stroke="#c8ff64" stroke-width="1.5"/>'
    b+=text(286,179,'RAG',15,'#c8ff64',600,True,'text-anchor="middle"')+line(328,174,377,174,'#c8ff64',1.5,'class="dash"')
    b+=rect(378,125,192,101,'#0f211b',7,'stroke="#50794a"')+text(392,147,'> ASK THE CODE',12,'#c8ff64',600,True)
    for y,w in [(164,140),(177,118),(190,151),(203,81)]: b+=rect(393,y,w,4,'#547961',2)
    b+=rect(480,203,7,9,'#c8ff64',0,'class="blink"')
    write('world-01-code.svg',600,310,'World 01: AI Codebase Analyzer. Source files feed retrieval and a code-question interface.',b)

def recommender():
    b=shell(2,'RECOMAI','RETRIEVAL / RANKING','#46d9ef')
    for x,label in [(54,'USER'),(196,'MOVIE')]:
        b+=rect(x,124,89,87,'#12252e',6,'stroke="#356c7b"')
        for row in range(3):
            for col in range(3): b+=circle(x+22+col*23,143+row*23,4,'#46d9ef',f'opacity="{.35+row*.2}"')
        b+=text(x+44,234,label,11,'#87afbb',500,True,'text-anchor="middle"')
    b+=line(143,169,196,169,'#46d9ef',1,'class="dash"')+line(285,169,337,169,'#46d9ef',1.5,'class="dash"')
    for i,w in enumerate([176,130,130]):
        b+=rect(357,128+i*34,w,21,'#173d49',3)+rect(357,128+i*34,4,21,'#46d9ef')+text(370,143+i*34,f'0{i+1}  '+['CANDIDATE','RE-RANK','RECOMMEND'][i],10,'#b2eaf1',500,True)
    write('world-02-recomai.svg',600,310,'World 02: RECOMAI. User and movie representations lead to ranked recommendations.',b)

def hunter():
    b=shell(3,'ModelHunter','ADVERSARIAL ML / EVALUATION','#b49aff')
    b+='<path d="M298 121L349 141V180Q349 214 298 240Q247 214 247 180V141Z" fill="#211c34" stroke="#b49aff" stroke-width="2"/>'
    b+=text(298,185,'ML',27,'#d8c9ff',700,True,'text-anchor="middle"')
    for x,y,label in [(38,129,'FGSM'),(38,192,'PGD')]:
        b+=rect(x,y,106,30,'#1d1930',5,'stroke="#6b579b"')+text(x+17,y+20,label,13,'#c8b3ff',600,True)+line(x+106,y+15,238,175,'#8b70ca',1.4,'class="dash"')
    b+=line(357,175,421,175,'#8b70ca',1.5,'class="dash"')+rect(426,127,141,101,'#171523',5,'stroke="#615379"')+text(439,149,'EVALUATE',11,'#c7b5e4',600,True)
    for x,h in [(440,27),(464,44),(488,34),(512,57),(536,46)]: b+=rect(x,211-h,12,h,'#8e72ce',2)
    write('world-03-modelhunter.svg',600,310,'World 03: ModelHunter. Adversarial attack methods feed model evaluation. Chart is decorative.',b)

def silence():
    b=shell(4,'Silence Engine','ANOMALIES / INVESTIGATION','#ffb65c')
    for x in range(34,362,29): b+=line(x,124,x,229,'#263139')
    for y in range(124,230,26): b+=line(34,y,358,y,'#263139')
    b+='<path d="M34 173L63 160L92 167L121 147L150 156L179 164L208 154L237 172L266 205L295 211L324 207L353 214" fill="none" stroke="#ffb65c" stroke-width="2.5"/>'
    b+=rect(250,123,112,108,'#ffb65c',3,'opacity=".06"')+circle(295,211,5,'#ffb65c','class="pulse"')+line(34,164,358,164,'#78938b',1,'stroke-dasharray="5 6"')
    for y,label,color in [(131,'FEED HEALTH','#9fb4bf'),(167,'SERVICE GAP?','#ffb65c'),(203,'VERIFY FIRST','#a9bea3')]:
        b+=rect(397,y,171,25,'#211d15',4,'stroke="#54432d"')+text(408,y+17,label,11,color,500,True)
    write('world-04-silence.svg',600,310,'World 04: Silence Engine. Investigate activity gaps and feed health. Illustration uses synthetic points.',b)

def music():
    rng=random.Random(42)
    b=rect(0,0,1200,300,'#100d1b',12)+rect(1,1,1198,298,'none',12,'stroke="#493045"')+rect(0,0,1200,4,'#ff86b6')
    for _ in range(150): b+=circle(round(rng.uniform(620,1170),1),round(rng.uniform(25,275),1),rng.choice([.7,1,1.4]),'#bfa1d0',f'opacity="{rng.uniform(.12,.6):.2f}"')
    b+=text(30,35,'WORLD 05 / FINAL STOP',12,'#ff86b6',700,True,'letter-spacing="2"')+text(28,106,'MusicDNA',59,'#f7ecf5',700,False,'letter-spacing="-2"')
    b+=text(30,151,'Your music taste, mapped.',25,'#d5b6ce')+text(30,186,'GENRES → TASTE VECTORS → ARTIST GALAXY',12,'#a58da7',500,True)
    b+=rect(30,228,223,40,'#ff86b6',5)+text(47,254,'ENTER THE GALAXY ↗',14,'#261120',700,True)
    b+='<g transform="translate(908 149) scale(1.35 .72)"><g class="orbit">'
    for arm in range(3):
        pts=[]
        for i in range(52):
            t=i/51*4.5+arm*math.tau/3; radius=15+i*2.3
            x=math.cos(t)*radius; y=math.sin(t)*radius
            pts.append((x,y)); b+=circle(round(x,2),round(y,2),2+(i%4)*.5,['#ff86b6','#b49aff','#46d9ef'][arm],f'opacity="{.35+i/80:.2f}"')
        d='M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)
        b+=f'<path d="{d}" fill="none" stroke="{["#ff86b6","#b49aff","#46d9ef"][arm]}" stroke-opacity=".18"/>'
    b+='</g></g>'+circle(908,149,22,'#ff86b6','opacity=".08" class="pulse"')+circle(908,149,9,'#ffbfdb')
    write('world-05-musicdna.svg',1200,300,'World 05, final stop: MusicDNA. Your music taste, mapped. An animated decorative artist galaxy.',b)

def section(name,number,title,subtitle,color='#c8ff64'):
    b=rect(0,0,1200,100,'#0c1319',9)+rect(0,0,5,100,color)+text(26,41,number,14,color,700,True,'letter-spacing="2"')
    b+=text(95,43,title,27,'#e6eff3',700,False,'letter-spacing="1"')+text(95,74,subtitle,14,'#8fa1ad',400,True)
    write(name,1200,100,title+'. '+subtitle,b)
def footer():
    b=rect(0,0,1200,115,'#0b1217',9)+line(22,1,1178,1,'#354836')+pixel_ship(35,35,6)
    b+=text(107,52,'CONTINUE?',26,'#c8ff64',700,True)+text(107,80,'Every world has source code. Pick one and follow the trail.',17,'#9cafba')+text(1126,68,'↗',39,'#c8ff64',600)
    write('arcade-footer.svg',1200,115,'Continue exploring: every project has source code.',b)

hero(); analyzer(); recommender(); hunter(); silence(); music()
section('section-worlds.svg','02','WORLD SELECT','Five projects. Five different problems. Choose your entry point.')
section('section-inventory.svg','01','THE INVENTORY','Tools found in the repositories below.','#46d9ef')
section('section-challenge.svg','03','THE SOURCE-CODE CHALLENGE','Three questions. Pick an answer. Open the code to verify.','#b49aff')
footer()
print('Built 10 SVG assets.')
