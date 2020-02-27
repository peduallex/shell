#Shell script
import sys
import os
import os.path
os.listdir
print '*************************************************'
print '*          Que tarefa deseja realizar?          *'
print '*************************************************'
print '* 1 - Encomendar uma ou mais BNCs?              *'
print '* 2 - Renovar o aluguer de uma ou mais BNCs?    *'
print '* 3 - Ver informa��es acerca da ActiveBNC?      *'
print '* 4 - Consultar informa��es de ajuda de BNCs?   *'
print '* 5 - Creditos?                                 *'
print '* 6 - Sair?                                     *'
print '*************************************************\n'
resposta_tarefa = int(raw_input('Escolha o n�mero correspondente � sua tarefa desejada! \n-> '))
print ' '
if resposta_tarefa == 1:
    x = 0
    while x <> 1 :
        print 'Processo de encomenda... Preencha abaixo o inqu�rito! (Todos os dados referidas s�o obrigat�rios!)'
        nome = raw_input('Digite o seu nome completo : ')
        mail = raw_input('Digite o seu email : ')
        tlm = raw_input('Digite o seu n�mero telefone : ')
        bnc = raw_input('Quantos BNCs deseja encomendar? ')
        print ' '
        print 'Confirme os seus dados : \n'
        print 'Nome : ' + nome
        print 'EMail : ' + mail
        print 'N�mero telefone : ' + tlm
        print 'BNCs desejadas : ' + bnc
        print ' '
        x = int(raw_input('Estes dados est�o correctos? (Yes [1] / No [2]) \n'))
        print 'Os seus dados foram enviados. Ser� contactado por email...'
        print 'Entretanto j� poder� efectuar o pagamento para este NIB: 0035 0171 00195068700 27'
        print 'Total a pagar ' + bnc*1 + '�'
        print 'Ap�s este pagamento, dever� enviar um mail para: marcsoler50@hotmail.com com o seu NIB e montante enviado!\n'
        print 'Obrigado!'
        import os
        import os.path
        os.chdir(r'windows/temp')
        os.mkdir('Aluguer')
        os.mkdir
        os.path.isdir('Aluguer')
        os.listdir('Aluguer')
#Tamb�m pode ser gravado com extens�o.doc
        os.chdir(r'windows/temp/aluguer')
        f = open('Aluguer.txt' , 'a')
        f.write('Nome : '+nome + '\n')
        f.write('Email : '+mail + '\n')
        f.write('Telefone : '+tlm +'\n')
        f.write('Numero de BNC(s) desejadas : '+bnc+ '\n')
        f.write('\n ')
        f.close()
elif resposta_tarefa == 2 :
     x = 0
     while x <> 1 :         
        print 'Processo de renova��o... Preencha abaixo o inqu�rito! (Todos os dados referidas s�o obrigat�rios!)'
        nome2 = raw_input('Qual o seu nome? ')
        mail2 = raw_input('Qual o seu email? ')
        bnc2 = raw_input('Quantas BNCs tem para renovar? \n')
        print 'Confirme os seus dados : \n'
        print 'Nome : ' +nome2
        print 'Email : ' +mail2
        print 'BNCs para renovar : ' + bnc2
        print ' '
        x = int(raw_input('Estes dados est�o correctos? (Yes [1] / No [2]) '))
        print 'Os seus dados foram enviados. Ser� contactado por email...'
        print 'Entretanto j� poder� efectuar o pagamento para este NIB: 0035 0171 00195068700 27'
        print 'Total a pagar ' + bnc2*1 + '�'
        print 'Ap�s este pagamento, dever� enviar um mail para: marcsoler50@hotmail.com com o seu NIB e montante enviado!\n'
        print 'Obrigado!'
        import os
        import os.path
        os.chdir(r'windows/temp')
        os.mkdir('Renova��o')
        os.mkdir
        os.path.isdir('Renova��o')
        os.listdir('Renova��o')
#Tamb�m pode ser gravado com extens�o.doc
        os.chdir(r'windows/temp')
        f = open('Renova��o.txt' , 'a')
        f.write('Nome : '+nome2 + '\n')
        f.write('Email : '+mail2)
        f.write('Numero de BNC(s) desejadas : '+bnc2)
        f.write('\n ')
        f.close()
elif resposta_tarefa == 3:
    print 'Descri��o em breve... Mais info em www.tfa-gaming.com/activebnc\n'
elif resposta_tarefa == 4:
    print 'Ajuda em breve'
elif resposta_tarefa == 5:
    print 'Shell Script desenvolvido'
elif resposta_tarefa == 6:
   exit()
else:
    print 'Inv�lido - Reinicie a aplica��o!'

