def get_supermarkets(loc, search_string='supermarket', distance=miles_to_meter(2)):
    business_list = []
    map_client = googlemaps.Client(API_KEY)
    # print(loc)
    response = map_client.places_nearby(
        location = loc,
        keyword = search_string,
        name = "supermarket",
        radius = distance
    )
    # print("here")
    business_list.extend(response.get('results'))
    # next_page_token = response.get('next_page_token')

    df = pd.DataFrame(business_list)
    df['url'] = 'http://www.google.com/maps/place/?q=place_id:' + df['place_id']
    df.sort_values('rating', inplace=True, ascending=False)
    
    return df
