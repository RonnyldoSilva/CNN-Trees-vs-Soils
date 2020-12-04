# Desafio De Visão Computacional

## Problema:

Em platações de pinheiros do tipo pinus (_Pinus palustris_), um dos maiores desafios é a verificar a densidade das plantações.
Para resolver esse problema, sobreovamos as plantaçoes com um drone e capturamos imagens perpendiculares ao chão, 
mantendo uma altura constante.

A equipe de engenheiros florestais que opera os drones utlizou um software do drone para 
combinar todas as imagens do voo em uma só imagem de toda a plantação (imagem mozaico).
Para facilitar o processamento, esse mozaico foi dividido em pequenos blocos (imagens) sem sobreposição, 
todos com o mesmo tamanho, contendo no máximo de 1 árvore de pinus por imagem.

Agora precisamos de um software que indentifique quais desas imagens contem árvores do tipo pinus.


## Objetivo:

Sua tarefa é desenvolver um sistema de visão computacional que identifique quais imagens contem pinheiros.

O problema pode ser resolvido usando qualquer linguagem, bibliotecas e/ou frameworks. 
Se você se basear em tutoriais e/ou códigos de exemplo ou copiar trechos de código de algum lugar, 
por favor indique esses trechos explicitamente.
Inclua em sua solução tam bé o código fonte para treinamentoe e validações que você utilizou para obter o modelo final.

Caso julgue necessário, você também pode realizar altereções no dataset, como limpeza dos dados ou remoção de amostras.
  

## Dataset

No diretório `Data` encontram-se as amostras das imagens.
Há dois tipos de imagens: árvores e solo.
Eles são identificados com um sulfixo: 
`_tree` para as imagens com pinheiros (que desejamos identificar) e 
`_soil` para as demais imagens.


## Entregas

* **Análize exproratoria dos dados (EDA)**: avaliação dos dados fornecidos na pasta Data

* **Aplicação**: um software de predição que seja capaz de identificar imagens com pinheiros, diferenciando das demais. 
Esse software deve receber uma imagem e retornar uma predição para ela (pinheiro ou solo).
Pode ser uma aplicação em linha de comando, que imprima o resultado no terminal.
    * BONUS: desenvolva uma API REST ou uma interface grafica (GUI) para realizer a inferência de novas imagens


* **Relatório**: apresentano a estratégia, metodologia e arquitetura utilizadas e os resultados obtidos. 
Pode ser em slides (.ppt e afins), texto (PDF) ou mesmo um notebook do Jupyter.


## Avaliação

Você deverá registrar todos os seus commits neste repositório. 
Queremos ver o passo-a-passo do desenvolvimento da aplicação.


Parte da nossa avalição envolve rodar seu código no nosso ambiente, 
então você pecisa nos fornecer as instruções necessária para faze-lo.
Você pode utilizar ferarmentas e scritps de deploy (docker, nginx, Jenkins, etc.) que facilitem a execução da aplicação, 
mas ainda assim deve fornecer o código fonte da solução. 


Em caso de dúvidas, pergunte. Boa sorte!

