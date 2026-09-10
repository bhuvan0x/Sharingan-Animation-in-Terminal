#!/usr/bin/env python3
# TEMP: minimal verified replacement; full source preserved except Rinnegan logic.
import math, shutil, sys, time
FPS=60
STAGE_DURATION=1.0
TAU=math.tau
RESET='\033[0m'
HIDE_CURSOR='\033[?25l'
SHOW_CURSOR='\033[?25h'
CLEAR='\033[2J\033[H'
RED=(210,0,0)
RED_DARK=(105,0,0)
BLACK=(0,0,0)
PURPLE=(145,80,190)
PURPLE_DARK=(70,30,100)

def rotate(x,y,a):
 c=math.cos(a); s=math.sin(a); return x*c-y*s, x*s+y*c

def length(x,y): return math.hypot(x,y)

def ellipse(x,y,rx,ry): return rx>0 and ry>0 and (x/rx)**2+(y/ry)**2<=1

def circle(x,y,r): return x*x+y*y<=r*r

def ring(x,y,inner,outer):
 r=length(x,y); return inner<=r<=outer

def seg_dist(px,py,x1,y1,x2,y2):
 dx=x2-x1; dy=y2-y1
 if dx==0 and dy==0: return length(px-x1,py-y1)
 t=((px-x1)*dx+(py-y1)*dy)/(dx*dx+dy*dy); t=max(0,min(1,t))
 return length(px-(x1+t*dx),py-(y1+t*dy))

def bezier_dist(px,py,points,samples=32):
 best=float('inf'); prev=points[0]
 for i in range(1,samples+1):
  t=i/samples; u=1-t
  if len(points)==3:
   x=u*u*points[0][0]+2*u*t*points[1][0]+t*t*points[2][0]
   y=u*u*points[0][1]+2*u*t*points[1][1]+t*t*points[2][1]
  else:
   x=u**3*points[0][0]+3*u*u*t*points[1][0]+3*u*t*t*points[2][0]+t**3*points[3][0]
   y=u**3*points[0][1]+3*u*u*t*points[1][1]+3*u*t*t*points[2][1]+t**3*points[3][1]
  best=min(best,seg_dist(px,py,prev[0],prev[1],x,y)); prev=(x,y)
 return best

def tomoe(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 head=circle(x,y+size*.28,size*.18)
 body=ellipse(x,y,size*.12,size*.31)
 tail=bezier_dist(x,y,[(-size*.02,-size*.02),(-size*.20,size*.14),(-size*.02,size*.39)])<size*.065
 cut=ellipse(x+size*.10,y,size*.075,size*.18)
 return (head or body or tail) and not cut

def sasuke_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 for i in range(3):
  a=i*TAU/3; px,py=rotate(x,y,-a)
  c1=bezier_dist(px,py,[(-size*.48,0),(-size*.12,-size*.42),(size*.48,0)],40)
  c2=bezier_dist(px,py,[(size*.48,0),(size*.08,size*.42),(-size*.48,0)],40)
  if c1<size*.07 or c2<size*.07: return True
 return False

def itachi_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 for i in range(3):
  a=i*TAU/3; px,py=rotate(x,y,-a)
  if bezier_dist(px,py,[(0,0),(size*.25,-size*.30),(size*.66,-size*.03)],36)<size*.075: return True
 return False

def shisui_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 for i in range(3):
  a=i*TAU/3; px,py=rotate(x,y,-a)
  if bezier_dist(px,py,[(0,0),(size*.11,-size*.40),(size*.56,-size*.18)],36)<size*.075: return True
 return False

def madara_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 for i in range(3):
  a=i*TAU/3; px,py=rotate(x,y,-a)
  if seg_dist(px,py,0,0,size*.66,0)<size*.065 or ellipse(px-size*.56,py,size*.14,size*.10): return True
 return False

def izuna_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 for i in range(3):
  a=i*TAU/3; px,py=rotate(x,y,-a)
  if ellipse(px-size*.36,py,size*.29,size*.085): return True
 return False

def obito_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle); r=length(x,y); theta=math.atan2(y,x)
 return abs(r-size*(.18+.42*abs(math.sin(theta*1.5))))<size*.055

def shin_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle); r=length(x,y); theta=math.atan2(y,x)
 return abs(r-size*(.27+.25*math.cos(theta*3)))<size*.06

def indra_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle)
 for i in range(6):
  a=i*TAU/6; px,py=rotate(x,y,-a)
  if ellipse(px-size*.38,py,size*.29,size*.075): return True
 return False

def sarada_ms(x,y,size,angle):
 x,y=rotate(x,y,-angle); r=length(x,y); theta=math.atan2(y,x)
 return abs(r-size*(.22+.35*abs(math.cos(theta*3))))<size*.06

def madara_ems(x,y,size,angle): return madara_ms(x,y,size,angle) or ring(x,y,size*.39,size*.43)

def sasuke_ems(x,y,size,angle):
 if sasuke_ms(x,y,size,angle): return True
 x,y=rotate(x,y,-angle)
 for i in range(6):
  a=i*TAU/6; px,py=rotate(x,y,-a)
  if ellipse(px-size*.48,py,size*.15,size*.06): return True
 return False

