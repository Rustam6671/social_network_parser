import requests


class Vk_parser:
    def __init__(self, hashtag):
        self.__token = '99f6089799f6089799f60897f699835abf999f699f60897c63d59bb4a198eaa83d5f356'
        self.__VERSION = 5.126
        self.__COUNT = 10
        self.__q = hashtag
        self.__posts = self.__request_data()
        self.__photo_storage = []

    def __fill_in_the_photo_storage(self):
        """
        Этот метод заполняет хранилище фотографий ("photo_storage") экземплярами класса Photo
        Это главный метод в этом модуле, поскольку он занимается создание объектов
        Внимание!!! Этот метод записывает только фотографии пользователей.
        """
        # TODO приложение записывает удаленных пользователей, сделай фильтр, чтобы такие фото не попадали в список

        for post in self.__posts:
            user_id = self.__get_user_id(post)
            user = self.__request_user(user_id)
            url = self.__get_photo_url(post)
            if user_id > 0 and 'deactivated' not in user and url is not None:  # ID пользователей имеют положительные числа, а группы - отрицательные
                photo_parameters = {
                    'url': url,
                    'likes': self.__get_photo_likes(post),
                    'data': self.__get_photo_date_of_publication(post),
                    'user_id': user_id,
                    'user': str(self.__get_user_name(user)),
                    'user_photo': self.__get_user_photo(user)
                }
                photo = Photo(photo_parameters)
                self.__photo_storage.append(photo)

    def __request_data(self):
        data = requests.get('https://api.vk.com/method/newsfeed.search',
                            params={
                                'access_token': self.__token,
                                'v': self.__VERSION,
                                'q': self.__q,
                                'count': self.__COUNT
                            }).json()['response']['items']
        return data

    def __request_user(self, user_id):
        user = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': self.__token,
                                'v': self.__VERSION,
                                'lang': 0,
                                'user_ids': user_id,
                                'fields': 'photo_max, domain, deactivated'
                            }).json()['response'][0]
        return user

    def __get_photo_url(self, post):
        """
        Метод проверяет метод проводит проверку поста на наличие медиафайлов ("attachments")
        в виде фотографий ("photo").
        При успешной проверке возвращает URL фотографии
        При неуспешной проверке возвращает None
        :return: URL:str or none
        """
        photo_url = None

        if 'attachments' in post and 'photo' in post['attachments'][0]:
            photo_url = post['attachments'][0]['photo']['sizes'][-1]['url']

        return photo_url

    def __get_photo_likes(self, post):
        like_counter = post['likes']['count']
        return like_counter

    def __get_photo_date_of_publication(self, post):
        """
        Возвращает дату публикации поста в формате unixtime
        :param post:dict
        :return:int
        """
        date_of_publication = post['date']
        return date_of_publication

    def __get_user_id(self, post):
        user_id = post['id']
        return user_id

    def __get_user_name(self, user_obj):
        user_name = str(user_obj['first_name'] + ' ' + user_obj['last_name'])
        return user_name

    def __get_user_photo(self, user):
        user_photo = user['photo_max']
        return user_photo

    def get_photo_storage(self):
        self.__fill_in_the_photo_storage()
        return self.__photo_storage


class Photo:
    def __init__(self, photo_parameters):
        self.url = photo_parameters['url']
        self.likes = photo_parameters['likes']
        self.data = photo_parameters['data']
        self.user_id = photo_parameters['user_id']
        self.user = photo_parameters['user']
        self.profile_photo = photo_parameters['user_photo']

    def __str__(self):
        return f"url: {self.url} \n" \
               f"likes: {self.likes} \n" \
               f"data: {self.data} \n" \
               f"user_id: {self.user_id} \n" \
               f"user: {self.user} \n" \
               f"profile_photo: {self.profile_photo} \n"


if __name__ == '__main__':
    pars1 = Vk_parser('#photo')
    photos = pars1.get_photo_storage()
    print(1)
