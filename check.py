import requests
import urllib3
id=[
    '154415890546', 
    '958315314028', 
    '312451761809', 
    '694123567413', 
    '334867315874', 
    '017354834894', 
    '914184206958', 
    '544912737910', 
    '118290414935', 
    '630359852497', 
    '098528148504', 
    '567801935112', 
    '298512904709', 
    '154295817385', 
    '887214794531', 
    '831937431645', 
    '094396385946', 
    '651640967832', 
    '071229575183', 
    '303018375412', 
    '315729506731', 
    '783479575392', 
    '099285613545',
    '846500184731', 
    '564784314802', 
    '592156701134', 
    '551034956103', 
    '610983523245', 
    '983407923445', 
    '312043258459', 
    '602125782357', 
    '647231582498', 
    '790679208248', 
    '254759082185', 
    '983014892714', 
    '082310945469', 
    '327082915435', 
    '280411845030', 
    '831249042892', 
    '031429317465', 
    '135175665152', 
    '702420575721', 
    '934636438654', 
    '632115655946', 
    '405995322384', 
    '031448158156', 
    '318434328510', 
    '530760572787', 
    '365173857479', 
    '188290270799', 
    '053933621568', 
    '023912381828', 
    '773716321233', 
    '807724916207', 
    '956250835710', 
    '102254133830']

Session=requests.Session()

for i in id:

#the required first parameter of the 'get' method is the 'url':
    x = Session.head(f'http://localhost:8080/login/{i}')
    #print the response text (the content of the requested file):
    if (x.status_code==200):
        print(i)
        break
    print(x.status_code, i)
# import urllib.request


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# for i in range(0,999999999999) :
#     url = 'http://localhost:8080/login/123456789121'
#     req = urllib.request.Request(url, headers=headers)
#     try:
#         response = urllib.request.urlopen(req)
#         content = response.read().decode('utf-8')
#         print(content)
#     except Exception as e : 
#         print(e)
    
#     e4ddaa73449351b70081ad715ec86a6d
#     79d392da396c4b4b9826f6f66afb8c68
#     79d392da396c4b4b9826f6f66afb8c68
#     df0c3e949582975ddf1ba00ffd90a2f6
#     a597ce1759d2986e159b57fc106f1997
#     b52afbfac237f11045a701f2f92ade3b
    
#     79d392da396c4b4b9826f6f66afb8c68
    
#     e4ddaa73449351b70081ad715ec86a6d
#     79d392da396c4b4b9826f6f66afb8c68
#     df0c3e949582975ddf1ba00ffd90a2f6
#     a597ce1759d2986e159b57fc106f1997
#     b52afbfac237f11045a701f2f92ade3b
    
#     e4ddaa73449351b70081ad715ec86a6d
#     cf7d6bd2de1298c78c9bb7de535014cb
#     aecb9c91efc47a6b2ac521aa74d2d52f
#     bdae8f4d417e9056d85500686c712402
#     72faa70835b1be7f9977589c7aa84532
    
#     e4ddaa73449351b70081ad715ec86a6d
#     8326210096cd8a60e2f69b888f04df46
#     192b2b6d26952e5940a6d83974cc3073
#     83f66b5b9a699901c6e04d22620314ae
#     461757b806d1d70f001c0026d1d62399
#     6d579e75d3607e16ddaf72248efc659a
#     6391df158005f7dd8bf0609a812ff74e
#     67f61af01d5edc33b1aa784e2c2b1b31
#     82278f3e28204b90863aa3a9310323fd
#     aecb9c91efc47a6b2ac521aa74d2d52f
#     bdae8f4d417e9056d85500686c712402
#     72faa70835b1be7f9977589c7aa84532
    
    
#     e4ddaa73449351b70081ad715ec86a6d
#     8326210096cd8a60e2f69b888f04df46
#     192b2b6d26952e5940a6d83974cc3073
#     83f66b5b9a699901c6e04d22620314ae
#     461757b806d1d70f001c0026d1d62399
#     6d579e75d3607e16ddaf72248efc659a
#     6391df158005f7dd8bf0609a812ff74e
#     67f61af01d5edc33b1aa784e2c2b1b31
#     82278f3e28204b90863aa3a9310323fd
#     c602f15e76c2c081712d4421566edcea
#     be2a162c5f6006350414ff1a13fe410b
#     ee4a0ac6638cb837b64f0845864708d5
#     612a6e31f21f5c64d05dbe2f6e63242e
#     48fbb17127ed8dfc76a1036f65211926
#     2b9c4e0bb3c24c9a101c85d83ce2d621
#     22b37dbece4adaf5d7ec69a583390a59
#     bdae8f4d417e9056d85500686c712402
#     1667fae89217d3fe77aeffbada845940
#     b6504771683edf335468e42754121b0d6d9c68b2b6b56a27f3228f248010fc42567b0ece3bd871f6886dd36590874df83004ae2f35294f59f13b1dcce322504edaf52555a7abc0cae65693039c3b0cb4fd019e1422229e4e6393452f3a872107cf7d6bd2de1298c78c9bb7de535014cbcb963e0606c30e2974d7725f8749d270ce3474a50cb8751df0feafbdb8c22e17aecb9c91efc47a6b2ac521aa74d2d52fbdae8f4d417e9056d85500686c71240272faa70835b1be7f9977589c7aa84532
    
    
#     e4ddaa73449351b70081ad715ec86a6d
#     bdae8f4d417e9056d85500686c712402
#     aecb9c91efc47a6b2ac521aa74d2d52f
#     bdae8f4d417e9056d85500686c712402
#     72faa70835b1be7f9977589c7aa84532
# Hello AAAAAAAAAAflag is letter PBBBBBBBBBB, the flag is letter X (uppercase).
#add a line ahihihi
