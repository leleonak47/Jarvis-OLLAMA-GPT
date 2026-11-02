# Jarvis AI Assistant

Assistente pessoal desenvolvido em Python, integrado ao Ollama para execução de modelos de inteligência artificial localmente.

O objetivo do projeto é desenvolver um assistente capaz de interpretar solicitações em linguagem natural, processar informações e interagir com recursos locais, como bancos de dados.

## Tecnologias utilizadas

- Python
- Ollama
- LLM: GPT-OSS 20B
- SQL Server
- ODBC Driver 18 for SQL Server

## Pré-requisitos

Antes de executar o projeto, é necessário instalar:

- Python
- Ollama
- SQL Server
- Microsoft ODBC Driver 18 for SQL Server

Também é necessário baixar o modelo utilizado pelo projeto:

```bash
ollama pull gpt-oss:20b
```

## Instalação

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

2. Acesse a pasta do projeto:

```bash
cd Jarvis
```

3. Crie um ambiente virtual:

```bash
python -m venv .venv
```

4. Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração do ambiente

O arquivo `.env` não está incluído neste repositório por questões de segurança, pois contém configurações locais e credenciais de acesso.

Antes de executar o projeto, você deverá criar manualmente um arquivo chamado `.env` na raiz do projeto, utilizando o exemplo abaixo:

```env
# .env
OLLAMA_HOST=http://localhost:11434
LLM_MODEL=gpt-oss:20b
DB_CONN_STR=DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=JarvisDB;UID=sa;PWD=SuaSenha
```

**Importante:**
- Altere `SuaSenha` para a senha do seu SQL Server.
- Certifique-se de que o SQL Server esteja instalado e em execução.
- O Ollama deve estar instalado e disponível no endereço configurado.
- O modelo `gpt-oss:20b` deve estar instalado no Ollama.

## Configuração do banco de dados

O projeto utiliza o SQL Server para armazenar os registros das conversas realizadas com o assistente.

Antes de executar o Jarvis pela primeira vez, é necessário criar o banco de dados e sua tabela de logs.

Execute o script abaixo no SQL Server Management Studio (SSMS):

```sql
-- 1. Criar o banco de dados
CREATE DATABASE JarvisDB;
GO

-- 2. Selecionar o banco de dados
USE JarvisDB;
GO

-- 3. Criar a tabela de logs
CREATE TABLE Logs (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    SessionId UNIQUEIDENTIFIER NOT NULL,
    Timestamp DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    UserInput NVARCHAR(MAX),
    AssistantOutput NVARCHAR(MAX)
);
GO
```

Após executar o script, confirme se o banco `JarvisDB` e a tabela `Logs` foram criados corretamente.

## Executando o projeto

Depois de concluir as configurações:

1. Verifique se o arquivo `.env` está preenchido corretamente.
2. Confirme se o banco de dados `JarvisDB` está acessível.
3. Verifique se o Ollama está em execução.
4. Execute o projeto:

```bash
python main.py
```

## Estrutura do projeto

```text
Jarvis/
├── main.py
├── modules/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Status do projeto

Em desenvolvimento.

Novas funcionalidades, melhorias de desempenho e integrações serão adicionadas gradualmente.

## Autor

Desenvolvimento pessoal.