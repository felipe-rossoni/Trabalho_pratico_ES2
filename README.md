Trabalho Prático - Microsserviços de Câmbio

Este projeto contém dois microsserviços mockados para consulta de câmbio e histórico, orquestrados via Docker Compose e com CI configurado.

Estrutura

currency-report: Serviço na porta 8100 (Cotação atual).

currency-history: Serviço na porta 8101 (Histórico).

Como Executar (Docker Compose)

Para subir todo o ambiente localmente:

Certifique-se de ter o Docker e Docker Compose instalados.

Na raiz do projeto, execute:

docker compose up --build


Isso irá compilar as imagens e iniciar os containers.

Como Testar

Você pode testar via navegador ou terminal (curl).

Serviço A (Report)

Health Check:

curl http://localhost:8100/health


Cotação:

curl "http://localhost:8100/quote?from=USD&to=BRL"


Serviço B (History)

Health Check:

curl http://localhost:8101/health


Histórico:

curl "http://localhost:8101/history?from=USD&to=BRL"


CI/DevOps

O projeto possui um workflow do GitHub Actions configurado em .github/workflows/ci.yml.
Ele executa automaticamente:

Setup do ambiente Python.

Instalação de dependências.

Testes unitários (pytest) em ambos os serviços.

Build de verificação das imagens Docker.