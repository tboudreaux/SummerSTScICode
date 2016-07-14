from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.803167,10.954667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_egb_5/sdB_egb_5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_egb_5/sdB_egb_5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
