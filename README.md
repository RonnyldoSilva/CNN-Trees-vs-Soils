# Classificação de árvores e solos {CNN, OpenCV, Python}

:star::star::star::star::star: (If it was useful, leave a star)

Desenvolver um classificador que identifica se uma imagem é uma árvore, ou um solo.

![Exemplo](https://github.com/RonnyldoSilva/CNN-Trees-vs-Soils/blob/main/img/example.png)

# Como executar?  

1 - Instale o Docker e execute os seguintes comandos:

- docker build . -t tree-vs-soil:v1
- docker run -it --name cont_1 tree-vs-soil:v1 

Se tudo ocorrer bem, você será capaz e executar as duas próximas etapas.

2 - **Executando notebook utilizado para o treinamento do modelo**

- jupyter-notebook classifier.ipynb

3 - **Executando script para teste manuais**

- python3 main.py -i imagem

Exemplo de execução:
- python3 main.py -i 0000_soil.png

.

.

.

Resultado: soil.

# Solução

Primeiramente, o problema se demostrou simples, e com complexidade baixa, devio a existência de apenas 2 classes (tree e soil), e de a base de dados ser bastante organizada, balanceada aproximada 50% para árvore e solo, respectivemente, e possuir uma boa quantidade de exemplos.

Disto tudo isso, percebi que o problema a ser resolvido é bastante similar ao projeto que trabalhei, o programa Farmácia Popular do governo federal, o qual exigiu um classificador para mais de 20 tipos de documentos reais.

Decidi utilizar Redes Neurais Convolucionais, do framework TensorFlow, por esta apresentar bom desempenho e está atualmente no main stream.

TRAIN_DIR e TEST_DIR foram configurados de acordo com a conveniência do problema e com os hiperparâmetros básicos como epoch, learning rate, para melhor acurácia. Converti a imagem para tons de cinza, para que só tenhamos que lidar com a matriz 2-d, caso contrário, a matriz 3-d é difícil de aplicar diretamente CNN. Garanti que as imagens fossem 50x50, e a proporção de treino e teste foram 80% e 20%, respectivamente, seguindo as boas práticas. Novamente, a base de dados fornecida estava muito estruturada.

- O modelo treinado obteve 92% de acurácia.

Além disso, removi 100 imagens, as quais nunca estiveram na base de treinamento e teste do modelo apresentado. As 100 foram utilizadas para teste real.

- No teste real, a acurácia foi de 95%.

Estes resultados são muito bons! :D

Os próximos passos seriam utilizar:

- Arquiteturas profundas.
- Otimização dos hiperparametros.
- Fine Tunning e Transfer Learning.

Também seria ótimo fazer um teste de sanidade na base de dados, para encontrar e remover outliers e dados que não fazem sentido no mundo real.

# Bibliotecas necessárias:

- TFLearn - Biblioteca de aprendizado profundo com uma API de nível superior para TensorFlow usada para criar camadas da CNN.

- tqdm - Faça instantaneamente seus loops mostrarem um medidor de progresso inteligente, apenas para criar um projeto simples.
     
- numpy - para processar as matrizes de imagem.

- OpenCV - Para processar a imagem como convertê-la em tons de cinza e etc.
     
- os - Para acessar o sistema de arquivos para ler a imagem do diretório de treinamento e teste de nossas máquinas.

- random - para embaralhar os dados para superar a polarização.
     
- matplotlib - Para exibir o resultado de nosso resultado preditivo.

- tensorflow - Basta usar o tensorboard para comparar a curva de perda e adam nos nossos dados, seja no resultado ou no log obtido.

# Referências de aprendizagem de máquina utilizadas:

- Andrew Ng Machine Learning Course on Coursera
- Machine Learning : A probabilistic Approach by Kevin Murphy
- Reddit community for Machine Learning.
- Machine Learning GeeksforGeeks
- Siraj Raval – YouTube

# Referências para Redes Neurais Convolucionais:

- Jupyter Notebook – Conv_Net
- Wikipedia – Convolutional Neural Networks
- Stanford Course – cs231n

Lembre-se, quanto mais simples, melhor! :D
