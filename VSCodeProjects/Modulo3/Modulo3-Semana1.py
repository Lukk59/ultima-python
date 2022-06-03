'''Formação Desenvolvedor Python 
Ultima.School
Módulo 3 - Controle de versão com GIT
Semana 1- Iniciando com Sistema de controle de Versionamento
Detalhes:

Instruções: O roteiro foi criado para ajudar a fixar o conteúdo teórico desta semana. As soluções podem ser o mais 
simples possível, mas é bom tentar explicar o máximo possível. Você pode usar quaisquer ferramentas que julgar 
necessário para exemplificar o cenário pedido

Tutores: Caso você precise de ajuda para completar os exercícios, os tutores estão à disposição no chat do telegram! 

Feedback: Os tutores vão revisar as atividades enviadas pela plataforma, na página da atividade; e vão dar feedback! 

Soluções/Gabarito: os alunos que tenham enviado as atividades, e já tenham recebido feedback; podem pedir acesso 
às soluções/gabarito dos exercícios se tiverem interesse. Este será liberado e estará disponível somente semanas 
após a conclusão do módulo em questão para os alunos que concluíram as atividades.
Roteiro

Cenário1: Você trabalha em uma equipe que deseja utilizar o git em seus projetos, vocês já possuem um repositório 
criado e precisam configurar o repositório (configurações do projeto, bibliotecas, documentação e etc) para 
começarem a trabalhar.

Descreva o que deverá ser feito para conseguir realizar o cenário acima. Lembre-se de que é necessário efetuar 
a configuração e disponibilizá-la para os demais colegas de equipe. Cite comandos que serão usados, qual a ordem 
que serão usados e etc.

R1: 
 Cria-se um "README file" com os objetivos do seu projeto, apos isso realiza-se o primeiro "commit" do projeto nesse
"file", apos iremos adicionar os coautores utiliziando seus emails da conta do "github", assim dando a eles 
autorização de mudar o projeto que sera o "main".
 Usamos o comando "clone" do GIT para copiar o repositório todo para nossa maquina pessoal, onde poderemos dar nossos
proprios "commit" pessoais criando nossa "branch" e para garantir que a branch local esteja atualizada, é 
necessário usar o comando de "pull" do GIT, realizando as alterações feitas no "main" para o nosso projeto local.
 Uma vez que terminamos a alteração local utilizamos o comando "push", enviando a "branch" para o projeto remoto
para que os outros colegas de equipe possam atualizar o código deles com a última versão criada, ou realizar qualquer
correção necessaria.
 Ao precisar trocar entre branches criadas, seja para a "main" ou para a "branch" que estamos trabalhando, vamos
utilizar o comando de "checkout", ele ira fazer essa troca. Assim nos permitindo fazer qualquer mudanças mesmo no 
meio do trabalho.
 Uma das formas de correção seria o comando "rebase" que ira fazer uma união dos códigos, inserindo todos os 
"commits" de "branch" no "main" antes dos "commits" da nossa branch para so depois aplicar cada um dos nossos. 
Desta forma conseguimos resolver cada conflito da união do código de forma faseada e somente os conflitos de cada 
um dos "commits" da "branch" que estamos trabalhando ao invés de resolvermos todos de uma vez só.
 Apos realizada qualquer alteração na nossa "branch" com o numero necessario de "commit" poderemos unila a 
"main" com o comando "merge", assim tornando as alterações realizadas parte do codigo principal "main".
 Quando tudo estiver finalizado, iremos gerar uma versão do nosso sistema para enviarmos para produção. 
Para gerar essa versão usamos o comando "tag" que irá marcar os "commits" com uma “etiqueta” na versão atual.

Cenário2: Você e seus colegas de equipe estão trabalhando em cima do mesmo conjunto de arquivos. Você precisa de 
uma atualização no seu repositório que algum de seus colegas acabou de finalizar e fez o merge para a branch main.

Descreva o que deverá ser feito para conseguir realizar o cenário acima. Cite comandos que serão usados, qual a 
ordem que serão usados e etc

R2:
 Utilizando o comando "pull" poderemos puxar do "main" o trabalho realizado pelo nosso colega, talves seja necessario
o uso do "rebase" para garantir a união dos dois projetos sem mais problemas.

Cenário3: Após um dia de trabalho você finalizou a codificação de uma tarefa e precisa unir o seu código com a 
main branch.

Descreva o que deverá ser feito para conseguir realizar o cenário acima. Cite comandos que serão usados, qual 
a ordem que serão usados e etc

R3:
 Uma vez que terminamos a alteração local utilizamos o comando "push", enviando a "branch" para o projeto remoto,
se necessario realizada qualquer alteração extra na nossa "branch", se não poderemos unila a "main" com o 
comando "merge", assim tornando as alterações realizadas parte do codigo principal "main". 

Cenário4: A sua equipe estava tendo muitos problemas com o versionamento do código e decidiu pensar em uma 
estratégia para poder organizar melhor o código através de “versões candidatas” para produção. Para isso foi 
decidido criar uma nova branch com o padrão de nome “rc_v150” (abreviação para “Release Candidate Version 1.5.0”) 
para a primeira versão a ser usada nesta nova estratégia.

Descreva o que deverá ser feito para conseguir realizar o cenário acima. Lembre-se de comentar como que a equipe 
irá unir o código nessa branch, como criá-la e etc. Cite comandos que serão usados, qual a ordem que serão 
usados e etc

R4:
 Para realizar qualquer alteração nessa nova "branch", iremos realizar o comando "pull" nessa "tag" ao terminamos 
qualquer alteração nela, utilizamos o comando "push", enviando a "branch" para o projeto remoto, se necessario, 
realizada qualquer alteração extra na nossa "branch" pelos demais colegas, talves seja necessario o uso do "rebase" 
para garantir a união dos dois projetos sem mais problemas. Se não, poderemos unila a "main" com o comando "merge", 
assim tornando as alterações realizadas parte do codigo principal "main" e criando uma nova "tag", por seguraça.

Cenário5: Após analisar um problema no código, você fez uma proposta do que precisa ser alterado para que o bug 
seja resolvido. Para realizar a correção, será necessário criar uma branch, codificar a correção e enviar o 
código para que outras pessoas do time possam avaliá-lo.

Descreva o que deverá ser feito para conseguir realizar o cenário acima. Lembre-se. Cite comandos que serão usados, 
qual a ordem que serão usados e etc

R5:
 Para realizar qualquer alteração do erro, iremos realizar o comando "pull" nessa "branch" ao terminamos qualquer 
alteração nela gerando uma nova "branch", utilizamos o comando "push", enviando a "branch" para o projeto remoto, 
se necessario, realizada qualquer alteração extra na nossa "branch" pelos demais colegas, talves seja necessario 
o uso do "rebase" para garantir a união dos dois projetos sem mais problemas. Caso esteja tudo bem, poderemos 
unila a "main" com o comando "merge", assim tornando as alterações realizadas parte do codigo principal "main".

'''
'''
Instruções: O roteiro foi criado para ajudar a fixar o conteúdo teórico desta semana. As soluções podem ser o 
mais simples possível, mas é bom tentar explicar o máximo possível. Você pode usar quaisquer ferramentas que 
julgar necessário para exemplificar o cenário pedido

Tutores: Caso você precise de ajuda para completar os exercícios, os tutores estão à disposição no chat do telegram! 

Feedback: Os tutores vão revisar as atividades enviadas pela plataforma, na página da atividade; e vão dar feedback! 

Agora que você já está utilizando o GitHub, sugerimos manter suas atividades em um repositório.

Para enviar a atividade por favor compartilhar o link do seu repositório, e usar titulo como “Modulo3-Semana1”.

Caso isso não seja possível, envie o documento em formato Word or Python, via e-mail (giulia@ultima.school), 
indicando o seu nome, formação (Desenvolvedor Python), módulo e semana referente à atividade.

You have now created a repository, including a README file, and created your first commit on GitHub.com.

You can now clone a GitHub repository to create a local copy on your computer. From your local repository you can commit, and create a pull request to update the changes in the upstream repository. For more information, see "Cloning a repository" and "Set up Git."
You can find interesting projects and repositories on GitHub and make changes to them by creating a fork of the repository. Forking a repository will allow you to make changes to another repository without affecting the original. For more information, see "Fork a repository."

Each repository on GitHub is owned by a person or an organization. You can interact with the people, repositories, and organizations by connecting and following them on GitHub. For more information, see "Be social."

GitHub has a great support community where you can ask for help and talk to people from around the world. Join the conversation on GitHub Support Community.
'''

