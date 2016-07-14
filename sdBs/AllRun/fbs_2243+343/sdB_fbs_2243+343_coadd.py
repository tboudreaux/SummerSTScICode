from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[341.483,34.594917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2243+343/sdB_fbs_2243+343_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2243+343/sdB_fbs_2243+343_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
