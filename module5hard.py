from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class UrTube:
    video = []
    users = []

    def __init__(self):
        self.users = self.users
        self.videos = self.video
        self.current_user = None

    '''
    def log_in(self, nickname, password):

        pass
    '''

    def register(self, nickname, password, age):
        if nickname not in self.users:
            User(nickname, password, age)
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    '''
    def log_out(self):
        self.current_user = None

    '''

    def add(self, *args):
        for item in args:
            if item not in self.video:
                self.video.append(item)

    def get_videos(self, str_find):
        find_video = []
        for item in self.video:
            if str(str_find).lower() in str(item).lower():
                find_video.append(str(item))
        return find_video

    def watch_video(self, title_play_video):
        if title_play_video.lower() in map(str.lower, map(str, self.video)):  # Ищем видео по названию
            i = 0
            while i < 5:  # "Включаем" видео. Вместо i < 5 должны быть атрибуты time_now < duration из экземпляра класса Video
                i += 1
                sleep(1)
                print(i)
            print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
'''
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
'''
