from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[200.660417,26.116267],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_1320+2622/sdB_HS_1320+2622_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_1320+2622/sdB_HS_1320+2622_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
