1. the program divides all the pictures int top and bottom half. it the uses differernt regression-methods to predict the bottom half based on the top half.
2. K-nn is quite good, but weird position of bottom-pic. Linear is actually pretty godd, but weird noise/black color. ridge also fine
3.
4. Divide the image into regions and learn the algorithm on patterns across these regions that will represent different parts/features of the face. This is instead of predicting the face pixel-wise

"Improve performance by replacing raw pixels with simple “face-shape features” (Haar-like features). These features describe important parts of a face (edges, dark/light areas), so the random forest has a much easier time predicting the missing half."
