from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.382167,74.350039],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_1706+7424/sdB_HS_1706+7424_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_1706+7424/sdB_HS_1706+7424_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
