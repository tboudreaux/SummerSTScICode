from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[15.305083,31.432725],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J01012+3125/sdB_GALEX_J01012+3125_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J01012+3125/sdB_GALEX_J01012+3125_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
