import requests

link_file = 'https://b1.filmpro.ru/c/494083.700xp.jpg'

link_video = 'https://samplelib.com/lib/preview/mp4/sample-5s.mp4'

class Download:
    def __init__(self, format, file, name_file):
        self.format = format
        self._file = file
        self.name_file = name_file

    def download(self):
        try:
            if self.format == 'image':
                response = requests.get(url=self._file)

                with open(f'{self.name_file}.jpg', 'wb') as file:
                    file.write(response.content)

                return 'Img successfully downloaded!'
            elif self.format == 'video':
                response = requests.get(url=self._file, stream=True)

                with open(f'{self.name_file}.mp4', 'wb') as file:
                    for chuck in response.iter_content(chunk_size=1024 * 1024):
                        if chuck:
                            file.write(chuck)

                return 'Video successfully downloaded!'

        except Exception as _ex:
            return 'Check your URL!'

test = Download('video', link_video, 'Foop')
print(test.download())