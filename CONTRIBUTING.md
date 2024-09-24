# Contribuindo para o Projeto Smart Relationship of Clients 🤝

Bem-vindo ao projeto Smart Relationship of Clients! Obrigado por considerar contribuir para o nosso projeto! Siga as instruções abaixo para configurar o ambiente de desenvolvimento.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas na sua máquina:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [VScode](https://code.visualstudio.com/download)

## ⚙️ Configuração rapida do projeto

### Clone o Repositório

Abra seu terminal e navegue até o diretório onde deseja clonar o repositório. Em seguida, execute o comando abaixo:

```bash
git clone https://github.com/Rvjq/SRC-Fundamentos-de-Desenvolvimento-de-Software.git
```

### Navegue até o Diretório do Projeto
Use o comando

```bat
cd SRC-Fundamentos-de-Desenvolvimento-de-Software
```

### 💻 Criando virtual environment

>Criar venv

```powershell
python.exe -m venv env 
```

>Caso esteja sendo configurado em um computador do Cesar :shipit: executar o seguinte Script

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

>Ativar venv

```powershell
./env/Scripts/activate
```

>Instalar Dependencias do projeto (libs)

```powershell
pip.exe install -r requirements.txt
```

>O seguinte script atualiza a lista de dependencias (libs)

```powershell
python.exe -m pip freeze > requirements.txt
```

### 🏃 Rodando o Servidor Dev Local

>Navegue para a pasta Raiz do projeto

```bat
cd SRC
```

>Rode o servidor

```powershell
python.exe manage.py runserver
```

## Contribuindo com Código

Recomendamos o uso do Visual Studio Code (VSCode) para desenvolver o projeto. Para abrir o projeto no VSCode, siga os passos abaixo:

### Abra o VSCode.

Clique em File > Open Folder... e selecione o diretório do projeto SRC.
Certifique-se de que o ambiente virtual esteja ativado no terminal do VSCode.

crie um Fork do repositório.
Clone seu fork localmente.
Crie uma branch para sua modificação:

```bash
git checkout -b nova-feature
```

Faça suas mudanças.

> Commit suas mudanças:

```bash
git commit -m "Adicionar nova feature"
```

> Push para a branch:

```bash
git push origin nova-feature
```

> Abra um Pull Request.

### Processo de Revisão

Nossa equipe irá analisar todos os pull requests. Apenas aqueles que forem coerentes e estiverem alinhados com os objetivos do projeto serão aprovados.

# Dúvidas?

Se tiver qualquer dúvida, sinta-se à vontade para abrir uma issue.