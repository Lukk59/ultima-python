'''
Instruções: O roteiro foi criado para ajudar a fixar o conteúdo teórico desta semana. As soluções podem ser as mais simples possíveis, mas é bom tentar explicá-las ao máximo.. Você pode usar quaisquer ferramentas que julgar necessárias para exemplificar o cenário pedido.

Tutores: Caso você precise de ajuda para completar os exercícios, os tutores estão à disposição no chat do Telegram! 

Feedback: Os tutores vão revisar as atividades enviadas pela plataforma, na página da atividade, e darão feedback! 

Roteiro de Exercícios (para download)

Agora que você já está utilizando o GitHub, sugerimos manter suas atividades em um repositório.

Para enviar a atividade, por favor compartilhar o link do seu repositório e usar como título “Modulo3-Semana2”.

Caso isso não seja possível, envie o documento em formato Word or Python, via e-mail (giulia@ultima.school), indicando o seu nome, formação (Desenvolvedor Python), módulo e semana referente à atividade.
'''
'''
Formação Desenvolvedor Python 
Ultima.School
Módulo 3- Controle de versão do Git
Semana 2- Operações comuns do Git
Detalhes:

Instruções: Os exercícios foram criados para ajudar a fixar o conteúdo e praticar tudo que foi visto durante a semana. É muito importante que eles sejam implementados para fixar o conteúdo. As soluções podem ser o mais simples possível.

Tutores: Caso você precise de ajuda para completar os exercícios, os tutores estão a disposição no chat do telegram! 

Feedback: Os tutores vão revisar as atividades enviadas pela plataforma, na página da atividade; e vão dar feedback! 

Soluções/Gabarito: os alunos que tenham enviado as atividades, e já tenham recebido feedback; podem pedir acesso as soluções/gabarito dos exercícios se tiverem interesse. Este será liberado e estará disponível somente semanas após a conclusão do módulo em questão.
Exercícios:

1)Existem várias situações no fluxo de trabalho com Git onde podemos encontrar conflitos durante o merge de branchs.
Na grande maioria dos casos, poucas alterações no código podem resolver estes conflitos, sendo então necessário 
atualizar a branch em questão. Qual a sequência de passos deve ser seguida após um comando git merge falhar 
devido a conflitos?

R1:
 O Git tentaria combinar as alterações de maneira inteligente, mas quando não puder determinar qual alteração deve ser
integrada, o conflito deverá ser resolvido manualmente.
  Para realizar qualquer alteração do erro, iremos realizar o comando "pull" nessa "branch" ao terminamos qualquer 
alteração nela gerando uma nova "branch", utilizamos o comando "push", enviando a "branch" para o projeto remoto, 
se necessario, realizada qualquer alteração extra na nossa "branch" pelos demais colegas, talves seja necessario 
o uso do "rebase" para garantir a união dos dois projetos sem mais problemas. Caso esteja tudo bem, poderemos 
unila a "main" com o comando "merge", assim tornando as alterações realizadas parte do codigo principal "main".

2)Luizinho estava trabalhando em uma melhoria em seu código utilizando a branch feature/ABC123  quando colegas de 
trabalho lhe informaram de um bug em produção que precisa ser corrigido o quanto antes. O bug em questão estava no 
arquivo hello.py na branch main do repositório. Qual sequência de comandos git, Luizinho deve executar para corrigir 
o bug e voltar ao seu trabalho? Lembre-se que a empresa em que Luizinho trabalha segue à risca o GitFlow.

R2:
 Luizinho devera utilizar "git checkout hello.py" para mudar da "branch feature/ABC123" para a com o "bug", 
apos usar "git pull origin hello.py" para atualizar o repositorio local e fazer as alteraçoes necessarias para 
corrigir o "bug".
 Apos esta, com o "git add hello.py" as alteraçoes sao adicionadas ao repositorio local e o "git status" confirma 
que tais foram realizadas, com o "git commit -m “conserto de bugs”" se confirma que todas as alteraçoes estao corretas
e estao prontas para serem enviadas ao repositorio do git com o comando "git push origin hello.py".
 Onde elas poderao ser checadas pelos outros membros da equipe e de fato adicionadas ao "main" utilizando-se o 
comando "git merge hello.py", tanto num repositorio local quanto no proprio Github, onde fica o repositorio remoto.

3)No fluxo de trabalho de software a principal forma de sincronização de códigos é por meio de ferramentas de 
versionamento. A mais popular delas é amplamente difundida e é conhecida como git. Tendo em vista os temas 
abordados em aula, descreva a funcionalidade e exemplifique os comando git pull e git push.

R3:
 O Git é uma plataforma de versionamento simples, pratica e de graça, garantindo-lhe grande popularidade, 
sendo utilizado para trabalhos em equipe onde varios programadores tem acesso a um repositorio remoto e podem 
atravez do comando "git pull" sincronizar todas as alterações do GitHub com seus respectivos repositorios locais.
 Tem a habilidade de ver historico, conflitos de codigo e ate resolve-los automaticamente, alem de ser conectado 
a todas as maquinas com acesso ao repositorio remoto que permite os envolvidos mandarem suas alteraçoes para o 
site utilizando o comando "git push", para serem analisadas antes de serem adicionadas ao codigo principal.
 Outra importante funcionalidade do Git são as "branches" que permitem a criação de novos pedaços que aumentam o 
codigo de forma organizada e facilitando a visualização do historico de modificações, com o comando 
"git push − −set-upstream origin" que vai criar uma nova branch no repositorio remoto, provido que se 
tenha as credenciais necessarias.

4)Realize uma pesquisa sobre as diversas plataformas de versionamento como o git, escolha duas e realize um 
comparativo com o GitHub avaliando as semelhanças, diferenças, vantagens e desvantagens para o desenvolvimento 
de software.

R4:
 O GIT é uma das ferramentas de controle de versão de software muito utilizada, sendo a mais popular no mercado, 
especialmente em projetos open source.
 Devido a sua popularidade especialmente por ter sua propria plataforma para hospedagem de programas online, o Github. 
Ela tambem pode ser utilizada em outras ferramentas e é a que ganhou mais repercussão tambem nesse aspecto.
 Suas principais vantagens são seu design interno e interface, a eficacia e desempenho do software, ou seja,
ele é agradável de ser utilizado, consegue atingir todos os objetivos de controle de software bem rápido. 
 Entretanto é desvantajoso por sua complexa utilização.  possui controles um pouco mais complexos quanto comparado 
a outros, o que significa que seus colaboradores precisam entender conceitos mais profundos, relacionados a seu 
controle de versão de software, para utiliza-la corretamente. 
 É tambem uma ferramenta de controle de versão distribuída, o que significa que é adequado para a utilização em 
grandes equipes, onde os desenvolvedores não estão localizados geograficamente no mesmo local.

 O Subversion é uma ferramenta de controle de versão de software bastante utilizada no meio corporativo, indicada
somente para pequenas empresas ou trabalhos bem divididos, pois suporta somente grupos menores e em um mesmo espaço 
fisico por ser muito centralizada, diferente do Git que é uma ferramenta de controle de versão distribuída.
 Ela é rapida na execução das funcionalidades do sistema e ainda se mostra como uma das mais simples de ser 
empregada, ou seja, com um conhecimento básico de conceitos relacionados ao controle de versão de software é 
possível controla-la, tambem facilitando a aprendizagem da equipe, contrario ao Git.
 Apesar de ter tido problemas no passado, versões mais novas repararam sua eficacia e funcionamento, provando ser uma
ferramenta eficiente para sua utilidade especifica.

 O Mercurial é a ferramenta de controle de versão utilizada por grandes empresas como o Facebook e Google. Ela é muito
eficaz e rapida, superando tanto Git como Subversion, o que significa que consegue desempenhar suas funções de maneira
mais ideal que ambos.
 Executando seus comandos rapidamente sendo a mais funcional para equipes grandes, nas quais os desenvolvedores não 
estão todos trabalhando no mesmo local. Ja que ela é uma ferramenta de controle de versão distribuída, como o Git.
 Ela é mais complexa de ser utilizada em comparação com o Git e Subversion, mas ainda é de facil aprendizagem por 
desenvolvedores e possui medidas de segurança para impedir erros, como o Git.
'''