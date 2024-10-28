# Conversor de Vídeos `.MPG` para `.MOV`

Este projeto é um script em Python que converte arquivos de vídeo no formato `.MPG` para `.MOV`. O script é especialmente útil para fluxos de trabalho em que vídeos precisam ser convertidos para o formato `.MOV` para edição em softwares como o **Final Cut Pro**, que oferece suporte otimizado para `.MOV`.

## Funcionalidades

- Converte vídeos do formato `.MPG` para `.MOV`.
- Processamento em paralelo para agilizar a conversão de grandes lotes de vídeos.
- Barra de progresso interativa para acompanhar o status da conversão.
- Compressão otimizada para balancear qualidade e velocidade.
- Verificação de arquivos já convertidos para evitar duplicações.

## Pré-requisitos

Certifique-se de ter o Python 3.x e as bibliotecas necessárias instaladas. O script utiliza:
- [moviepy](https://zulko.github.io/moviepy/): para manipulação e conversão de vídeos.
- [tqdm](https://github.com/tqdm/tqdm): para uma barra de progresso.

Instale as dependências executando:
```bash
pip install moviepy tqdm
```

## Como Usar

1. Coloque os arquivos `.MPG` no diretório raiz do projeto ou modifique o caminho do `source_dir` no código para apontar para o diretório desejado.
2. Execute o script. Ele criará automaticamente um diretório `./mov` na primeira execução para salvar os vídeos convertidos em `.MOV`.

### Explicação dos Principais Componentes

- **convert_video(filename)**: Função responsável por carregar, converter e salvar cada vídeo.
- **source_dir** e **output_dir**: Define os diretórios de entrada e saída dos arquivos.
- **ThreadPoolExecutor**: Permite conversão paralela de vídeos, acelerando o processo em sistemas com múltiplos núcleos.
- **tqdm**: Barra de progresso que indica quantos vídeos já foram processados.

## Contribuindo

1. Faça um fork do repositório.
2. Crie uma branch com a nova funcionalidade: `git checkout -b feature/nova-funcionalidade`
3. Commit suas alterações: `git commit -m 'Adicionei nova funcionalidade'`
4. Dê um push na sua branch: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

Este projeto foi desenvolvido por **Lucas Alexandre Alves Rodrigues**.
