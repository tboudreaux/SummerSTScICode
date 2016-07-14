from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[341.446333,39.443556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2243+392/sdB_fbs_2243+392_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2243+392/sdB_fbs_2243+392_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
