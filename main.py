import json

def handle_json():
    with open('a20plus.json') as f:
        data = json.load(f)
    all_songs = data.get('songs')
    # For each song...
    for song in all_songs:
        # For each chart in this song...
        charts = song.get('charts')
        for chart in charts:
            # Initialize "mtgColor" to "uncolored"
            chart['mtgColor'] = 'uncolored'
        song['charts'] = charts
    
    # Update the songs with this new metadata attribute
    data['songs'] = all_songs
    # Write to the output file.
    with open('ee23_a20plus.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)





if __name__ == "__main__":
    handle_json()