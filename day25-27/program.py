import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search:')

    try:
        results = api.find_movie_by_title(keyword)

        print('There are {} movies found.'.format(len(results)))

        for result in results:
            print("{} with code {} has score {}".format(
                result.title, result.imdb_code, result.imdb_score))
    except requests.exceptions.ConnectionError:
        print('Error: Could not find server. Check your network connection.')

    except ValueError:
        print('Error: You must specify a search term.')

    except Exception as ex:
        print('Oh that didn\'t work: {}'.format(ex))

if __name__ == '__main__':
    main()
