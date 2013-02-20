### Using PNG transparency as mask


Python script `createMask.py` requires Numpy and PIL installed. It takes two RGB PNGs: (1) an image of some field and (2) an image of a simulated gravitational lens that is contained in (1), and produces an RGBA PNG where the alpha layer represents the location of the simulated lens.

The HTML file `index.html` is an example of using the alpha layer to detect when a user clicks on a simulated lens.

Must use a local server.

	python -m SimpleHTTPServer
