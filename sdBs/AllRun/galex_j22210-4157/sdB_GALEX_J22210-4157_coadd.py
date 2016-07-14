from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[335.271208,-41.961603],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J22210-4157/sdB_GALEX_J22210-4157_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J22210-4157/sdB_GALEX_J22210-4157_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
