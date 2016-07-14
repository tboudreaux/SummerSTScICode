from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.6605,3.313283],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J16546+0318/sdB_GALEX_J16546+0318_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J16546+0318/sdB_GALEX_J16546+0318_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
