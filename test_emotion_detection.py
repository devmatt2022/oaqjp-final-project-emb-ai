import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        tests = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for test in tests:
            stmt,dominant_emotion = test
            self.assertEqual(emotion_detector(stmt)["dominant_emotion"], dominant_emotion)

unittest.main()
