from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        for user_log_in in self.users:
            if nickname == str(user_log_in) and hash(password) == user_log_in.password:
                self.current_user = nickname


    def register(self, nickname, password, age):
        if nickname not in map(str, self.users):
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for item in args:
            if item not in self.videos:
                self.videos.append(item)

    def get_videos(self, str_find):
        find_video = []
        for item in self.videos:
            if str(str_find).lower() in str(item).lower():  # Ищем видео
                find_video.append(str(item))
        return find_video

    def watch_video(self, title_play_video):
        if self.current_user is not None:
            for name_current_user in self.users:
                if name_current_user.nickname == self.current_user:
                    for vid in self.videos:
                        if title_play_video.lower() == vid.title.lower():
                            if vid.adult_mode is True and name_current_user.age < 18:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                            else:
                                while vid.time_now < vid.duration:
                                    vid.time_now += 1
                                    sleep(1)
                                    print(vid.time_now)
                                print("Конец видео")
                                vid.time_now = 0
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

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

