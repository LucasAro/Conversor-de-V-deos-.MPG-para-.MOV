import os
from moviepy.editor import VideoFileClip
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Diretórios de origem e saída
source_dir = './'
output_dir = './mov'

# Cria o diretório de saída, caso não exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def convert_video(filename):
    """Converte um único arquivo .MPG para .MOV."""
    if filename.endswith('.MPG'):
        filepath = os.path.join(source_dir, filename)
        new_filename = os.path.splitext(filename)[0] + '.mov'
        output_path = os.path.join(output_dir, new_filename)

        # Verifica se o arquivo já foi convertido
        if os.path.exists(output_path):
            print(f'Skipping {filename} (already converted)')
            return

        print(f'Convertendo: {filename} -> {new_filename}')
        try:
            # Carrega o vídeo
            clip = VideoFileClip(filepath)
            # Converte para .mov com configuração de compressão otimizada
            clip.write_videofile(output_path, codec='libx264', audio_codec='aac', preset='fast')
            print(f'Convertido: {filename} -> {new_filename}')
        except Exception as e:
            print(f'Erro ao converter {filename}: {e}')
        finally:
            # Fecha o arquivo para liberar memória
            clip.reader.close()
            clip.close()

# Lista de todos os arquivos na pasta de origem
filenames = [f for f in os.listdir(source_dir) if f.endswith('.MPG')]

# Converte os vídeos em paralelo com uma barra de progresso
with ThreadPoolExecutor() as executor:
    list(tqdm(executor.map(convert_video, filenames), total=len(filenames)))

print('Conversão concluída!')
