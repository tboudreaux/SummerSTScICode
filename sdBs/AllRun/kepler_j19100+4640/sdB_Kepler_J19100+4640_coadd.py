from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.50125,46.673611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19100+4640/sdB_Kepler_J19100+4640_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19100+4640/sdB_Kepler_J19100+4640_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
