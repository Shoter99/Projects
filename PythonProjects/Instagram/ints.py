from instapy_cli import client

username = 'dawid_roszman'
password = 'D075p08!'
image = 'posts/'+input("Jaki nazywa się plik? ")
text = input('Jaki ma być opis: ')


def Upload():
    with client(username, password) as cli:
        cli.upload(image, text)


Upload()
