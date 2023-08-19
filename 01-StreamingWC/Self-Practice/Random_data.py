import random
import time


speaking_words = [
    "hello", "world", "apple", "banana", "cat", "dog", "computer", "internet",
    "coffee", "book", "movie", "music", "friend", "family", "car", "bicycle",
    "phone", "school", "work", "beach", "mountain", "travel", "pizza", "chocolate",
    "rain", "sun", "garden", "game", "happy", "sad", "laugh", "cry", "love",
    "hug", "smile", "wave", "talk", "listen", "sing", "dance", "eat", "drink",
    "sleep", "dream", "study", "learn", "play", "watch", "read", "write", "draw",
    "paint", "create", "explore", "discover", "adventure", "fun", "exciting",
    "calm", "quiet", "colorful", "fast", "slow", "new", "old", "beautiful",
    "ugly", "interesting", "boring", "delicious", "disgusting", "warm", "cold",
    "hard", "soft", "heavy", "light", "big", "small", "happy", "angry", "surprised",
    "confused", "excited", "tired", "busy", "relaxed", "famous", "ordinary",
    "important", "meaningless", "unique", "normal", "strange", "popular", "unpopular",
    "laughter", "photograph", "creative", "refreshing", "curious", "mysterious",
    "generous", "adventure", "technology", "fantastic", "peaceful", "vibrant",
    "knowledge", "comfortable", "imagination", "inspiration", "freedom", "balance",
    "connection", "surprise", "nature", "wonder", "journey", "experience", "brave",
    "curiosity", "wander", "dreamer", "passion", "delight", "effort", "appreciate",
    "innovate", "express", "communicate", "embrace", "harmony", "celebrate",
    "courage", "motivate", "challenge", "persevere", "persistence", "transform",
    "joyful", "sincere", "determined", "optimistic", "energetic", "resilient",
    "prosperous", "grateful", "positive", "loyal", "authentic", "humorous",
    "compassionate", "mindful", "charismatic", "visionary", "ambitious",
    "independent", "compassion", "contentment", "enthusiastic", "generosity"
    # ... and many more words
]

n = len(speaking_words)
path = "/home/mayank612512/SparkStreaming/input_dir/"
path_temp = "G:/GitHub/Spark-Streaming-In-Python/01-StreamingWC/Self-Practice/input_dir/"

for i in range (0, 1000):
    with open(path + "dummy_data_"+ str(i) + ".txt", "w") as f:
        for j in range (0, 1000):
            data = str(speaking_words[random.randint(0, n-1)])
            f.write(data + ' ')
            f.flush()
            