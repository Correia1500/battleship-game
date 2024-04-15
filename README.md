Inicialize o Git no seu projeto:

Abra o terminal no Visual Studio Code (Terminal > New Terminal).
Navegue até a pasta do seu projeto se ainda não estiver lá.
Execute git init para iniciar um novo repositório Git local.
Configure o remoto com git remote add origin [URL do Repositório].
Adicione os arquivos ao repositório Git:

Use git add . para adicionar todos os arquivos e pastas ao seu próximo commit, ou git add [caminho específico] para adicionar arquivos específicos.
Faça o commit das alterações:

Use git commit -m "Mensagem do Commit" para salvar suas alterações com uma mensagem explicativa.
Envie as alterações para o GitHub:

Use git push origin main para enviar suas alterações para o repositório GitHub.
Atualizando pastas com alterações de outros colaboradores
Atualize seu repositório local:
Use git pull origin main para puxar as últimas alterações do GitHub para seu repositório local.
Dicas para resolver dificuldades comuns
Conflitos de Merge:

Quando um conflito de merge ocorre, o Git irá notificar você. Abra os arquivos conflitantes e faça as correções necessárias manualmente, escolhendo as alterações que devem ser mantidas.
Depois de resolver os conflitos, adicione os arquivos resolvidos com git add [arquivo] e complete o merge com git commit.
Esqueceu de adicionar um arquivo no commit:

Se você esquecer de adicionar um arquivo antes de fazer um commit, você pode adicionar o arquivo e usar git commit --amend para adicionar o arquivo ao último commit.
Reverter um Commit:

Para desfazer alterações de um commit específico, use git revert [hash do commit]. Isso cria um novo commit que desfaz as alterações.