### Este é um projeto desenvolvido para o curso de desenvolvimento web full-stack da Trybe, Módulo Ciência da Computação.  
  
A aplicação é um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.  
  
São aceitos os formatos **CSV**, **JSON** e **XML**

Os tipos de relatório disponiveis são: **simples**, **completo** e **colorido**(com as mesmas informações do simples).
  
Este foi meu segundo projeto em Python e que me ensinou demais sobre a liguagem e como a POO se aplica a ela, além de entender porque esta linguagem é tão utilizada para manipulação e leitura de dados em arquivos para os mais diversos fins, sendo quase tudo muito intuitivo, e mesmo para as poucas coisas que não são, têm sempre ferramentas fáceis de encontrar que simplificam a execução, como é o caso da biblioteca xmltodict.  
  
## Tecnologias utilizadas:  
<details>  
  <summary>Clique para expandir</summary>  
  
* Python;  
* csv(library);  
* json(library);  
* xmltodict;  
* Pytest;  

</details>  
  
## Rodando a aplicação
  
<details>  
  <summary>Clique para expandir</summary>
  Você pode rodar a aplicação na sua máquina através do terminal, na pasta onde será instalada:  
  
```
git clone git@github.com:R-R-Freitas/Inventory-Report.git
cd Inventory-Report  
pip install .  
python3 -m pip install -r dev-requirements.txt  
pip install python-dotenv  
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>  
```  
Exemplo:  
  
```  
inventory_report inventory_report/data/inventory.csv colorido  
```  
</details>

### Ponto de partida do desenvolvimento:  
Ou: créditos à participação da Trybe no projeto  
<details>  
  <summary>Clique para expandir</summary>  
  
  A Trybe disponibilizou um projeto parcialmente pronto. O "Initial Commit" deste repositório contém os arquivos e códigos de autoria da Trybe.  
    
</details>  
