# CLASSES 
### O CONCEITO DE CLASSE

A Programação Orientada a Objetos é um paradigma que nos permite modelar problemas complexos de forma mais próxima ao mundo real. Diferente da programação tradicional, que foca em sequências lineares de instruções, a POO organiza o software em torno de "objetos". Mas, para entendermos o que é um objeto, precisamos primeiro compreender a sua origem e essência: a Classe.

Para definir o que é uma classe de maneira técnica, podemos recorrer a Grady Booch, um dos pioneiros e principais autores sobre o tema, que em sua obra clássica *"Object-Oriented Analysis and Design with Applications"* descreve a classe como uma construção que define os atributos e operações comuns a um conjunto de objetos.

Em termos didáticos, uma classe é um modelo, um molde, uma planta baixa ou um projeto. Ela não é a coisa em si, mas sim a descrição teórica de como essa coisa deve ser construída.

Pense na planta baixa de um edifício. A planta (a classe) contém todas as especificações de como o prédio deve ser: quantos quartos terá, qual a metragem, como as portas se abrem. No entanto, você não pode morar dentro da planta baixa; você precisa construir o prédio físico baseado nela. Na POO, a classe é exatamente essa planta baixa.

Toda classe possui dois componentes fundamentais:

1. **Atributos (ou Propriedades):** São as características, os dados ou o "estado" do objeto.

2. **Métodos (ou Comportamentos):** São as ações que o objeto pode realizar ou as funções que ele executa.

Vamos a um exemplo prático. Imagine a classe "Carro". 

Quais seriam seus atributos? Cor, modelo, ano de fabricação, velocidade atual. 
Quais seriam seus métodos? Ligar o motor, acelerar, frear, buzinar.

A grande vantagem de utilizarmos classes é a organização e a reutilização. Em vez de programar cada carro individualmente do zero, nós criamos a classe "Carro" uma única vez. A partir desse modelo centralizado, garantimos que todos os carros gerados a partir dela terão a mesma estrutura base.

Portanto, a classe é a fundação de todo o paradigma orientado a objetos. Ela encapsula dados e comportamentos em uma única entidade lógica, servindo como o projeto definitivo para a criação dos elementos que comporão o nosso sistema. Compreender a classe como um "molde" é o primeiro e mais importante passo para dominar a POO.

***
#  INSTANCIAÇÃO

### CONCEITO DE INSTANCIAÇÃO

Nesta segunda parte, focaremos exclusivamente no conceito de **Instanciação**. Assim como antes, manteremos o texto puramente teórico e didático, sem nenhum código, para que vocês absorvam a essência do conceito.

Se a classe é a ideia, o projeto, a planta baixa, ela por si só é estática. Você não pode morar em uma planta baixa, nem pode dirigir um projeto no papel. Para que o nosso sistema de software ganhe vida e possa ser executado, precisamos transformar essa abstração em algo concreto. É exatamente aqui que entra o conceito de Instanciação.

**O que é Instanciação?**

Em termos técnicos, instanciação é o processo de criação de um **objeto** (também chamado de **instância**) a partir de uma classe. Quando dizemos que estamos "instanciando" uma classe, estamos ordenando ao computador que reserve um espaço na sua memória RAM e construa, de fato, a entidade descrita naquele modelo.

Para ilustrar de forma didática, imagine uma forma de silicone para fazer chocolates. A forma de silicone é a nossa classe: ela define o formato, o tamanho e o desenho. Porém, você não come a forma de silicone. Para ter o chocolate em si, você precisa derramar o chocolate líquido na forma e deixá-lo solidificar. O ato de criar o chocolate físico é a instanciação. Cada chocolate individual que sai dessa forma é uma "instância" da classe "Forma de Chocolate".

O que acontece nos bastidores do computador durante a instanciação?

1. **Alocação de Memória:** O computador lê a classe e calcula quanto espaço será necessário para guardar as características (atributos) daquele objeto.

2. **Inicialização:** O computador executa uma rotina especial (chamada de construtor) para definir os valores iniciais das características. É o momento em que dizemos "este objeto específico terá a cor vermelha" ou "este objeto específico terá o modelo fusca".

Um dos conceitos mais importantes e poderosos da instanciação é a **independência**. Como cada instância ganha seu próprio espaço na memória, elas são totalmente independentes entre si. Se você pegar um chocolate e pintá-lo de branco, o outro chocolate continuará da cor original. No software, se alterarmos a velocidade de um carro instanciado, o outro carro instanciado a partir da mesma classe não será afetado. Eles compartilham o mesmo modelo, mas possuem estados e memórias separados.

