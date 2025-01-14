from PIL import Image
from collections import Counter
import numpy as np

class ImageAnalyser:
    def __init__(self, path):
        self.__img = Image.open(path).convert("RGB")
        self.__pixels = list(self.__img.getdata())
        self.__counter = Counter(self.__pixels)

    def findMostCommonColor(self, count=1):
        return self.__counter.most_common(count)

    def uniqueColors(self):
        return len(set(self.__pixels))

    def calcAverage(self):
        sum_r = 0
        sum_g = 0
        sum_b = 0
        total_pixels = 0

        for (r, g, b), count in self.__counter.items():
            sum_r += r * count
            sum_g += g * count
            sum_b += b * count
            total_pixels += count

        avg_r = int(sum_r / total_pixels)
        avg_g = int(sum_g / total_pixels)
        avg_b = int(sum_b / total_pixels)

        return (avg_r, avg_g, avg_b)
    
    # Zuerst werden für je R,G,B einzelne Arrays erstellt 
    # Anschließend werden die Wert der größe nach sortiert
    # Um den Median zu finden wird jetzt der Mittlerle Wert des Arrays zurückgegeben
    def calcMedian(self):
        r_counts = Counter()
        g_counts = Counter()
        b_counts = Counter()

        for (r, g, b), value in self.__counter.items():
            r_counts[r] += value
            g_counts[g] += value
            b_counts[b] += value

        totalPixels = sum(self.__counter.values())
        median_r = self._findMedianInColor(r_counts, totalPixels)
        median_g = self._findMedianInColor(g_counts, totalPixels)
        median_b = self._findMedianInColor(b_counts, totalPixels)

        return (median_r, median_g, median_b)

    # Sortiert die gegebnene Werte und gibt den Mittleren Wert zurück
    def _findMedianInColor(self, counts, total):
        sortedValues = sorted(counts.items(), key=lambda x: x[0])
        midpoint = total // 2

        cumulative = 0
        for val, count in sortedValues:
            cumulative += count

            if cumulative > midpoint:
                return val
            
        return sortedValues[-1][0]