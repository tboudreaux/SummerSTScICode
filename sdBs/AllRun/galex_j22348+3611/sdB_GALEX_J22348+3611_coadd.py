from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[338.720458,36.184708],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J22348+3611/sdB_GALEX_J22348+3611_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J22348+3611/sdB_GALEX_J22348+3611_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
