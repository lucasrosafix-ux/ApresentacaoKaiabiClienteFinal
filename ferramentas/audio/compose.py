import numpy as np, wave
SR=44100; DUR=64.0; N=int(SR*DUR)
rng=np.random.default_rng(7)
t=np.arange(N)/SR
L=np.zeros(N);R=np.zeros(N)
def mtof(m): return 440*2**((m-69)/12)
def env_adsr(n,a,r):
    e=np.ones(n);ai=int(a*SR);ri=int(r*SR)
    e[:ai]=np.linspace(0,1,ai)**2;e[-ri:]*=np.linspace(1,0,ri)**1.5;return e
def onepole(x,c):
    y=np.empty_like(x);acc=0.0
    # vectorized lowpass via lfilter-like recursion
    from scipy.signal import lfilter
    return lfilter([c],[1,-(1-c)],x)
# --- pads: D major-ish, slow chords, 8s each
chords=[[50,57,62,64,69],[47,54,59,62,66],[43,50,57,59,66],[45,52,57,59,64],
        [50,57,62,66,71],[47,54,59,62,69],[43,50,55,59,64],[45,52,57,61,64]]
seg=8.0
for i,ch in enumerate(chords):
    s=int(i*seg*SR); n=int((seg+3)*SR); n=min(n,N-s) if i<len(chords)-1 else n
    tt=np.arange(n)/SR
    e=env_adsr(n,2.5,3.5)
    for j,m in enumerate(ch):
        f=mtof(m)
        for d,pan in ((-0.07,0.25),(0.07,0.75)):
            ff=f*2**(d/12*0.5)
            sig=(np.sin(2*np.pi*ff*tt+rng.uniform(0,6))+0.25*np.sin(4*np.pi*ff*tt)+0.08*np.sin(6*np.pi*ff*tt))
            sig*=e*0.028*(1.0 if j>0 else 1.3)*(1+0.15*np.sin(2*np.pi*0.13*tt+j))
            idx=np.arange(s,s+n)%N   # wrap for seamless loop
            np.add.at(L,idx,sig*(1-pan)); np.add.at(R,idx,sig*pan)
# --- low drone
dr=0.05*np.sin(2*np.pi*mtof(38)*t)*(0.7+0.3*np.sin(2*np.pi*t/16))
L+=dr;R+=dr
# --- kalimba-like plucks, D major pentatonic
pent=[62,64,66,69,71,74,76,78,81]
times=np.arange(1.0,DUR-1,1.0)
for k,tm in enumerate(times):
    if rng.random()<0.45: continue
    m=pent[rng.integers(len(pent))]; f=mtof(m)
    n=int(3.2*SR); s=int(tm*SR+rng.uniform(-.08,.08)*SR); tt=np.arange(n)/SR
    e=np.exp(-tt*2.2)*(1-np.exp(-tt*400))
    sig=(np.sin(2*np.pi*f*tt)+0.35*np.sin(2*np.pi*f*2.76*tt)*np.exp(-tt*6)+0.15*np.sin(2*np.pi*f*5.4*tt)*np.exp(-tt*12))*e*0.06
    pan=rng.uniform(.2,.8); idx=np.arange(s,s+n)%N
    np.add.at(L,idx,sig*(1-pan)); np.add.at(R,idx,sig*pan)
    # echo
    for dly,g in ((0.375,.35),(0.75,.15)):
        idx2=(idx+int(dly*SR))%N
        np.add.at(L,idx2,sig*g*pan); np.add.at(R,idx2,sig*g*(1-pan))
# --- forest air: wind/leaves (filtered noise, slow swell) + stream
from scipy.signal import butter,sosfilt
def band(x,lo,hi): return sosfilt(butter(2,[lo,hi],btype='band',fs=SR,output='sos'),x)
for ch_,ph in ((0,0),(1,1.7)):
    wn=band(rng.standard_normal(N),300,2200)*0.007*(0.6+0.4*np.sin(2*np.pi*t/11+ph))
    st=band(rng.standard_normal(N),1800,7000)*0.0035*(0.8+0.2*np.sin(2*np.pi*t*0.7+ph))
    (L if ch_==0 else R)[:]+=wn+st
# --- birds: chirps (FM sweeps) sparse
for _ in range(26):
    s=int(rng.uniform(0,DUR-2)*SR); pan=rng.uniform(.1,.9)
    kind=rng.integers(3); base=rng.uniform(2600,4200)
    nchirp=rng.integers(2,5); off=0
    for c in range(nchirp):
        d=rng.uniform(.06,.14); n=int(d*SR); tt=np.arange(n)/SR
        if kind==0: f=base+1400*np.sin(np.pi*tt/d)
        elif kind==1: f=base*(1+0.6*tt/d)
        else: f=base*(1.5-0.6*tt/d)+200*np.sin(2*np.pi*38*tt)
        ph=2*np.pi*np.cumsum(f)/SR
        sig=np.sin(ph)*np.sin(np.pi*tt/d)**2*rng.uniform(.012,.03)
        idx=np.arange(s+off,s+off+n)%N
        np.add.at(L,idx,sig*(1-pan)); np.add.at(R,idx,sig*pan)
        off+=n+int(rng.uniform(.04,.12)*SR)
# --- gentle reverb (simple multi-tap diffusion)
def verb(x):
    y=x.copy()
    for d,g in ((0.031,.32),(0.047,.28),(0.071,.24),(0.113,.2),(0.173,.16),(0.251,.12),(0.379,.09)):
        y+=np.roll(x,int(d*SR))*g
    return y
L=verb(L);R=verb(R)
# loop-safe: wrapped adds already circular; normalize
m=max(abs(L).max(),abs(R).max()); L/=m/0.8; R/=m/0.8
st=np.stack([L,R],1)
open('/dev/null','w')
with wave.open(str(__import__('pathlib').Path(__file__).resolve().parent/'trilha.wav'),'wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR)
    w.writeframes((st*32767).astype(np.int16).tobytes())
print('ok',DUR)
