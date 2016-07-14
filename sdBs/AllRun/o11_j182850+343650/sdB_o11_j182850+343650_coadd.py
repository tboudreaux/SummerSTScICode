from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[277.208333,34.613889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j182850+343650/sdB_o11_j182850+343650_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j182850+343650/sdB_o11_j182850+343650_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
