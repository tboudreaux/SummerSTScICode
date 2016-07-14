from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[11.9185,31.398633],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J00476+3123/sdB_GALEX_J00476+3123_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J00476+3123/sdB_GALEX_J00476+3123_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
