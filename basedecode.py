import base64

print('''

 /$$$$$$$$ /$$
| $$_____/| $$
| $$      | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$
| $$$$$   | $$ |____  $$ /$$__  $$ /$$_____/ /$$__  $$
| $$__/   | $$  /$$$$$$$| $$  \ $$|  $$$$$$ | $$$$$$$$
| $$      | $$ /$$__  $$| $$  | $$ \____  $$| $$_____/
| $$$$$$$$| $$|  $$$$$$$| $$$$$$$/ /$$$$$$$/|  $$$$$$$
|________/|__/ \_______/| $$____/ |_______/  \_______/
                        | $$
                        | $$
                        |__/

''')
print("请输入需要解码的字符串")
bm = input()
while (True):
	try:
		decode = base64.b16decode(bm)
	except :
		try:
			decode = base64.b32decode(bm)
		except :
			try:
				decode = base64.b64decode(bm)
			except :
				break
	bm = decode
try:
    decode = str(decode).replace('b\'','')
    decode = str(decode).replace('\'','')
    print("\n"+"解码结果为: "+decode)
    input("按回车退出程序")
except:
    print("请输入正确的base编码字符串!")
    input("按回车退出程序")
