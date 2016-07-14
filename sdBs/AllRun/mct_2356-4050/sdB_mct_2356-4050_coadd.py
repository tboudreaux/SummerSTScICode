from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[359.791042,-40.555475],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_mct_2356-4050/sdB_mct_2356-4050_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_mct_2356-4050/sdB_mct_2356-4050_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()