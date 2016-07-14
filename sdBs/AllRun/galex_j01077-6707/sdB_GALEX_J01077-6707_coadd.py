from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[16.940792,-67.128408],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J01077-6707/sdB_GALEX_J01077-6707_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J01077-6707/sdB_GALEX_J01077-6707_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()