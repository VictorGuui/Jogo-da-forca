import Forca
import Adivinhacao
def escolhe_jogo():
   print('**************************')
   print('*****Escolha seu jogo*****')
   print('**************************')

   print('(1) forca (2) Advinhação')

   jogo=int(input('Qual jogo?'))

   if jogo==1:
      print('Jogo da Forca')
      Forca.jogar(Forca)
   elif jogo==2:
      print('Jogo da Advinhação')
      Adivinhacao.jogar(Adivinhacao)

if(__name__=='__main__'):
    escolhe_jogo()    
    




 






