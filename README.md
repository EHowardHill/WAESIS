# WAESIS
 Worldwide Algorithmic Expression Screening and Identification System

Now, you too can be a WAESIS-t™!

You want to install requirements with:
`pip install -r requirements.txt`

The program is designed to be used as a library. You'll use it like this:

```
import engine

engine.compare("Barack-Obama.webp")
```

The output will be something like:
```
Loading existing face database from face_database.pkl
Loaded 466 face encodings

Top 10 most similar faces to Barack-Obama.webp:
South Arabian:
33.06% similarity

Vedda:
33.01% similarity

Trans Mediterranid:
32.83% similarity

Alföld:
32.74% similarity

South Gondid:
32.27% similarity

Strandlooper:
32.16% similarity

Paleo Sardinian:
31.35% similarity

Subandids:
30.93% similarity

Western Desert:
30.82% similarity

Mundari:
30.58% similarity
```