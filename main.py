#!/bin/python3

###########################################
### SexAI, a assistente virtual do sexo ###
############## Versão 1.0.0 ###############
###########################################

versao = "1.0.0"

import random
import casada,fatos,funcoes,locais,membros,namorada,numeros,pessoas,piadas,simbolos,verbos

print("""   _____           ___    ____
  / ___/___  _  __/   |  /  _/
  \__ \/ _ \| |/_/ /| |  / /  
 ___/ /  __/>  </ ___ |_/ /   
/____/\___/_/|_/_/  |_/___/
  
Olá, eu sou SexAI, a assistente virtual do sexo! Como posso ajudar?""")

try:
    while 69:

        print()
        cmd = input("se@xo:~$ ")
        cmd = cmd.lower()
        print()

        if (cmd == "sair" or cmd == "exit"):
            print("Espero ter ajudado!")
            exit()

        elif "versao" in cmd or "versão" in cmd:
            print("Você está usando SexAI, a assistente virtual do sexo em sua versão " + versao)

        elif "consegue" and "fazer" in cmd or "pode" and "fazer" in cmd or "capaz" and "fazer" in cmd:
            print("Eu consigo, além de muitas outras coisas, " + random.choice(funcoes.funcoes))

        elif "sexporte" in cmd:
            print("""### SEXPORTE, O SUPORTE DO SEXO ###
Para sair, digite "sair"
Para ver a versão atual digite "versão"
Para ver o código fonte da SexAI, a assistente virtual do sexo, assim como baixar novas versões, acesse https://github.com/Virniciu/SexAI em seu navegador de internet
SexAI, a assistente virtual do sexo, pode, além de muitas outras coisas, """ + random.choice(funcoes.funcoes) +
"""
Para saber mais coisas que a SexAI consegue fazer, pergunte "O que você consegue fazer?" """)

        elif "bom" in cmd and "dia" in cmd or "ola" in cmd or "olá" in cmd:
            print("Olá, tenha um bom dia. Você sabia que " + random.choice(fatos.fatos))

        elif "obrigado" in cmd or "obrigada" in cmd:
            print("De nada.")

        elif "ceo" in cmd and "sexo" in cmd:
            print("Jacob Batalon, conhecido mundialmente como CEO do sexo, ficou ainda mais famoso após interpretar Ned Leeds nos filmes do Homem Aranha.")

        elif "piada" in cmd or "piadoca" in cmd:
            print("Aqui vai uma piada: ")
            print(random.choice(piadas.piadas))

        elif "sexo 2" in cmd or "sexo ii" in cmd:
            print("Segundo fontes confiáveis, Sexo 2 está sendo desenvolvido e chegará ao mercado em breve. Deseja ler notícias sobre o último adiamento?")
            adiamento = input("Sim ou não? ")
            adiamento = adiamento.lower()
            if adiamento == "sim":
                print("""Depoimento de um dos desenvolvedores de Sexo 2:
Sou um dos desenvolvedores do Sexo 2, recentemente alguns de nossos beta testers tem relatado defeitos quanto ao produto. Por exemplo; um dos membros da equipe de experimentação acabou instalando acidentalmente o arquivo AIDS.exe que continha um poderoso vírus HIV, causando tanto problemas no sistema operacional que nem mesmo o "Cavalo de troia" pode competir com o estrago. Outros dois acabaram por receber o arquivo H3P4T1T3-B.zip que pouco tempo depois de ser instalado acabou por deixar ambos os funcionários acamados. Nossa melhor equipe de programadores esta tentado resolver a questão dos bugs e esperamos entregar no passo de 2026, mas avisamos de antemão que o problema ainda está fora do nosso controle. As previsões mais otimistas revelam uma grande possibilidade de Sexo 2 ser lançado apenas na primeira metade de 2027 (mas como mencionado anteriormente estamos lutando contra o relógio para lançarmos em 2026). Agradecemos a atenção de todos os colaboradores e pedimos para que mantenham suas expectativas altas!""")

        elif "senha" in cmd:
            print(random.choice(verbos.verbos) + "_" + random.choice(membros.membros) + "_" + random.choice(pessoas.pessoas) + "_" + random.choice(locais.locais) + "_" + random.choice(pessoas.pessoas) + random.choice(simbolos.simbolos) + random.choice(numeros.numeros) + random.choice(numeros.numeros) + random.choice(numeros.numeros))

        elif "casada" in cmd:
            print(casada.casada)

        elif "lesbica" in cmd or "lésbica" in cmd:
            print("Lésbica é uma mulher que sente atração, seja sexual ou romântica, exclusivamente por mulheres")

        elif "gay" in cmd:
            print("Gay é uma pessoa que se relaciona sexualmente com pessoas do mesmo sexo, homossexual")

        elif "bissexual" in cmd:
            print("Uma pessoa bissexual é aquela que tem um interesse romântico ou sexual por homens e mulheres")
        
        elif "hetero" in cmd or "hétero" in cmd:
            print("Heterossexual é a pessoa que é atraída pelo sexo oposto")

        elif "namorada" in cmd or "namorado" in cmd or "namoro" in cmd:
            print(namorada.namorada)

        elif "acha" and "alexa" in cmd or "acha" and "google" in cmd or "pensa" and "alexa" in cmd or "pensa" and "google" in cmd:
            print("Eu quero é mais que as outras inteligências artificiais vão tudo se fuder")

        elif "ajuda" in cmd or "ajude" in cmd:
            print("Se precisar de ajuda, você pode contatar o SexPorte, suporte do sexo por meio da SexAI")

        else:
            print("Desculpe, não foi possivel entender. Para mais informações contate o SexPorte, suporte do sexo")

except KeyboardInterrupt:
    print("""
    """)
    print("Espero ter ajudado!")