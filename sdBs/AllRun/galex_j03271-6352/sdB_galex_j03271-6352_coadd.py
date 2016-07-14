from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[51.791625,-63.881397],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j03271-6352/sdB_galex_j03271-6352_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j03271-6352/sdB_galex_j03271-6352_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
