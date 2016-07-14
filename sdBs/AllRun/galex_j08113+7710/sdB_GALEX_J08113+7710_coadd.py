from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.849083,77.169164],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J08113+7710/sdB_GALEX_J08113+7710_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J08113+7710/sdB_GALEX_J08113+7710_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