O cientista da computação Grady Booch, em sua obra de referência *"Object-Oriented Analysis and Design with Applications"*, reforça essa distinção ao definir que, enquanto a classe descreve a estrutura e o comportamento comuns, a instância é a realização concreta e individualizada de uma classe específica durante a execução do programa.

Portanto, a instanciação é a ponte entre o mundo abstrato do design (a classe) e o mundo concreto da execução (o objeto). Sem a instanciação, as classes seriam apenas definições teóricas inertes. É através dela que multiplicamos um único modelo em diversos objetos funcionais e independentes, dando verdadeira vida e utilidade ao nosso programa.

---
# CLASSES PURAS OU ABSTRATAS

## CONCEITOS DE CLASSES PURAS OU ABSTRATAS

Nas etapas anteriores, entendemos que a Classe é a planta baixa e que a Instanciação é o ato de construir o objeto físico a partir dela. Mas agora surge uma pergunta muito interessante: **e se existirem plantas baixas que nunca deveriam ser construídas diretamente?**

É exatamente sobre isso que vamos conversar agora. Nesta terceira e última parte teórica, focaremos exclusivamente no conceito de **Classes Puras ou Abstratas**.

Até este momento, todas as classes que criamos eram o que chamamos de **classes concretas**. Isso significa que elas eram completas o suficiente para serem instanciadas, ou seja, para gerarem objetos funcionais. A classe "Carro" gerava carros, a classe "Chocolate" gerava chocolates. Faz sentido, certo?

Porém, à medida que os nossos sistemas de software crescem e se tornam mais complexos, nos deparamos com situações em que precisamos criar classes que servem apenas como **modelos genéricos**, como categorias amplas que não fazem sentido sozinhas no mundo real. É aqui que entram as Classes Abstratas.

**O que são Classes Abstratas?**

Uma classe abstrata (também chamada de classe pura em algumas linguagens, como C++) é uma classe que **não pode ser instanciada diretamente**. Ela é um modelo incompleto de propósito, projetado para ser a base de outras classes mais específicas.

Para entender isso de forma didática, vamos pensar no conceito de "Animal". Se eu pedir para você imaginar um animal, você provavelmente pensará em um cachorro, um gato, um pássaro ou um peixe. Mas ninguém imagina um "animal genérico" andando pela rua. O conceito de "Animal" é muito amplo e abstrato. Ele existe como uma categoria, mas não como um ser concreto.

No entanto, todos os animais compartilham certas características: eles têm um nome, uma idade e precisam se alimentar. O que muda é **como** cada um se alimenta. Um cachorro come ração, um pássaro come sementes, uma baleia filtra plâncton.

É exatamente isso que uma classe abstrata faz no software: ela define **o que** os objetos devem ter e **o que** eles devem fazer, mas deixa para as classes filhas (as classes concretas) a responsabilidade de definir **como** fazer.

A classe abstrata "Animal" diria: *"Todo animal que descender de mim OBRIGATORIAMENTE terá um nome e OBRIGATORIAMENTE saberá se alimentar. Mas eu não vou dizer como se alimentar, porque isso depende de cada espécie."*

Essas obrigações que a classe abstrata impõe são chamadas de **métodos abstratos**. Um método abstrato é como um contrato: ele declara que a ação deve existir, mas não fornece a implementação (o código de como executar). Quem herdar essa classe será obrigado a preencher esse contrato.

O engenheiro de software Robert C. Martin, em sua obra *"Agile Software Development: Principles, Patterns, and Practices"*, destaca que as abstrações são fundamentais para criar sistemas flexíveis, pois permitem que o código dependa de conceitos gerais em vez de detalhes específicos.

Grady Booch, em *"Object-Oriented Analysis and Design with Applications"*, complementa essa visão ao explicar que a abstração é o mecanismo que nos permite focar nos detalhes essenciais de um objeto e ignorar os irrelevantes para o contexto do problema.

Portanto, as classes abstratas são ferramentas poderosas de organização e planejamento. Elas funcionam como "contratos" ou "modelos mestres" que garantem que todas as classes derivadas sigam uma mesma estrutura, promovendo consistência e segurança no nosso código. Elas não existem para serem usadas diretamente, mas sim para serem a fundação sobre a qual as classes concretas serão construídas.

Com isso, fechamos o nosso ciclo introdutório: **Classes** (a planta baixa), **Instanciação** (a construção do objeto) e **Classes Abstratas** (as plantas mestras que orientam todo o projeto).
