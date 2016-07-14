from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[171.000292,-9.476136],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J11240-0928/sdB_GALEX_J11240-0928_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J11240-0928/sdB_GALEX_J11240-0928_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