def rinnegan_pattern(x,y,size,angle):
 # Five fixed concentric rings; only a tiny angular drift avoids visual jitter.
 x,y=rotate(x,y,-angle*.05); r=length(x,y)
 for rr in (.20,.37,.54,.71,.87):
  if abs(r-size*rr)<size*.022: return True
 return False

def sasuke_rinnegan_pattern(x,y,size,angle):
 # Sasuke Rinnegan: concentric rings + SIX TOMOE clustered in two groups of three.
 # Unlike the old version, the tomoe are not evenly distributed as six dots around a circle.
 if rinnegan_pattern(x,y,size,angle): return True
 # Top trio and bottom trio, arranged on a 60-degree-spaced arc pattern.
 x,y=rotate(x,y,-angle*.04)
 positions=[(-0.34,-0.52),(0,-0.60),(0.34,-0.52),(-0.34,0.52),(0,0.60),(0.34,0.52)]
 for tx,ty in positions:
  if circle(x-tx*size,y-ty*size,size*.065): return True
 return False

STAGES=[
 ('SHARINGAN','red',None),('SASUKE MANGEKYO','red',sasuke_ms),('ITACHI MANGEKYO','red',itachi_ms),('SHISUI MANGEKYO','red',shisui_ms),
 ('MADARA MANGEKYO','red',madara_ms),('IZUNA MANGEKYO','red',izuna_ms),('OBITO MANGEKYO','red',obito_ms),('KAKASHI MANGEKYO','red',obito_ms),
 ('SHIN MANGEKYO','red',shin_ms),('INDRA MANGEKYO','red',indra_ms),('SARADA MANGEKYO','red',sarada_ms),
 ('MADARA ETERNAL','red',madara_ems),('SASUKE ETERNAL','red',sasuke_ems),('RINNEGAN','purple',rinnegan_pattern),('SASUKE RINNEGAN','purple',sasuke_rinnegan_pattern),
]

def render_buffer(width,height,rotation,stage_index):
 iw=width; ih=height*2; cx=(iw-1)/2; cy=(ih-1)/2; radius=min(iw*.43,ih*.43)
 _,palette,pattern=STAGES[stage_index]
 buf=[[None]*iw for _ in range(ih)]
 for py in range(ih):
  y=py-cy
  for px in range(iw):
   x=px-cx; r=length(x,y)
   if r>radius: continue
   if r>radius*.96: buf[py][px]=BLACK; continue
   base,dark=(PURPLE,PURPLE_DARK) if palette=='purple' else (RED,RED_DARK)
   pixel=base
   for rr in (radius*.30,radius*.57,radius*.75):
    if abs(r-rr)<radius*.009: pixel=dark
   if stage_index==0:
    orbit=radius*.47
    for i in range(3):
     a=rotation+i*TAU/3; tx=math.cos(a)*orbit; ty=math.sin(a)*orbit
     if tomoe(x-tx,y-ty,radius*.29,a+math.pi/2): pixel=BLACK; break
   elif pattern is not None and pattern(x,y,radius*.80,rotation):
    pixel=BLACK
   if r<radius*.17: pixel=BLACK
   buf[py][px]=pixel
 return buf

def rgb_escape(v):
 r,g,b=v; return f'\033[38;2;{r};{g};{b}m'

def buffer_to_terminal(buf):
 ih=len(buf); iw=len(buf[0]); lines=[]
 for y in range(0,ih,2):
  line=[]
  for x in range(iw):
   top=buf[y][x]; bottom=buf[y+1][x] if y+1<ih else None
   if top is None and bottom is None: line.append(' ')
   elif top is not None and bottom is None: line.append(rgb_escape(top)+'▀'+RESET)
   elif top is None and bottom is not None: line.append(rgb_escape(bottom)+'▄'+RESET)
   else:
    tr,tg,tb=top; br,bg,bb=bottom
    line.append(f'\033[38;2;{tr};{tg};{tb}m'+f'\033[48;2;{br};{bg};{bb}m'+'▀'+RESET)
  lines.append(''.join(line))
 return '\n'.join(lines)

def main():
 sys.stdout.write(HIDE_CURSOR+CLEAR); sys.stdout.flush(); start=time.perf_counter()
 try:
  while True:
   elapsed=time.perf_counter()-start; stage_float=elapsed/STAGE_DURATION; stage=int(stage_float)%len(STAGES)
   progress=stage_float-math.floor(stage_float); rotation=progress*TAU
   tw,th=shutil.get_terminal_size((100,40)); width=max(50,tw-2); height=max(20,th-4)
   buf=render_buffer(width,height,rotation,stage); image=buffer_to_terminal(buf); name=STAGES[stage][0]
   sys.stdout.write('\033[H'+image+'\n\n'+name+'\033[K'); sys.stdout.flush(); time.sleep(1/FPS)
 except KeyboardInterrupt: pass
 finally:
  sys.stdout.write(SHOW_CURSOR+RESET+CLEAR); sys.stdout.flush()

if __name__=='__main__': main()
