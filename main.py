
# 读取nes文件
with open("smb1.nes","rb") as f:
    nes = f.read()
print(nes[0:16])