from tqdm import tqdm
import requests

def download_file(url, save_path):
    """
    Download a file from URL with progress bar
    
    Args:
        url (str): URL of the file to download
        save_path (str): Path to save the file as
    """
    GREEN = '\033[92m'
    RESET = '\033[0m'
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(save_path, 'wb') as file, tqdm(
        desc=save_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
        colour='green',
        bar_format=f'{GREEN}{{l_bar}}{{bar}}{RESET}{GREEN}{{r_bar}}{RESET}' 
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.update(size)
