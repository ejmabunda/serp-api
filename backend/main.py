from serpapi import GoogleSearch

def main():
    """Entry point
    """
    params = {
        'engine': 'google',
        'q': '',
        'api_key': 'e2bca6bfbf9f5733c3a3d60cf6e41ad0cbf48ae3ff96ebff121889cdaef3e452'
    }

    search = GoogleSearch(params)
    print(search.get_dict())

if __name__ == '__main__':
    main()
