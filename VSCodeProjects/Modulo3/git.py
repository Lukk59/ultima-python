'''
Defina uma branch na qual irá trabalhar git checkout dev
Atualize o seu repositório local git pull origin dev
> Faça uma uma modificação qualquer no código e salve.

Visualize o status do seu arquivo com git status
> Você receberá a mensagem de que o arquivo foi modificado

Adicione para confirmar a alteração git add nome_arquivo
Confirme que está tudo certo git commit -m “comentário aqui”
Envie para o repositório remoto git push origin dev
Agora, você precisa entrar na branch principal e pegar as modificações enviadas para a branch dev;
Mude para a branch desejada git checkout master
Junte os arquivos da branch master com os arquivos enviados por você para a branch dev git merge dev
Fazendo isso, todas as alterações feitas e atualizadas na branch dev passarão a fazer parte da branch master (que, no exemplo, pode ser a branch utilizada para publicação do projeto).

Para entender melhor como as branches e as ramificações dentro de um projeto funcionam, existe um tutorial na documentação oficial do Git que mostra essa utilização. O link pode ser acessado aqui.

Essa foi uma abordagem utilizada como fluxo de trabalho. Em outros lugares, será preciso copiar uma branch (git checkout -b nova_branch) a partir de uma branch principal. Essa ação garante que a versão original do código seja preservada e permite revertê-la mais facilmente, caso erros ocorram.

Outra possibilidade é utilizar o comando git cherry-pick para pegar pequenas alterações feitas em branches provisórias antes do envio definido para a branch principal. Usado incorretamente, esse comando resulta em problemas de commit. Nesses casos, o comando git log pode ajudar.

Além disso, ainda podemos criar uma solicitação de pull request dentro de um projeto. O código deve ser validado por alguém para então ser publicado. 

Muita coisa né!? =) Todos esses processos e decisões variam conforme a realidade de cada projeto, por isso fique tranquilo(a).

Opções de correção

Eventualmente, erros ocorrerão na hora de enviar um arquivo e, para resolver isso, o Git também possui comandos para reverter um determinado ponto na linha do tempo. 

O comando git checkout funciona como o ctrl+z do windows, ele reverte a alteração feita em um arquivo fazendo com que retorne para o seu estado original.
Agora, imagine que fez muitas alterações em vários códigos e por algum motivo precisa desconsiderar tudo o que fez. Tentar desfazer “no olho” será muito complicado. Para voltar ao estado igual ao da branch principal, temos o comando git reset − −hard origin/master
'''
'''
Comandos básicos

Os comandos que podem ser utilizados são divididos em 14 grupos distintos. Uma lista completa dos comandos possíveis no GIT estão disponíveis no link oficial. Vale a pena conferir os exemplos de uso e as opções permitidas. Alguns dos comandos mais comuns estão listados a seguir:

 Comando	 Funcionalidade
 git init	 Cria um novo repositório
 git clone caminho_projeto	 Copia um projeto de um servidor remoto
 git status	 Exibe o status dos arquivos modificados
 git log	 Log do que foi feito
 git branch nome_branch	 Cria uma nova branch
 git branch -b nome_branch	 Copia os dados e cria uma branch nova
 git add nome_arquivo	 Permite que um arquivo seja monitorado e o adiciona à área de envio
 git add .	 Adiciona todos os arquivos de uma vez só
 git commit -m “”	 Permite confirmar a adição do arquivo e inserir um comentário
 git push origin nome_branch	 Envia os arquivos para o servidor remoto
 git pull origin nome_branch	 Atualiza o repositório local com os dados do servidor remoto
 git merge nome_branch	 Mescla arquivos de branches distintas
Não é preciso se preocupar em decorar todos esses comandos. Alguns são utilizados apenas em situações bem específicas e, com a prática do exercício contínuo de envio e manutenção dos arquivos em um projeto, conseguiremos lembrar deles naturalmente, fique tranquilo(a)! =)

Verdadeiro ou falso: podemos verificar o estado atual dos arquivos em um repositório Git com o comando “git status”.
'''
'''
Criando um repositório

Para criar um repositório na sua máquina local, siga os passos a seguir:

Crie uma pasta para armazenar o seu projeto;
Dentro da pasta, clique com o botão direito do mouse em qualquer área e selecione a opção ‘Git bash here’;
No terminal bash que aparece, digite o comando git init. Pronto, o seu repositório local para o projeto está criado (ponto 1);
Com isso, o Git cria uma branch com o nome  ‘master’ (ponto 2);
Crie um arquivo de texto (vazio mesmo) ou pegue o código anterior e salve dentro da pasta (ponto 3);
Digite o comando git status e visualize o resultado (ponto 4);

Uma mensagem é exibida informando que o arquivo criado ainda não está sendo monitorado, por isso fica com o texto na cor vermelha (ponto 5).
'''
'''
git clone https://github.com/ratopythonista/ultima-python.git
'''
'''
Uma vez com o repositório em nossa máquina, devemos abrir o terminal na pasta que foi criada. Se o comando foi realizado conforme as instruções mostradas anteriormente, essa pasta será ‘utlima-python’.

Podemos criar uma nova branch a partir do comando git checkout -b exemplo. Podemos observar se foi criado corretamente com o comando git branch, que listará todas as branches na sua máquina.

Utilizando o comando git checkout <nome_da_branch>,  podemos navegar entre as branches do repositório, como na imagem a seguir.
'''
'''
Após adicionar um arquivo qualquer no repositório — neste caso, teste.py contendo apenas um print —, vamos realizar as etapas necessárias para enviar esse arquivo para o nosso repositório no GitHub.

Primeiramente, precisamos adicionar todos os arquivos novos do repositório com git add, e podemos checar se tudo foi adicionado com git status.

Em seguida, devemos realizar o commit com o comando git commit -m “comentário qualquer”, evidenciando que as alterações que realizamos estão prontas para serem enviadas para o GitHub, assim como na imagem.
'''
'''
Para enviar as alterações que realizamos para o GitHub, precisaremos utilizar o comando git push que, nesse caso, apresentará erro, uma vez que não temos essa branch na nuvem, apenas localmente. Então ele indicará um novo comando git push − −set-upstream origin exemplo, que funcionará e pedirá suas credenciais, como mostrado na figura.
'''
'''
O comando git pull não terá nenhum efeito no nosso repositório, uma vez que ele é responsável por sincronizar todas as alterações do GitHub com nosso repositório.

Mas é importante saber que este comando está disponível e será utilizado durante a formação! 
'''
'''
Nesse arquivo README estamos definindo:

 Tipo da Tag	 Descrição
 Titulo de Nível 1	 A tag de título consiste em duas linhas. A primeira linha contém o texto do título, enquanto a segunda linha delimita que o texto deve ser um título de nível 1. Demonstrado nas linhas 1 e 2.
 Titulo de Nível 2	 Funciona da mesma forma que o título de nível 1, mas usamos o caractere de traço. Está sendo demonstrado na linha 7 e 8.
 Texto com link	 Essa tag adiciona um link a um determinado texto, tornando-o clicável. Dessa forma, após ler o texto, pode-se clicar nele para ir a outra página. Demonstrado na linha 15.
 Texto em negrito	 Para aplicar o efeito negrito a um texto, devemos usar “**” antes e depois do trecho selecionado. Demonstrado na linha 17.
 Texto em itálico	 Para aplicar o efeito itálico a um texto, devemos usar “*” antes e depois do trecho selecionado. Demonstrado na linha 17.
 Texto com negrito e Itálico	 Para aplicar ao mesmo tempo os efeitos negrito e itálico a um texto, devemos usar “***” antes e depois do trecho selecionado. Demonstrado na linha 17.
 Bloco de código	 Essa tag é usada quando precisamos criar um bloco de código no texto. Para isso adicionamos os caracteres ““`” em volta do código. Demonstrado nas linhas 23, 24 e 25.
Existem diversas outras tags disponíveis na documentação do Github. Vale lembrar que esse não é um formato exclusivo para o Github, mas a documentação contém mais informações do que é compatível com a plataforma.

Após enviar o código do README para o servidor, será exibido algo assim na tela inicial do projeto:
Existem algumas ferramentas que nos ajudam a escrever os arquivos em Markdown. Para quem está usando o Visual Studio Code, basta abrir a paleta de comandos e pesquisar por “Markdown: Open Preview to the Side”, que terá uma noção de como está ficando o arquivo.
'''