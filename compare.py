from engine import FaceRecognitionDatabase

# Initialize and build the database
db = FaceRecognitionDatabase()
db.build_database()

# Example: Compare a new face against the database
test_image = "X.jpg"  # Replace with your test image
results = db.compare_face(test_image)

if results:
    print(f"\nTop 10 most similar faces to {test_image}:")
    for name, similarity in results:
        print(f"{name}: {similarity:.2f}% similarity")
else:
    print(f"No faces found for comparison in {test_image}")