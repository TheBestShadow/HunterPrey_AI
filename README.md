# HunterPrey_AI
Desenvolvido por Leonardo Saraiva, Gabriel Pedroso e Hector Alexandre para cadeira de IA na UniRitter

Desenvolvido em python e com visualização simples.

O jogo foi divido em 4 classes:
Game, que é a classe que roda o jogo. 
Grid, que é a classe que define a como a matriz será visualizada, e seu tamanho.
Prey, onde é definida a IA da caça, seus comportamentos e movimentos na grid.
Hunter, onde é definida a IA do caçador, seus comportamentos e sua movimentação na grid.

## Prey
Aqui é iniciado as Preys, onde são definidos seu ID (O qual será sua visualização na grid) e posição inicial.

![image](https://user-images.githubusercontent.com/26562023/234450221-2eda2f78-f6fe-4530-8ea7-c60e7ef004a0.png)

Aqui definimos as opções de movimentação possível para caça e em seguida, checamos sua posição na grid para ver se a caça está nos limites da grid, e caso esteja, removemos as opções de movimentação que resultariam em um movimento que a levaria para fora da grid, criando erros. Após isso ele escolhe aleatoriamente um dos movimentos e o executa.

![image](https://user-images.githubusercontent.com/26562023/234452666-9472b99b-9c94-4fd8-8a9c-a061dd891e5d.png)

Este if checa se a movimentação escolhida está dentro dos conformes e não vai para fora da grid, e se estiver tudo certo, moved vira true e o movimento é contado no turno.
Abaixo disso temos a inicialização da caça na grid e sua visualização, que é baseada no seu ID.

![image](https://user-images.githubusercontent.com/26562023/234452177-c1191ac9-38f5-4dd8-ba21-0bfcbb11ad37.png)

## Hunter
A máquina de estados do caçador tem dois estados, patrulhando e caçando. Quando está patrulhando ele anda de forma aleatória, exatamente da mesmma forma que a caça age o tempo todo. A diferença aqui é a criação de um novo estado cuja transição ocorre quando o caçador vê uma caça há no máximo 5 células distantes de si.

Aqui implementamos uma função que checa na range da grid se há alguma caça visível, baseado no seu alcance de visão, caso não haja nada, ele continua no estado de patrulha, e caso haja uma caça na visão, a transição de estados ocorre.

![image](https://user-images.githubusercontent.com/26562023/234454391-4d1e4747-b85f-4a91-bcde-86da9d53ae9f.png)

Pra fazer a movimentação deste estado do caçador, ele checa a posição atual da caça e e decide seu próximo movimento na grid baseado nisto.

![image](https://user-images.githubusercontent.com/26562023/234454605-08d55c73-401d-4680-867d-7eaa3826bb9c.png)

## Grid 

Criação da grid usando uma matriz bidimensional. Inicialmente criamos as linhas e colocamos 'X' nelas, e em seguida preenchemos o resto dos espaços de acordo com o tamanho da grid que pode ser definido.

![image](https://user-images.githubusercontent.com/26562023/234455110-e6cb5f59-ce5d-4647-8024-e3d7f3dd658e.png)

## Game

Defininido uma checagem para ver se há caças presentes no mapa.

![image](https://user-images.githubusercontent.com/26562023/234455660-9d5772ed-d30e-404b-be03-98c725528d30.png)

Iniciamos as as caças, entre 5 e 9, e em seguida definimos o tamanho que desejamos da grid usando grid = Grid( ), entre parenteses colocamos o tamanho desejado. 
Em seguida inserimos o caçador no mapa.
Abaixo definimos o número de caças que será inserido no mapa, de maneira aleatória e depois as inserindo.
Depois printamos a grid, e no sleep() definimos em segundos a duração de cada turno.
Por fim enquanto o número de caças for maior que 0, fazemos, em sequência, a movimentação da caça e depois do caçador.

![image](https://user-images.githubusercontent.com/26562023/234456004-0ac92c88-88e3-4db3-b3b3-344866d8cbcd.png)


