# 运行这个打包机？
#	请先安装python3，然后定位到扩展所在文件夹，
#	再使用命令：
#		python ./build_to_ccx.py
#	或简写指令（部分系统可能不支持）：
#		py build_to_ccx.py

buildfile='./build'
#————————————————————————————————
# 实际上，这就只是一个将文件夹压缩为zip的程序。
#————————————————————————————————
print('build to ccx\n')
try:
	print('#️⃣  import\n\tjson\n\tzipfile\n\tos')
	import json,zipfile,os
	infojsonfile= buildfile + '/info.json'
	print('🔍 read',infojsonfile)
	info= json.loads(open(infojsonfile,'r').read())
	print('📦 packaging ',end='')
	zipname= ("./%s@%s.ccx" %(info['id'], info['version']) )
	print(zipname)
	if os.path.exists(zipname): 
		os.remove(zipname)
	z= zipfile.ZipFile(zipname,"w", zipfile.ZIP_DEFLATED)
	for dirpath,dirs,files in os.walk(buildfile):
		for f in files:
			p= (os.path.join(dirpath, f)).replace('\\','/')
			arcn= p[len(buildfile)+1:]
			print('\t➕ add %s\n\t    to %s'%(p,arcn))
			z.write(p, arcname= arcn)
	print('\t✅ done\n✅ 打包完成\n')
except Exception as e:
	print('\n❌ 打包失败！%s\n'%e)