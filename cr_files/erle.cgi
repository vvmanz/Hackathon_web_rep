
(function (ph){
try{
var A = self['DSPCounter' || 'AdriverCounter'],
	a = A(ph);
a.reply = {
ph:ph,
rnd:'291996',
bt:62,
sid:223445,
pz:0,
sz:'product',
bn:0,
sliceid:0,
netid:0,
ntype:0,
tns:0,
pass:'',
adid:0,
bid:2864425,
geoid:63,
cgihref:'//ad.adriver.ru/cgi-bin/click.cgi?sid=223445&ad=0&bid=2864425&bt=62&bn=0&pz=0&xpid=DWnQ_R9-3nzJKx4IwA08GcT9Ao8XQUU0OfPTjY06lAsI3ok3V6Q7HI-pKEf4sXWjYrz63f6RDqSjs6A&ref=https:%2f%2fibe.s7.ru%2f&custom=157%3D0%3B10%3DTOF-MOW%3B11%3Dundefined%3B206%3DDSPCounter',
target:'_blank',
width:'0',
height:'0',
alt:'AdRiver',
mirror:A.httplize('//mlb1.adriver.ru'), 
comp0:'0/script.js',
custom:{"10":"TOF-MOW","11":"undefined","157":"0","206":"DSPCounter"},
cid:'',
uid:0,
xpid:'DWnQ_R9-3nzJKx4IwA08GcT9Ao8XQUU0OfPTjY06lAsI3ok3V6Q7HI-pKEf4sXWjYrz63f6RDqSjs6A'
}
var r = a.reply;

r.comppath = r.mirror + '/images/0002864/0002864425/' + (/^0\//.test(r.comp0) ? '0/' : '');
r.comp0 = r.comp0.replace(/^0\//,'');
if (r.comp0 == "script.js" && r.adid){
	A.defaultMirror = r.mirror; 
	A.loadScript(r.comppath + r.comp0 + '?v' + ph) 
} else if ("function" === typeof (A.loadComplete)) {
   A.loadComplete(a.reply);
}
(function (o) {
	var i, w = o.c || window, d = document, y = 10;
	function oL(){
		if (!w.postMessage || !w.addEventListener) {return;}
		if (w.document.readyState == 'complete') {return sL();}
		w.addEventListener('load', sL, false);
	}
	function sL(){try{i.contentWindow.postMessage('pgLd', '*');}catch(e){}}
	function mI(u, oL){
		var i = d.createElement('iframe'); i.setAttribute('src', o.hl(u)); i.onload = oL; with(i.style){width = height = '10px'; position = 'absolute'; top = left = '-10000px'} d.body.appendChild(i);
		return i;
	}
	function st(u, oL){
		if (d.body){return i = mI(u, oL)}
		if(y--){setTimeout(function(){st(u, oL)}, 100)}
	}
	st(o.hl('https://content.adriver.ru/banners/0002186/0002186173/0/s.html?0&4&6&0&291996&0&0&63&85.143.79.134&counter&' + (o.all || 0)), oL);
}({
	hl: A.httplize,
	
	all: 1
	
}));
}catch(e){} 
}('2'));
