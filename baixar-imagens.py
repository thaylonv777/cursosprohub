# Baixa as imagens do produtor para a pasta img/ (rode uma vez: python3 baixar-imagens.py)
import os,urllib.request
O="https://trans-resveratrol.com/wp-content/uploads/"
L=["2024/09/90-dias.jpg", "2024/09/K2-REDONDO.png", "2024/09/Modo-de-usar-1-3.png", "2024/09/Modo-de-usar-2-2.png", "2024/09/Modo-de-usar-3-1.png", "2024/09/animais-1-1.webp", "2024/09/anvisa.png", "2024/09/b6.jpg", "2024/09/bnf1.jpeg", "2024/09/bnf2-2.jpeg", "2024/09/bnf3-1.jpeg", "2024/09/bnf4-3.jpeg", "2024/09/bnf5.jpeg", "2024/09/bnf6.jpeg", "2024/09/cliente-1-1.webp", "2024/09/cliente-2-1.webp", "2024/09/cliente-4-1.webp", "2024/09/cliente-5-1.webp", "2024/09/empresa-certificada-iso-9001.png", "2024/09/globo-1-1.webp", "2024/09/gnt-1.webp", "2024/09/icon-formula1.jpeg", "2024/09/icon-formula2.jpeg", "2024/09/icon-formula3.jpeg", "2024/09/icon-formula4.jpeg", "2024/09/pagamento-new.png", "2024/09/r7-1-1.webp", "2024/09/selos-2.png", "2024/11/Design-sem-nome-7-min.png", "2024/11/Inserir-um-titulo-2-min.png", "2024/11/Inserir-um-titulo-3-min.png", "2024/11/Resveratrol-Adalberto-1-min.png", "2024/11/Resveratrol-Adalberto-2-min.png", "2024/12/1-3.png", "2024/12/2-4.png", "2024/12/3.png", "2024/12/Kits-Trans-Resveratrol-Gotas-Canva.jpg"]
os.makedirs("img",exist_ok=True)
for p in L:
    dst="img/"+p.replace("/","-")
    if os.path.exists(dst): continue
    try:
        req=urllib.request.Request(O+p,headers={"User-Agent":"Mozilla/5.0"})
        open(dst,"wb").write(urllib.request.urlopen(req,timeout=30).read()); print("ok",dst)
    except Exception as e: print("ERRO",p,e)
