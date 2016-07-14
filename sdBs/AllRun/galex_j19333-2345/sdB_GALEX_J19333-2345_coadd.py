from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[293.348583,-23.764881],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J19333-2345/sdB_GALEX_J19333-2345_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J19333-2345/sdB_GALEX_J19333-2345_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()