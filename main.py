from pytube import Playlist, YouTube
import os

def download_video(video, output_path):
    try:
        print(f'Downloading {video.title}...')
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=output_path)
        print(f'Finished downloading {video.title}')
    except Exception as e:
        print(f'Error downloading {video.title}: {e}')

def download_playlist(playlist_url, playlist_name):
    playlist = Playlist(playlist_url)
    output_path = os.path.join(os.getcwd(), playlist_name)
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    print(f'Starting download of playlist: {playlist_name}')
    for video in playlist.videos:
        download_video(video, output_path)
    
    print(f'Finished downloading playlist: {playlist_name}')

if __name__ == '__main__':
    playlist_url = input('Enter the playlist URL: ')
    playlist_name = input('Enter the playlist name: ')
    download_playlist(playlist_url, playlist_name)
