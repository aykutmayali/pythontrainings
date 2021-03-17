# in terminal
# pip install pytube

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   from pytube import YouTube
   url= "https://www.youtube.com/watch?v=jXKXjouY_h4"
   YouTube(url).streams.first().download()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


