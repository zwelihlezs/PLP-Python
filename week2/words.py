words = ['go', 'marry', 'park', 'assists', 'pick', 'status', 'bed', 'operate', 'smoke', 'enforce']

result = [(len(word) % 2==1) for word in words ]


odd_length_words = [word for word in words if len(word) % 2 != 0]

print(f"Words with an odd number of characters: {odd_length_words}")


