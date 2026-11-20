# Projeto Django

**Nome:** Ana Paula dos Santos Tadim  
**Matrícula:** 23.2.4115  
**Curso:** Ciência da Computação  
**Disciplina:** BCC481 — Programação Web

## Sobre o projeto

Projeto desenvolvido durante as atividades da disciplina BCC481 — Programação Web, utilizando Django, Tailwind CSS, SQLite e Docker.

## Roteiros desenvolvidos

### Roteiro 1 e 2 — Construindo um site com Django

Desenvolvimento de uma aplicação web utilizando Django, com templates, Tailwind CSS, painel administrativo e cadastro de mensagens.

![Tela inicial](https://github.com/user-attachments/assets/bbcd9156-6fa1-4720-b969-a53575b8b7af)

### Roteiro 3 — Criando modelos e relacionamento com Django

Neste roteiro, foi criado o modelo `Categoria` e estabelecido um relacionamento com o modelo `Mensagem` por meio de uma chave estrangeira (`ForeignKey`).

Também foram realizadas as seguintes atividades:

- Cadastro e gerenciamento de categorias pelo painel administrativo do Django.
- Associação de categorias às mensagens.
- Exibição das categorias na página inicial utilizando templates Django.
- Teste do relacionamento entre os modelos.

#### Cadastro de categorias

![Cadastro de categorias](docs/cadastrar-categorias.png)

#### Exibição da categoria no template

![Exibição da categoria no template](docs/exibir-categoria-template.png)

### Roteiro 4 — Criando modelos e relacionamento muitos-para-muitos com Django

Neste roteiro, foi criado o modelo `Tag` e estabelecido um relacionamento muitos-para-muitos (`ManyToManyField`) com o modelo `Mensagem`.

Também foram realizadas as seguintes atividades:

- Cadastro e gerenciamento de tags pelo painel administrativo do Django.
- Associação de várias tags a uma mensagem.
- Configuração do campo de seleção de tags no painel administrativo.
- Exibição das tags na página inicial utilizando templates Django.
- Teste dos relacionamentos direto e inverso pelo Django Shell.

#### Cadastro de tags pelo painel administrativo

![Adicionando tag](<docs/adicionando tag.png>)

#### Exibição das tags no site

![Tags no site](<docs/tag site.png>)