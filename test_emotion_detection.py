import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        # Test cases with expected dominant emotions
        test_cases = [
            ("I am glad this happened", 'joy'),
            ("I am really mad about this", 'anger'),
            ("I feel disgusted just hearing about this", 'disgust'),
            ("I am so sad about this", 'sadness'),
            ("I am really afraid that this will happen", 'fear'),
        ]

        for text, dominant_emotion in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                # Get the emotion with the highest score
                self.assertEqual(result['dominant_emotion'], dominant_emotion)

if __name__ == '__main__':
    unittest.main()